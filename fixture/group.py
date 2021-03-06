from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not self.group_page_is_open():
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def group_page_is_open(self):
        wd = self.app.wd
        return wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0

    group_cache = None

    def get_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                group_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=group_id))
        return list(self.group_cache)

    def select_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_css_selector(f"input[value='{id}']").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def check_for_test_group(self):
        # ensure that at list 1 group exists
        self.open_groups_page()
        if self.count() == 0:
            self.create(Group(name="test"))

    def update_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def fill_group_form(self, group):
        # fill group name
        self.update_field_value("group_name", group.name)
        # fill group header
        self.update_field_value("group_header", group.header)
        # fill group footer
        self.update_field_value("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_some_group(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        # init group modification
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # update group modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_id(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group modification
        self.select_group_by_id(group.id)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # update group modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_some_group(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None
