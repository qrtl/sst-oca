# Copyright 2021 Pierre Verkest <pierreverkest84@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, tools

class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    @tools.ormcache('self.env.uid', 'group_ext_id')
    def has_group(self, group_ext_id):
        """While ensuring a user is part of `base.group_user` this code will
        try if user is in the `base_group_backend.group_backend` group to let access
        to the odoo backend.
        This code avoids overwriting a lot of places in controllers from
        different modules ('portal', 'web', 'base') with hardcoded statements
        that check if user is part of `base.group_user` group.
        As `base.group_user` has a lot of default permissions, this
        makes it hard to maintain proper access rights according to your business.
        """
        res = super(ResUsers, self).has_group(group_ext_id)
        if not res and (group_ext_id == "base.group_user"):
            has_base_group_backend = super(ResUsers, self).has_group(
                "base_group_backend.group_backend"
            )
            return has_base_group_backend
        return res

    @api.depends('groups_id')
    def _compute_share(self):
        for user in self:
            user.share = not (user.has_group('base.group_user') or user.has_group('base_group_backend.group_backend'))
