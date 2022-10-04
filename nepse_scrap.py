import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

import sys
sys.setrecursionlimit(10000)

contact = []
stock_symbol = []
buyer_broker = []
seller_broker = []
quantity = []
rate = []
amount = []


def scrap_data(index):
    datas = []
    try:
        soup = BeautifulSoup(
            urllib.request.urlopen(
                "http://www.nepalstock.com/main/floorsheet/index/"
                + str(index)
                + "/?contract-no=&stock-symbol=&buyer=&seller="
            ).read(),
            "lxml",
        )
        total_index = soup("div", {"class": "pager"})[0].find_all("a")
        list_data = total_index[0].text.split(" ")
        pagedata = list_data[1].split("/")
        total_pages = pagedata[1]

        tr_data = soup("table", {"class": "my-table"})[0].find_all("tr")

        for data in tr_data:
            datas.append(data.text.split())

        datas = datas[2:-3]
        for data in datas:
            # sn.append(data[0])
            contact.append(data[1])
            stock_symbol.append(data[2])
            buyer_broker.append(data[3])
            seller_broker.append(data[4])
            quantity.append(data[5])
            rate.append(data[6])
            amount.append(data[7])

        if index < int(total_pages):
            print(index)
            scrap_data(index + 1)

    except Exception as e:
        print(e)


scrap_data(0)

data = {
    "contact": contact,
    "stock_symbol": stock_symbol,
    "buyer_broker": buyer_broker,
    "seller_broker": seller_broker,
    "quantity": quantity,
    "rate": rate,
    "amount": amount,
}

data_frame = pd.DataFrame(data)
data_frame.to_csv("nepse_data.csv")

print("Completed")
