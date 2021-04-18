class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        print("BasePage")
    def open(self):
        self.browser.get(self.url)
        print("open")

class BaseBasePageBaseBase(BasePage):
    print("BaseBasePageBaseBase")

class BaseBasePageBase(BaseBasePageBaseBase):
    super().__init__()

class BaseBasePage(BaseBasePageBase):
    print("BaseBasePage")

class MainMainPage(BaseBasePage):
      print("MainMainPage")


a = MainMainPage()