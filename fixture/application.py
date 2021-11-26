from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.select = Select
        self.alert = Alert
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        # здесь если добавлять проверку по элементу страницы - то сначала нужно добавить проверку на логин
        # метод используется внутри метода login, если пользователь не авторизован - контент страницы другой
        # хедер везде одинаковый, но он также одинаковый и на других страницах, так что это неэффективно
        # мне кажется проверка на логин тут избыточной
        if not wd.current_url.endswith("/addressbook/"):
            wd.get("http://localhost/addressbook/")
