import logging
from urllib.request import urlopen
#import BeautifulSoup  # Specify url of the web page
import re

class BinarySearch:

    def __init__(self):
        pass

    def get_wikipedia_article(self, url):
        logging.debug("grabbing 1000 words from Wikipedia article")
        text = 'hello'
        # Specify url of the web page
        # source = urlopen(url).read()  # Make a soup
        # soup = BeautifulSoup(source, 'lxml')
        # # Extract the plain text content from paragraphs
        # for paragraph in soup.find_all('p'):
        #     text += paragraph.text
        # # Clean text
        # text = re.sub(r'\[.*?\]+', '', text)
        # text = text.replace('\n', '')
        return text

    def run(self):
        text = self.get_wikipedia_article('https://en.wikipedia.org/wiki/John_D._Hunter')
        logging.debug(text)

