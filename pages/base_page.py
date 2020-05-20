#from selenium.webdriver import Remote as RemoteWebDriver
class BasePage(object):
    def __init__(self, browser, url):
        """Конструктор класса.
               :param browser:
               :param url:
        """
        self.browser = browser
        self.url = url

    def open(self):
        """метод открывает нужную страницу,
                используя метод get()
        """
        self.browser.get(self.url)



