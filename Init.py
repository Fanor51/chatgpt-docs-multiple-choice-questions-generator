#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import os, logging, sys
import time

from dotenv import load_dotenv
from Crawler import Crawler
from ChatGPT import ChatGPT

load_dotenv()

start_time = time.time()
print('Start Crawler')
crawler = Crawler("https://docs.typo3.org/m/typo3/reference-coreapi/11.5/en-us/ApiOverview/DependencyInjection/Index.html", "DependencyInjection")

content = crawler.get_content_from_api()
print('Save Content in file')
crawler.save_content(content)

print('Get Content from file')
content = crawler.get_content()

print('Start ChatGPT')
chatgpt = ChatGPT(content)
ChatGPT.create_questions(chatgpt,'DependencyInjection')

end_time = time.time()
print("END | Time elapsed: " + str(end_time - start_time) + " seconds")
