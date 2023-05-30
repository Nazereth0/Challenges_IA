import requests
from bs4 import BeautifulSoup
import json
import re

def create_json():
    base_url = "https://www.root-me.org/?page=news&lang=fr&debut_chat_box_archive={}&var_ajax=1&var_ajax_env=glcVU8AE57GEnXXITfgldAuG66Pro7n3xt498bYo%2BcqVmhCctNVs1LjEt%2Fi5RLc6xwu0VKIllWwHhXJ2nuVplCZdNGEuvHi0JpyvNz9DuR%2Bl%2Bwusf8Zw8TlC%2BnfVIHnQS6AVQsdwMbeu%2F5WRxE%2BKJ%2FJ4Xh9AO5ek2uaoss%2B5wIeA%2FmdfZs24B2c2QoMkwigaXZ45VAPD0CSB884hQZ16dRB2C8t%2BiiNjFkBm0Q%3D%3D&var_ajax_ancre=pagination_chat_box_archive&var_t=1685265188663"

    start_index = 1
    messages = []
    message_id = 1

    while len(messages) < 48:
        url = base_url.format(start_index)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        chatbox = soup.find('ul', class_='chatbox')
        messages_list = chatbox.find_all('li')

        for message_item in messages_list:
            author_element = message_item.find('img', class_=re.compile("vmiddle .*"))
            author = author_element.get('alt') if author_element else "N/A"
            date = message_item.find('i').text.replace('\xa0', ' ')
            message = message_item.find('div', class_='chatbox').text.strip().replace('\xa0', ' ')

            message_info = {
                'id': message_id,
                'pseudo': author,
                'date': date,
                'message': message
            }

            messages.append(message_info)
            print(message_info)
            message_id += 1

        start_index += 3

    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(messages, json_file, ensure_ascii=False, indent=4)

create_json()
