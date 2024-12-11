import os
import unittest
import requests
from main import find_links


file_path = os.path.join(os.getcwd(), "pr.html")

class TestLinkFinder(unittest.TestCase):
    def test_localfile(self):
        a=[]
        with open(file_path, encoding='utf-8') as f:
            html = f.read()
            links = find_links(html)
            if links:
                for link in links:
                    a.append(link)
        self.assertEqual(2,len(a),"Неверное количество ссылок")
        
    def test_url(self):
        url="https://example.com/"
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            links = find_links(html)
            if links:
                for link in links:
                    a=link
        self.assertEqual("https://www.iana.org/domains/example",a,"Неверная ссылка")