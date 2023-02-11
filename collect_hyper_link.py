from bs4 import BeautifulSoup

class collect_hyper_link:

    def __init__(self, document):
        self.soup = BeautifulSoup(document, 'html.parser')

    def find_all_links(self):
        return [(link.getText(), link.get('href')) for link in self.soup.find_all('a')]

    def get_all_paragraphs(self):
        return [paragraph.getText() for paragraph in self.soup.find_all(name='p')]
