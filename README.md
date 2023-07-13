# [POC] chatgpt-docs-multiple-choice-questions-generator
Python 3 Scripts for generating multiple choice questions from code docs websites.

## Future Idea
The main idea for this project was to create educational data from crawling docs websites like https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/ApiOverview/Index.html and create randomized multiple choice quizes to learn for a certificate.

## Known issues
- Some content from pages are to long to send to chatGPT api and need to get splitted into multiple parts. Because every prompt stands for itself it is possible that context from the whole page gets lost in the questions.
- 

## Open Tasks
- Crawl a page tree / multiple pages and not only 1 Page
- Check and maybe optimize incoming data structure
- Maybe import data directly into a DB?
- Optimize code
- ... 

## Python Packages

- pip3 install {package}

````
> pip list
Package            Version
------------------ --------
aiohttp            3.8.4
aiosignal          1.3.1
async-timeout      4.0.2
attrs              23.1.0
beautifulsoup4     4.12.2
certifi            2023.5.7
charset-normalizer 3.1.0
frozenlist         1.3.3
idna               3.4
multidict          6.0.4
openai             0.27.6
pip                23.1.2
python-dotenv      1.0.0
requests           2.30.0
setuptools         67.7.2
soupsieve          2.4.1
tqdm               4.65.0
urllib3            2.0.2
wheel              0.37.1
yarl               1.9.2

````

## Run Programm

`` python3 Init.py ``


