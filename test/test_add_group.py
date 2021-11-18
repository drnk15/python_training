# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="test_group_name", header="test_group_header", footer="test_group_footer"))
    app.group.return_to_groups_page()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_groups_page()
    app.session.logout()
