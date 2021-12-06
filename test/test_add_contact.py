# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_list()
    contact = Contact(firstname="first_name", middlename="middle_name", lastname="last_name", nickname="nickname",
                title="title", company="company", address="Any street 26 49", home_phone_number="+78885544",
                mobile_phone_number="+7265489621466", work_phone_number="+445298466", fax_number="+449628963",
                email="mail@mail.io", email2="mail2@mail.com", email3="mail3@mail.ru", homepage="homepage.com",
                birth_day="2", birth_month="July", birth_year="1955", anniversary_day="14",
                anniversary_month="November", anniversary_year="2002", address2="Other street 15 36",
                home_phone_number2="+754236986", notes="notes notes notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
