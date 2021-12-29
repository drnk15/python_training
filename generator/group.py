# -*- coding: utf-8 -*-
from model.group import Group
import random
import string
import re
import json
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number_of_groups", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def trim_whitespace(s):
    s = re.sub(" +", " ", s)
    return s.strip()


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return trim_whitespace(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))


testdata = [Group(name=random_string("name", 10), header=random_string("header", 20),
    footer=random_string("footer", 20))
    for i in range(n)
]


other_testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
