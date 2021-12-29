# -*- coding: utf-8 -*-
from model.group import Group
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
