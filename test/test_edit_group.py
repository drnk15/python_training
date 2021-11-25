# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_full(app):
    app.group.edit_first_group(Group(name="new_group_name", header="new_group_header", footer="new_group_footer"))


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="new_group_name"))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="new_group_header"))


def test_edit_first_group_footer(app):
    app.group.edit_first_group(Group(footer="new_group_footer"))
