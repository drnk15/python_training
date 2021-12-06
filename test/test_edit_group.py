# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_some_group_full(app):
    app.group.check_for_test_group()
    old_groups = app.group.get_list()
    index = randrange(len(old_groups))
    group = Group(name="new_group_name", header="new_group_header", footer="new_group_footer")
    group.id = old_groups[index].id
    app.group.edit_some_group(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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
