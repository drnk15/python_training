# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    app.contact.check_for_test_contact()
    old_contacts = app.contact.get_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="new_first_name", middlename="new_middle_name", lastname="new_name",
                      nickname="new_nickname", title="new_title", company="new_company", address="New street 27 302",
                      home_phone_number="+78885566", mobile_phone_number="+7265489621477",
                      work_phone_number="+445298477", fax_number="+449628977", email="new@mail.com",
                      email2="new2@mail.ru", email3="new3@mail.ru", homepage="webpage.com", birth_day="3",
                      birth_month="August", birth_year="1966", anniversary_day="28", anniversary_month="December",
                      anniversary_year="2003", address2="New lane 101 3", home_phone_number2="+754236999",
                      notes="some updated notes")
    contact.id = old_contacts[index].id
    app.contact.edit_some_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=lambda c: c.id) == sorted(new_contacts, key=lambda c: c.id)


def test_edit_some_contact_lastname(app):
    app.contact.check_for_test_contact()
    old_contacts = app.contact.get_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="zzzzlastname")
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    app.contact.edit_some_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=lambda c: c.id) == sorted(new_contacts, key=lambda c: c.id)
