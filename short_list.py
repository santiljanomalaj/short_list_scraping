from bs4 import BeautifulSoup as soup
from random import randint
import requests
import re
import random
import time


def main():
  company_list_url = "https://www.sortlist.be/fr/s/illustrations/anvers-be"
  company_list_contents = requests.get(company_list_url)
  company_list_content = soup(company_list_contents.content, 'html.parser')
  company_lists = company_list_content.findAll('a',{'class':'md-truncate md-button md-sortlist-theme'})
  print(company_list_content)
main()