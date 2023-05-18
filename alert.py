import requests
import time
from bs4 import BeautifulSoup

url = 'https://www.community-boating.org/'
response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, 'html.parser')

flag_element = soup.find('span', id="flag-text-sm")

initial_flag = flag_element.text.strip()

while True:
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    if initial_flag != None:
        updated_flag_element = soup.find('span', id="flag-text-sm")

        updated_flag = updated_flag_element.text.strip()

    if updated_flag != initial_flag:
        if updated_flag == 'Red Flag':
            print('Red flag')
        elif updated_flag == 'Yellow Flag':
            print('Yellow flag')
        else:
            print('Green flag')
        
        initial_flag = updated_flag
    
    time.sleep(60)