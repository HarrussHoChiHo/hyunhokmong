from selenium import webdriver
from selenium.webdriver.chrome import service, options
class scrap_page:

    def __init__(self, start_link):
        self.start_link = start_link
        self.service = service.Service("./chromedriver");
        self.options = options.Options()
        self.options.add_argument("--disable-notifications")
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.chrome = webdriver.Chrom(service=service, options=options)

    def open_with_start_link(self):
        self.chrome.get(self.start_link)

    def get_page_source(self):
        return self.chrome.page_source