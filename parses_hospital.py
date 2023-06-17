from bs4 import BeautifulSoup
import requests
from config import *

def parse_doctors(n):
    url = ""
    if n == 1:
        url = doctor1_url
    if n == 2:
        url = doctor2_url
    if n == 3:
        url = doctor3_url
    if n == 4:
        url = doctor3_url
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "lxml")
    info = ""
    block1 = soup.findAll('div', class_='doctor-name')
    block2 = soup.findAll('div', class_='field-item even')
    if len(block1) < 13:
        for i in range(len(block1)):
            info += block1[i].text
            info += "\n"
            info += block2[i].text
            info += "\n\n"
        return info
    else:
        for i in range(13):
            info += block1[i].text
            info += "\n"
            info += block2[i].text
            info += "\n\n"
        return info

def parse_services(n):
    url = ""
    if n == 1:
        url = service1_url
    if n == 2:
        url = service2_url
    if n == 3:
        url = service3_url
    if n == 4:
        url = service4_url
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "lxml")
    info = ""
    block1 = soup.findAll('td', class_='service-title')
    block2 = soup.findAll('td', class_='service-price')
    if len(block2) > 10:
        for i in range(10):
            info += block1[i].text + '\n'
            info += " Цена:"+block2[i].text
            info += "\n\n"
        return info
    else:
        for i in range(len(block2)):
            info += block1[i].text + '\n'
            info += " Цена:"+block2[i].text
            info += "\n\n"
        return info