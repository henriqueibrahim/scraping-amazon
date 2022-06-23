import json
import mysql.connector
import os
import requests
from dotenv import load_dotenv
from selectorlib import Extractor
from time import sleep

# Carregando as variáveis do SQL.
load_dotenv()

sqlUser = os.getenv("USER")
sqlPassword = os.getenv("PASSWORD")
sqlDatabase = os.getenv("DATABASE")


# Cria um Extractor lendo do arquivo YAML.
e = Extractor.from_yaml_file('search.yml')


def scrape(url):  

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    print(f"Downloading {url}")
    r = requests.get(url, headers=headers)

    # Verificação simples para ver se a página foi bloqueada.
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print(f"Page {url} was blocked by Amazon.\n")
        else:
            print(f"Page {url} must have been blocked by Amazon.The status code is: {r.status_code}")
        return None
    return e.extract(r.text)


# Conectar no MySQL.
cnx = mysql.connector.connect(user=sqlUser, password=sqlPassword, database=sqlDatabase)
cursor = cnx.cursor()

with open("search_urls.txt", "r") as urllist:
    for url in urllist.read().splitlines():
        data = scrape(url)
        if data:
            for product in data["products"]:
                product["search_url"] = url

                sqlTitle = product.get("title")
                sqlPrice = product.get("price")

                add_product = ("INSERT IGNORE INTO Data (title, price)"
                               "VALUES (%s, %s)")

                data_product = (f"{sqlTitle}", f"{sqlPrice}")
                
                cursor.execute(add_product, data_product)
                print(f"Saving to MySQL: {product['title']}")
cnx.commit()
cursor.close()
cnx.close()
