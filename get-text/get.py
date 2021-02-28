from bs4 import BeautifulSoup
import requests

url = 'https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}'
target_url = url.format(1)
print(target_url)

r = requests.get(target_url)
soup = BeautifulSoup(r.text,'html.parser')

contents = soup.find_all('div', class_='cassetteitem')

content = contents[0]

detail = content.find('div', class_='cassetteitem-detail')

table = content.find('table', class_='cassetteitem_other')


title = detail.find('div', class_='cassetteitem_content-title').text

address = detail.find('li', class_='cassetteitem_detail-col1').text

access = detail.find('li', class_='cassetteitem_detail-col2').text

age = detail.find('li', class_='cassetteitem_detail-col3').text

tr_tags = table.find_all('tr', class_='js-cassette_link')

tr_tag: object = tr_tags[0]

floor, price, first_fee, capacity = tr_tag.find_all('td')[2:6]

fee, management_fee = price.find_all('li')

deposit, gratuity = first_fee.find_all('li')

madori, menseki = capacity.find_all('li')

d = {
    'title': title,
    'adress': address,
    'access': access,
    'age': age,
    'floor': floor.text,
    'fee': fee.text,
    'management_fee': management_fee.text,
    'deposit': deposit.text,
    'gratuity': gratuity.text,
    'madori': madori.text,
    'menseki': menseki.text
}


d_list = []

contents = soup.find_all('div', class_='cassetteitem')

for content in contents:
    detail = content.find('div', class_='cassetteitem-detail')
    table = content.find('table', class_='cassetteitem_other')
    title = detail.find('div', class_='cassetteitem_content-title').text
    address = detail.find('li', class_='cassetteitem_detail-col1').text
    access = detail.find('li', class_='cassetteitem_detail-col2').text
    age = detail.find('li', class_='cassetteitem_detail-col3').text
    tr_tags = table.find_all('tr', class_='js-cassette_link')

    for tr_tag in tr_tags:
        floor, price, first_fee, capacity = tr_tag.find_all('td')[2:6]
        fee, management_fee = price.find_all('li')
        deposit, gratuity = first_fee.find_all('li')
        madori, menseki = capacity.find_all('li')


        d = {
            'title': title,
            'adress': address,
            'access': access,
            'age': age,
            'floor': floor.text,
            'fee': fee.text,
            'management_fee': management_fee.text,
            'deposit': deposit.text,
            'gratuity': gratuity.text,
            'madori': madori.text,
            'menseki': menseki.text
        }

        d_list.append(d)

from pprint import pprint

pprint(d_list[0])
print()
pprint(d_list[4])
