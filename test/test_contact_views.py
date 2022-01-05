import re
from random import randint
from model.contact import Contact


def test_contacts_on_homepage_match_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test'))
    contacts_from_homepage = sorted(app.contact.get_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list_with_phones_and_emails(), key=Contact.id_or_max)
    assert contacts_from_homepage == contacts_from_db
    # свойства, не прописанные в функции сравнения, сравниваются отдельными списками:
    addresses_from_homepage = [c.address for c in contacts_from_homepage]
    addresses_from_db = [c.address for c in contacts_from_db]
    assert addresses_from_homepage == addresses_from_db
    emails_from_homepage = [clear_newlines(c.all_emails) for c in contacts_from_homepage]
    emails_from_db = [c.all_emails for c in contacts_from_db]
    assert emails_from_homepage == emails_from_db
    phones_from_homepage = [clear_phones(c.all_phones) for c in contacts_from_homepage]
    phones_from_db = [clear_phones(c.all_phones) for c in contacts_from_db]
    assert phones_from_homepage == phones_from_db


#def test_contact_on_detail_page(app):
#    contact_from_details = app.contact.get_info_from_detail_page(0)
#    contact_from_edit_page = app.contact.get_info_from_edit_page(0)
#    assert contact_from_details.lastname == contact_from_edit_page.lastname
#    assert contact_from_details.firstname == contact_from_edit_page.firstname
#    assert contact_from_details.address == contact_from_edit_page.address
#    assert contact_from_details.email == contact_from_edit_page.email
#    assert contact_from_details.email2 == contact_from_edit_page.email2
#    assert contact_from_details.email3 == contact_from_edit_page.email3
#    assert contact_from_details.home_phone_number == contact_from_edit_page.home_phone_number
#    assert contact_from_details.mobile_phone_number == contact_from_edit_page.mobile_phone_number
#    assert contact_from_details.work_phone_number == contact_from_edit_page.work_phone_number
#    assert contact_from_details.home_phone_number2 == contact_from_edit_page.home_phone_number2


def clear_phones(s):
    return re.sub("[- ()\n]", "", s)

def clear_newlines(s):
    return re.sub("\n", "", s)
