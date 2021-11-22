# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.edit(Group(name="new_group_name", header="new_group_header", footer="new_group_footer"))
    app.group.return_to_groups_page()
    app.session.logout()
