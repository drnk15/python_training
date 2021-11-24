# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="new_first_name", middlename="new_middle_name", lastname="new_last_name",
                                           nickname="new_nickname", title="new_title", company="new_company",
                                           address="New street 27 302", home_phone_number="+78885566",
                                           mobile_phone_number="+7265489621477", work_phone_number="+445298477",
                                           fax_number="+449628977", email="new@mail.com", email2="new2@mail.ru",
                                           email3="new3@mail.ru", homepage="webpage.com", birth_day="3", birth_month="August",
                                           birth_year="1966", anniversary_day="28", anniversary_month="December",
                                           anniversary_year="2003", address2="New lane 101 3", home_phone_number2="+754236999",
                                           notes="some updated notes"))
    app.session.logout()
