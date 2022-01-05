# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test'))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="new_first_name", middlename="new_middle_name", lastname="new_name",
                      nickname="new_nickname", title="new_title", company="new_company", address="New street 27 302",
                      home_phone_number="+78885566", mobile_phone_number="+7265489621477",
                      work_phone_number="+445298477", fax_number="+449628977", email="new@mail.com",
                      email2="new2@mail.ru", email3="new3@mail.ru", homepage="webpage.com", birth_day="3",
                      birth_month="August", birth_year="1966", anniversary_day="28", anniversary_month="December",
                      anniversary_year="2003", address2="New lane 101 3", home_phone_number2="+754236999",
                      notes="some updated notes")
    contact.id = random.choice(old_contacts).id
    app.contact.edit_contact_by_id(contact)
    new_contacts = db.get_contact_list()
    old_contacts = [contact if c.id == contact.id else c for c in old_contacts]
    assert sorted(old_contacts, key=lambda c: c.id) == sorted(new_contacts, key=lambda c: c.id)
    if check_ui:
        assert sorted(new_contacts, key=lambda c: c.id) == sorted(app.contact.get_list(), key=lambda c: c.id)


def test_edit_some_contact_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test'))
    old_contacts = db.get_contact_list()
    contact_to_edit = random.choice(old_contacts)
    contact = Contact(lastname="zzzzlastname")
    contact.id = contact_to_edit.id
    contact.firstname = contact_to_edit.firstname
    app.contact.edit_contact_by_id(contact)
    new_contacts = db.get_contact_list()
    old_contacts = [contact if c.id == contact.id else c for c in old_contacts]
    assert sorted(old_contacts, key=lambda c: c.id) == sorted(new_contacts, key=lambda c: c.id)
    if check_ui:
        assert sorted(new_contacts, key=lambda c: c.id) == sorted(app.contact.get_list(), key=lambda c: c.id)
