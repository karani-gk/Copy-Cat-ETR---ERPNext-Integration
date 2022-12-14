import frappe
import requests
import json

class CopyCatGroupESD:
    def process_invoice_information(self, invoice_number):
        item_data = ['name', 'item_code', 'item_name', 'qty', 'rate', 'amount', 'uom', 'item_tax_template']
        items = frappe.get_all("Sales Invoice Item", {"parent": invoice_number}, item_data)
        
        deonItemDetails = []
        new_item = {}
        
        for item in items:
            item_tax_rate = frappe.get_value("Item Tax Template Detail", {"parent": item.item_tax_template}, 'tax_rate')
            
            vatClass = self.get_vat_class(item_tax_rate)
            
            new_item = {
                "hsDesc":"",
                "namePLU": item.item_name,
                "taxRate": item_tax_rate,
                "unitPrice": item.rate,
                "discount": 0,
                "hsCode": "",
                "quantity": item.qty,
                "measureUnit": item.uom,
                "vatClass": vatClass
            }
            
            deonItemDetails.append(new_item)
            
        return self.process_payload(invoice_number, deonItemDetails)
    
    
    
    def get_vat_class(self, item_tax_rate):
        if item_tax_rate == 16:
            vatClass = "A"
        elif item_tax_rate == 8:
            vatClass = "B"
        elif item_tax_rate == 0:
            vatClass = "C"
        elif item_tax_rate == "Exempt":
            vatClass = "D"
            
        return vatClass
    
            
    def process_payload(self, invoice_number, deonItemDetails):
        payload = {
            "deonItemDetails": deonItemDetails,
            "senderId": frappe.db.get_single_value('Copy Cat ESD', 'sender_id'),
            "invoiceCategory":"tax_invoice",
            "traderSystemInvoiceNumber":  invoice_number,
            # "traderSystemInvoiceNumber":  "INV-20102",
            "relevantInvoiceNumber": "",
            "pinOfBuyer": "",
            "invoiceType": "Original",
            "exemptionNumber": "",
            "totalInvoiceAmount": frappe.db.get_value('Sales Invoice', invoice_number, 'grand_total'),
            "systemUser": "Karani"
            }
        
        return payload
        
        




@frappe.whitelist()
def process_invoice(invoice_number):
    new_request = CopyCatGroupESD()
    payload = new_request.process_invoice_information(invoice_number)
    
    url = "http://197.248.30.164:5000/EsdApi/deononline/signinvoice"
    
    response = requests.post(url, json=payload)
    data = json.loads(response.text)
    
    print(f"\n\n\n {payload} \n\n\n")
    print(f"\n\n\n {data} \n\n\n")
    
    qr_code = frappe.get_doc({
        "doctype":"QR Demo", 
        "title": data['qrCode'],
        "invoice_number": invoice_number
    })
    
    qr_code.insert()
    frappe.db.commit()
    
    
    return data



def get_qr_code(doc):
    qr_code = frappe.db.get_value("QR Demo", {'invoice_number': doc.name}, ['qr_code'])

    return qr_code
    