# Copyright 2021 Pierre Verkest <pierreverkest84@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Base Group Backend",
    "version": "11.0.1.0.0",
    "category": "Tools",
    "author": "Pierre Verkest, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "website": "https://github.com/OCA/server-backend",
    "depends": ["base", "mail"],
    "data": [
        "data/res_groups.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
}
