# ARCHITECT-

This repository contains custom Odoo modules. Follow these steps to set up an Odoo development environment and run the server.

## 1. Install System Packages

```bash
apt-get update
apt-get install -y git python3-pip python3-dev build-essential wget postgresql-client
```

## 2. Install Python Dependencies

```bash
pip3 install wheel setuptools psycopg2-binary
pip3 install babel decorator docutils ebaysdk Jinja2 lxml Mako MarkupSafe num2words passlib Pillow psutil pydot pyparsing PyPDF2 python-dateutil python-stdnum pytz PyYAML qrcode reportlab requests six suds-py3 vatnumber vobject Werkzeug XlsxWriter xlwt xlrd
```

## 3. Clone Repositories

```bash
git clone https://github.com/sidmidccompany/ARCHITECT-.git /workspace/my_odoo_module
git clone https://github.com/odoo/odoo.git /workspace/odoo
```

## 4. Install Odoo Requirements

```bash
pip3 install -r /workspace/odoo/requirements.txt
```

## 5. Configure Odoo

Create a configuration file using your database credentials:

```bash
cat << EOF > /workspace/odoo/debian/odoo.conf
[options]
addons_path = /workspace/odoo/addons,/workspace/my_odoo_module
db_host = ${ODOO_DB_HOST}
db_user = ${ODOO_DB_USER}
db_password = ${ODOO_DB_PASSWORD}
db_port = 5432
log_level = info
EOF
```

## 6. Start the Odoo Server

```bash
python3 /workspace/odoo/odoo-bin -c /workspace/odoo/debian/odoo.conf
```

The server will be accessible on port 8069 by default.
