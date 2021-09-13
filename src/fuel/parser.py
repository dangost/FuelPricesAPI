import requests
from bs4 import BeautifulSoup


def parse_fuel():
    proxy = {"http": "96.9.74.91:8080"}
    html = requests.get(
        "https://azs.belorusneft.by/sitebeloil/ru/center/azs/center/fuelandService/price",
        proxies=proxy
    ).text

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find_all("div", {"class": "b-left__informer_top"})
    table = table[0].parent.contents[4].contents

    ai92 = table[2].contents[0].contents[0]
    ai95 = table[2].contents[1].contents[0]

    ai98 = table[4].contents[0].contents[0]
    gas = table[4].contents[1].contents[0]

    dt = table[6].contents[0].contents[0]

    return ai92, ai95, ai98, gas, dt
