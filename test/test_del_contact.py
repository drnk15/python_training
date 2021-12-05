# -*- coding: utf-8 -*-


def test_delete_first_contact(app):
    app.contact.check_for_test_contact()
    old_contacts = app.contact.get_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

