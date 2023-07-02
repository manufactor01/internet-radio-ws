import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup

from utils import process_url
from utils import process_name

class InternetRadioCrawler:

    def __init__(self, current_url):
        self.url = current_url
        req = requests.get(current_url)
        self.html = BeautifulSoup(req.text, "html.parser")

    def get_elements(self):
        entries = self.html.find('table', {'class': 'table table-striped'})
        return entries.find_all('tr')

    def get_stations(self):
        names = []
        urls = []

        elements = self.get_elements()

        for element in elements:
            sub_elements = element.find_all('td')
            title = process_name(sub_elements[2].find('h4').getText())
            names.append(title)

            links = sub_elements[1].find_all('a', href=True)
            url = process_url(links[1]['href'])
            urls.append(url)

        dicc = {
                'names': names,
                'urls': urls
                }

        return dicc

    def generate_csv(self, filename):
        dicc = self.get_stations()
        df = pd.DataFrame(dicc)
        df.to_csv(filename, index = False)
