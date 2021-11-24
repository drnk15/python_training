# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_full(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="new_group_name", header="new_group_header", footer="new_group_footer"))
    app.session.logout()


def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="new_group_name"))
    app.session.logout()


def test_edit_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="new_group_header"))
    app.session.logout()


def test_edit_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(footer="new_group_footer"))
    app.session.logout()
