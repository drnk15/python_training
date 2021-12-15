# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import re


def trim_whitespace(s):
    s = re.sub(" +", " ", s)
    return s.strip()


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    r_str = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return trim_whitespace(r_str)


def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return months[random.randrange(len(months))]

#def random_day(self):
#    if self.
#


def random_phone(prefix, maxlen):
    symbols = string.digits + "-" + " " + "(" + ")"
    r_phone = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return trim_whitespace(r_phone)


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "_"*5 + "."*5 + "-"*5
    r_str1 = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    r_str2 = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    d_zone = "".join([random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3))])
    return prefix + r_str1 + "@" + r_str2 + "." + d_zone


testdata = [
    Contact(firstname=random_string("fn", 7), middlename=random_string("mn", 7), lastname=random_string("ln", 7),
            nickname=random_string("nn", 7), title=random_string("title", 5), company=random_string("company", 10),
            address=random_string("addr", 10), home_phone_number=random_phone("+1", 14),
            mobile_phone_number=random_phone("+2", 14), work_phone_number=random_phone("+3", 14),
            fax_number=random_phone("+5", 14), email=random_email("em1", 7), email2=random_email("em2", 7),
            email3=random_email("em3", 7), homepage=random_string("hp", 8), birth_day=str(random.randint(1, 31)),
            birth_month=random_month(), birth_year=str(random.randint(1900, 2015)),
            anniversary_day=str(random.randint(1, 31)), anniversary_month=random_month(),
            anniversary_year=str(random.randint(1906, 2021)), address2=random_string("addr2", 10),
            home_phone_number2=random_phone("+4", 14), notes=random_string("notes: ", 150))
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
