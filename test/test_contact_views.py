import re
from random import randint


def test_contact_on_homepage(app):
    app.contact.check_for_test_contact()
    index = randint(0, (app.contact.count()-1))
    contact_from_homepage = app.contact.get_list()[index]
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert clear_newlines(contact_from_homepage.all_emails) == contact_from_edit_page.all_emails
    assert clear_newlines(contact_from_homepage.all_phones) == clear_phones(contact_from_edit_page.all_phones)


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
