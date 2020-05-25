from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.go_to_login_page()# выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_register_login_form_and_link(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.should_be_register_form()
    page.should_be_login_url()


# pytest -v --tb=line --language=en test_main_page.py /
# В этой команде мы использовали опцию PyTest --tb=line, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста