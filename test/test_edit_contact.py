# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_by_id_contact(app):
    app.contact.check_for_test_contact()
    old_contacts = list(sorted(app.contact.get_list(), key=lambda c: c.id))
    contact = Contact(firstname="new_first_name", middlename="new_middle_name", lastname="new_name",
                      nickname="new_nickname", title="new_title", company="new_company", address="New street 27 302",
                      home_phone_number="+78885566", mobile_phone_number="+7265489621477",
                      work_phone_number="+445298477", fax_number="+449628977", email="new@mail.com",
                      email2="new2@mail.ru", email3="new3@mail.ru", homepage="webpage.com", birth_day="3",
                      birth_month="August", birth_year="1966", anniversary_day="28", anniversary_month="December",
                      anniversary_year="2003", address2="New lane 101 3", home_phone_number2="+754236999",
                      notes="some updated notes")
    contact.id = old_contacts[0].id
    app.contact.edit_contact_selected_by_id(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = list(sorted(app.contact.get_list(), key=lambda c: c.id))
    old_contacts[0] = contact
    assert old_contacts == new_contacts


def test_edit_first_contact_lastname(app):
    app.contact.check_for_test_contact()
    old_contacts = list(sorted(app.contact.get_list(), key=lambda c: c.id))
    contact = Contact(lastname="zzzzlastname")
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname
    app.contact.edit_contact_selected_by_id(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = list(sorted(app.contact.get_list(), key=lambda c: c.id))
    old_contacts[0] = contact
    assert old_contacts == new_contacts
