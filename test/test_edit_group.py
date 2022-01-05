# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_some_group_full(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    group = Group(name="new_group_name", header="new_group_header", footer="new_group_footer")
    group.id = random.choice(old_groups).id
    app.group.edit_group_by_id(group)
    new_groups = db.get_group_list()
    old_groups = [group if g.id == group.id else g for g in old_groups]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)


#def test_edit_first_group_name(app):
#    app.group.check_for_test_group()
#    old_groups = app.group.get_list()
#    group = Group(name="other_group_name")
#    group.id = old_groups[0].id
#    app.group.edit_first_group(group)
#    assert len(old_groups) == app.group.count()
#    new_groups = app.group.get_list()
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
#
#def test_edit_first_group_header(app):
#    app.group.check_for_test_group()
#    old_groups = app.group.get_list()
#    app.group.edit_first_group(Group(header="other_group_header"))
#    assert len(old_groups) == app.group.count()
#
#
#def test_edit_first_group_footer(app):
#    app.group.check_for_test_group()
#    old_groups = app.group.get_list()
#    app.group.edit_first_group(Group(footer="other_group_footer"))
#    assert len(old_groups) == app.group.count()
