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

    def get_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        raw_list = wd.find_elements_by_xpath("//tr[@name='entry']")
        contacts_list = []
        for element in raw_list:
            contact_id = element.find_element_by_name("selected[]").get_attribute("id")
            firstname = element.find_element_by_xpath("./td[3]").text
            lastname = element.find_element_by_xpath("./td[2]").text
            contacts_list.append(Contact(id=contact_id, firstname=firstname, lastname=lastname))
        return contacts_list

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

    def edit_contact_selected_by_id(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact modification
        wd.find_element_by_css_selector(f'[href="edit.php?id={contact.id}"]').click()
        self.fill_contact_form(contact)
        # update contact modification
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def delete_first_contact(self):
        wd = self.app.wd
        alert = self.app.alert
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # click delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        alert(wd).accept()
        # wait until deletion complete
        wd.find_element_by_css_selector("div.msgbox")
