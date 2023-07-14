#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import requests
import re
import os

from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, url, name, folder):
        self.url = url
        self.name = name
        self.folder = folder

    def get_content_from_api(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find('div', {'class': 'document'})
        if not content:
            content = soup.find('div')
        if content:
            return content.get_text()
        else:
            return None

    def save_content(self, content):
        # Entferne alle doppelten Zeilenumbrüche
        text = re.sub(r'\n\s*\n', '\n\n', content)

        # Entferne alle zusätzlichen Leerzeichen am Anfang und am Ende jeder Zeile
        text = "\n".join([line.strip() for line in text.split("\n")])

        # Entferne alle Zeilenumbrüche am Anfang und am Ende des Textes
        text = text.strip()
        
        # Check if the directory exists
        if not os.path.exists(self.get_path()):
            # If it doesn't exist, create it
            os.makedirs(self.get_path())

        with open(self.get_path() + self.name + '.text', 'w') as outfile:
            outfile.write(text)
            outfile.close()

    def get_content(self):
        with open(self.get_path() + self.name + '.text', 'r') as file:
            content = file.read()
            file.close()
            return content
        
    def get_path(self):
        path = 'Content'
        if self.folder:
            path = path + '/' + self.folder
        
        return path + '/'