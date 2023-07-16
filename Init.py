#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import os
import time

from dotenv import load_dotenv
from Classes.Service.Crawler import Crawler
from Classes.Service.ChatGPT import ChatGPT
from Classes.Service.SitemapLoader import SitemapLoader

load_dotenv()

print("SETUP\n")
print("SITEMAP_JSON_FILE_NAME: " + os.getenv('SITEMAP_JSON_FILE_NAME'))
print("MODEL_TO_USE: " + os.getenv('MODEL_TO_USE'))
print("AMOUNT_OF_QUESTIONS_PER_PROMPT: " + os.getenv('AMOUNT_OF_QUESTIONS_PER_PROMPT'))
print("TEXT_THRESHOLD: " + os.getenv('TEXT_THRESHOLD'))
print()

start_time = time.time()
print("Load Sitemap")
sitemapJson = SitemapLoader(os.getenv('SITEMAP_JSON_FILE_NAME')).load_sitemap()
print("Successfully loaded sitemap for: " + sitemapJson['page'] + " with " + str(len(sitemapJson['pageSiteMap'])) + " urls\n\n")

for each in sitemapJson['pageSiteMap'] :
    folder = sitemapJson['folder']
    if 'folder' in each.keys() :
        folder += '/' + each['folder']

    print('Start Crawling for Page: ' + each['name'])
    crawler = Crawler(each['url'], each['name'], folder)
    content = crawler.get_content_from_api()

    print('Save Content in file')
    crawler.save_content(content)

    print('Get Content from file')
    content = crawler.get_content()


    print('Start ChatGPT\n')
    print('__________________________')
    chatgpt = ChatGPT(content, each['name'], folder)
    ChatGPT.create_questions(chatgpt, int(os.getenv('AMOUNT_OF_QUESTIONS_PER_PROMPT')))
    print('')
    print('Finished ChatGPT - Start next Page')
    print('==========================\n\n')

end_time = time.time()
print("END | Time elapsed: " + str(end_time - start_time) + " seconds")