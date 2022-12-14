## Copy Cat ESD - KRA

[ERPNext](https://erpnext.com) Integration to the [Copy Cat Group ESD](https://www.copycatgroup.com/) Gadget for tax reporting.

### Maintenance
This repository is managed by [Geoffrey Karani](https://www.linkedin.com/in/karani-gk), [Upeosoft Limited](https://upeosoft.com) and [Code with Karani](https://codewithkarani.com)

### License
This integration is provided and serviced under the MIT License

This integration is developed and maintained by [Upeosoft Limited](https://upeosoft.com) and contributors. The copyright is owned by [Upeosoft Limited](https://upeosoft.com) and contributors. The software comes as-is without any warranty.

### Main Features

1. East to Integrate
2. Supports ERPNext version 12, 13 and 14 with minor change on the hooks file as described below
3. Automatically send the invoice data to KRA for signing
4. Automatically appends the e-Signature on the invoice

### How to automatically append the e-Signature on your invoices
Appending the e-signature automatically on your signed invoices requires thr [QR Demo](https://github.com/alyf-de/frappe_qr_demo) application. This is the application responsible for converting the signature to a QR code that can be appended to the invoice.

### Compatibility
Supports ERPNext versions 12 and 13 out of the box.


If you want to use this integration with version 14, do the following:


In the *hooks.py* file, do the following:


**Remove this piece of code**

This is referred to as the **jenv** block

```
jenv = {
	"methods": [
		"get_qr_code:copycatesd.services.rest.get_qr_code"
	]
}
```

**Add this piece of code**

This is referred to as the **jinja** block

```
jinja = {
	"methods": [
		"copycatesd.services.rest.get_qr_code"
	]
}
```

You can also opt to un-comment the *jinja block* and comment or delete the *jenv block* in the *hooks.py* file


### How to Install
```
bench get-app https://github.com/karani-gk/Copy-Cat-ETR---ERPNext-Integration.git
```
```
bench get-app https://github.com/alyf-de/frappe_qr_demo.git
```
```
bench setup requirements
```
```
bench restart
```
```
bench --site [your.site.name] install-app copycatesd
```
```
bench --site [your.site.name] install-app qr_demo
```
```
bench --site [your.site.name] migrate
```
```
supervisorctl restart all
```

### Update
Run updates with

```
bench update
```

You may also need to update the dependencies with the following command

```
bench update --requirements
```
