# -*- coding: utf-8 -*-
from random import randrange


def test_delete_some_contact(app):
    app.contact.check_for_test_contact()
    old_contacts = app.contact.get_list()
    index = randrange(len(old_contacts))
    app.contact.delete_some_contact(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
