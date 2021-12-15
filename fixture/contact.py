from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("address")) > 0):
            wd.find_element_by_link_text("add new").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_contact_for_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        entry = wd.find_elements_by_name("entry")[index]
        entry.find_element_by_css_selector('img[title="Edit"]').click()

    def open_contact_details_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        entry = wd.find_elements_by_name("entry")[index]
        entry.find_element_by_css_selector('img[title="Details"]').click()

    def get_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_for_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        all_emails = "".join([email, email2, email3])
        home_phone_number = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone_number = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone_number = wd.find_element_by_name("work").get_attribute("value")
        home_phone_number2 = wd.find_element_by_name("phone2").get_attribute("value")
        all_phones = "".join([home_phone_number, mobile_phone_number, work_phone_number, home_phone_number2])
        return Contact(id=id, lastname=lastname, firstname=firstname, address=address, email=email, email2=email2,
                    email3=email3, home_phone_number=home_phone_number, mobile_phone_number=mobile_phone_number,
                    work_phone_number=work_phone_number, home_phone_number2=home_phone_number2, all_emails=all_emails,
                    all_phones=all_phones)

    #def get_info_from_detail_page(self, index):
    #    wd = self.app.wd
    #    self.open_contact_details_by_index(index)
    #    text = wd.find_element_by_id("content").text
    #
    #    home_phone_number = re.search("H: (.*)", text).group(1)
    #    mobile_phone_number = re.search("M: (.*)", text).group(1)
    #    work_phone_number = re.search("W: (.*)", text).group(1)
    #    home_phone_number2 = re.search("P: (.*)", text).group(1)
    #    return Contact(
    #        id=id, lastname=lastname, firstname=firstname, address=address, email=email, email2=email2,
    #        email3=email3, home_phone_number=home_phone_number, mobile_phone_number=mobile_phone_number,
    #        work_phone_number=work_phone_number, home_phone_number2=home_phone_number2
    #    )

    contact_cache = None

    def get_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                contact_id = element.find_element_by_name("selected[]").get_attribute("id")
                firstname = element.find_element_by_xpath("./td[3]").text
                lastname = element.find_element_by_xpath("./td[2]").text
                address = element.find_element_by_xpath("./td[4]").text
                all_emails = element.find_element_by_xpath("./td[5]").text
                all_phones = element.find_element_by_xpath("./td[6]").text
                self.contact_cache.append(
                    Contact(id=contact_id, firstname=firstname, lastname=lastname, address=address,
                            all_emails=all_emails, all_phones=all_phones)
                    )
        return list(self.contact_cache)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def check_for_test_contact(self):
        self.app.open_home_page()
        if self.count() == 0:
            self.create(Contact(firstname="for test"))

    def update_select_field_value(self, field_name, value):
        wd = self.app.wd
        select = self.app.select
        if value is not None:
            wd.find_element_by_name(field_name).click()
            select(wd.find_element_by_name(field_name)).select_by_visible_text(value)

    def update_input_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        select = self.app.select
        self.update_input_field_value("firstname", contact.firstname)
        self.update_input_field_value("middlename", contact.middlename)
        self.update_input_field_value("lastname", contact.lastname)
        self.update_input_field_value("nickname", contact.nickname)
        self.update_input_field_value("title", contact.title)
        self.update_input_field_value("company", contact.company)
        self.update_input_field_value("address", contact.address)
        self.update_input_field_value("home", contact.home_phone_number)
        self.update_input_field_value("mobile", contact.mobile_phone_number)
        self.update_input_field_value("work", contact.work_phone_number)
        self.update_input_field_value("fax", contact.fax_number)
        self.update_input_field_value("email", contact.email)
        self.update_input_field_value("email2", contact.email2)
        self.update_input_field_value("email3", contact.email3)
        self.update_input_field_value("homepage", contact.homepage)
        self.update_select_field_value("bday", contact.birth_day)
        self.update_select_field_value("bmonth", contact.birth_month)
        self.update_input_field_value("byear", contact.birth_year)
        self.update_select_field_value("aday", contact.anniversary_day)
        self.update_select_field_value("amonth", contact.anniversary_month)
        self.update_input_field_value("ayear", contact.anniversary_year)
        self.update_input_field_value("address2", contact.address2)
        self.update_input_field_value("phone2", contact.home_phone_number2)
        self.update_input_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        # submit creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def edit_some_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact modification
        wd.find_element_by_css_selector(f'[href="edit.php?id={contact.id}"]').click()
        self.fill_contact_form(contact)
        # update contact modification
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_some_contact(self, index):
        wd = self.app.wd
        alert = self.app.alert
        self.app.open_home_page()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # click delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        alert(wd).accept()
        # wait until deletion complete
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_some_contact(0)
