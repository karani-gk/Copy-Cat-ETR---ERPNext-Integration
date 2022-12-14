## Copy Cat ESD - KRA

[ERPNext](https://erpnext.com) Integration to the [Copy Cat Group ESD](https://www.copycatgroup.com/) Gadget for tax reporting.

### Main Features

1. East to Integrate
2. Supports ERPNext version 12, 13 and 14 with minor change on the hooks file as described below
3. Automatically send the invoice data to KRA for signing
4. Automatically appends the e-Signature on the invoice

### How to Install
```
bench get-app https://github.com/karani-gk/Copy-Cat-ETR---ERPNext-Integration.git
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
bench --site [your.site.name] migrate
```
```
supervisorctl restart all
```

### License

MIT
