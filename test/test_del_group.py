# -*- coding: utf-8 -*-
from random import randrange


def test_delete_some_group(app):
    app.group.check_for_test_group()
    old_groups = app.group.get_list()
    index = randrange(len(old_groups))
    app.group.delete_some_group(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
