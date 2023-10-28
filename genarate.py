import random
import string
import time

import requests
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
# options = webdriver.ChromeOptions()
# service = ChromeService(executable_path='D:\chromedriver-win32\chromedriver')
# driver = webdriver.Chrome(service=service, options=options)

options = webdriver.FirefoxOptions()
service = Service(executable_path='D:\geckodriver')
driver = webdriver.Firefox(service=service, options=options)

# form_url = "http://over.org.tilda.ws/testuser"
# driver.get(form_url)

# form_url = "https://rem-service.by/"
# driver.get(form_url)

# form_url = "https://remontstiralka.by"
# driver.get(form_url)
#не работает

# form_url = "https://www.xn--e1aascffjcqga1b9h.xn--90ais/remont-stiralnyh-mashin-v-minske"
# driver.get(form_url)

# form_url = "https://sm-service.by/price"
# driver.get(form_url)

while True:
    form_url = input('Введите ссылку: ')
    if form_url == 0:
        break
    else:
        driver.get(str(form_url))

        time.sleep(3)

        from bs4 import BeautifulSoup

        response = requests.get(form_url)
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')

        input_elements = soup.find_all('input')

        names_list = ['Иван', 'Мария', 'Алексей', 'Екатерина', 'Андрей', 'Максим', 'Егор', 'Анна', 'Валера', 'Ирина', 'Владислав', 'Полина']
        random_name = random.choice(names_list)

        def generate_email():
            letters = string.ascii_lowercase
            username = ''.join(random.choice(letters) for _ in range(8))
            domain = random.choice(['gmail.com', 'mail.ru', 'list.ru', 'yandex.ru'])
            email = f"{username}@{domain}"
            return email

        random_email = generate_email()

        def generate_phone():
            numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            base_phone = ''.join(str(random.choice(numbers)) for _ in range(8))
            code = random.choice(['29', '33', '44', '25'])
            phone = f"{code}{base_phone}"
            return phone

        random_phone = generate_phone()


        for input_tag in input_elements[:6]:
            if input_tag.get('type') == 'text':
                if input_tag.get('name') == 'tel' or input_tag.get('name') == 'phone' or input_tag.get('name') == 'Phone':
                    input_text_phone = input_tag.get('name')
                    input_field_phone = driver.find_element(By.NAME, input_text_phone)
                    input_field_phone.send_keys(random_phone)
                elif input_tag.get('name') == 'email' or input_tag.get('name') == 'Email':
                    input_text_email = input_tag.get('name')
                    input_field_email = driver.find_element(By.NAME, input_text_email)
                    input_field_email.send_keys(random_email)
                else:
                    input_name = input_tag.get('name')
                    input_field_name = driver.find_element(By.NAME, input_name)
                    input_field_name.send_keys(random_name)
            elif input_tag.get('type') == 'email':
                if input_tag.get('id'):
                    input_id_email = input_tag.get('id')
                    input_field_email = driver.find_element(By.ID, input_id_email)
                    input_field_email.send_keys(random_email)
                else:
                    input_name_email = input_tag.get('name')
                    input_field_email = driver.find_element(By.NAME, input_name_email)
                    input_field_email.send_keys(random_email)
            elif input_tag.get('type') == 'tel':
                if input_tag.get('id'):
                    input_phone = input_tag.get('id')
                    input_field_phone = driver.find_element(By.ID, input_phone)
                    input_field_phone.send_keys(random_phone)
                elif input_tag.get('name'):
                    input_phone = input_tag.get('name')
                    input_field_phone = driver.find_element(By.NAME, input_phone)
                    input_field_phone.send_keys(random_phone)

