import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://www.amazon.com/Acer-AN515-57-79TD-i7-11800H-GeForce-Keyboard/dp/B09R65RN43/?_encoding=UTF8&pd_rd_w=NcsY4&content-id=amzn1.sym.10f16e90-d621-4a53-9c61-544e5c741acc&pf_rd_p=10f16e90-d621-4a53-9c61-544e5c741acc&pf_rd_r=M51M3AA58QYMZ3MB58SP&pd_rd_wg=bJHw6&pd_rd_r=0df35619-481e-4b7c-b548-48727d9525e5&ref_=pd_gw_exports_top_sellers_unrec'

# 'what user agent am i using'


def get_link_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Accept-language': 'en',
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    name = soup.select_one(selector='#productTitle').getText()
    name = name.strip()

    price = soup.select_one(selector='.a-offscreen').getText()
    price = float(price[1:])

    data = {
        'name': name,
        'price': price
    }
    return data

print(get_link_data(url))