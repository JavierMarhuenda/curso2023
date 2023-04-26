# Copyright <2023> <Javier Marhuenda>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk ticket",
    "summary": "Helpdesk tickets",
    "version": "16.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    "development_status": "Alpha|Beta|Production/Stable|Mature",
    "category": "Uncategorized",
    # "website": "https://github.com/OCA/<repo>" or "https://github.com/OCA/<repo>/tree/<branch>/<addon>",
    "author": "<JavierMarhuenda>, Odoo Community Association (OCA)",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    "maintainers": ["javiermarhuenda@gmail.com"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    # "preloadable": True,
    # "pre_init_hook": "pre_init_hook",
    # "post_init_hook": "post_init_hook",
    # "post_load": "post_load",
    # "uninstall_hook": "uninstall_hook",
    # "external_dependencies": {
       # "python": [],
       # "bin": [],
    # },
    "depends": [
        "base",
    ],
    "data": [
        "security/helpdesk_ticket_security.xml",
        "security/ir.model.access.csv",
        #"views/report_name.xml",
    ],
}