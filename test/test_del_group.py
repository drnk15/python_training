# -*- coding: utf-8 -*-


def test_delete_first_group(app):
    app.group.check_for_test_group()
    old_groups = app.group.get_list()
    app.group.delete_first_group()
    new_groups = app.group.get_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
