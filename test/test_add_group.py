# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string
import re


def trim_whitespace(s):
    s = re.sub(" +", " ", s)
    return s.strip()


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return trim_whitespace(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
