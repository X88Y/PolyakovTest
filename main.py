# Created by Duxk
# time 18.17
# date 27.02.21
from bs4 import BeautifulSoup
import requests

url = input('kpolyakov Owned by Duxk: ')

source_code = requests.get(url)
source_code.encoding = 'utf-8'

html = BeautifulSoup(source_code.text, 'html.parser')
questions = html.find_all('div', {"class": "q"})

for i in questions:
    question = i.find('div', {"class": "label"}).string
    answers = i.find_all('tr')
    print(question)

    for i in answers:
        try: # string input protection
            is_right = i.find('input')['value']
            if is_right != '0':
                print(i.find('td', {'class': 'ans'}).string)
        except:
            pass
    print()
