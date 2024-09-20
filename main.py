import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "product_url": "https://www.snapdeal.com/product/indus-valley-disposable-face-mask/638539148385",
        "name": "Face mask",
        "target-price":400
    },
    {
        "product_url": "https://www.snapdeal.com/product/shoetopia-black-womens-sneakers/6917529647135382559",
        "name": "Shoes",
        "target-price":500
    },
    {
        "product_url": "https://www.snapdeal.com/product/samsung-galaxy-m12-plain-cases/651472486892#bcrumbSearch:samsung%20m12",
        "name": "Samsung phone case",
        "target-price":200
    },
    {
        "product_url":"https://www.amazon.in/Samsung-Thunder-Storage-Corning-Gorilla/dp/B0D7Z8CJP8/ref=sr_1_3?crid=1HT3YQX54G6ER&dib=eyJ2IjoiMSJ9.py3S6sDB957qNVs_s8BlnFiHuTRljMWweZFqouQy0JowZmVX67-ndjJSuN7262VNdJ509sViZnCo3aZqe8EHABxJ7UnXm39vdpIlFKww00f5A2pfLPvzwX7510iX_stN8Ze5Fc_24O3JM6Jp54vAmPLt6FxeLvuKAtultnW72n44QQJP45Z_KUG17Xo7OM-9FR3b6Nd1mJDhlF0Zozwm3eE3DYE4chLt9RNpMHN4jmM.T03DcY4ifUPCUjdyUjAKEdwIuhKccr_UR3cKS2wNicY&dib_tag=se&keywords=m35+5g+samsung&qid=1726848234&sprefix=%2Caps%2C1070&sr=8-3",
        "name":"Samsung M35",
        "target-price":21000
    },
    {
        "product_url":"https://www.amazon.in/Redmi-Arctic-Storage-Flagship-TurboCharge/dp/B0CRQFGKXG/ref=sr_1_12_sspa?crid=1HT3YQX54G6ER&dib=eyJ2IjoiMSJ9.py3S6sDB957qNVs_s8BlnFiHuTRljMWweZFqouQy0JowZmVX67-ndjJSuN7262VNdJ509sViZnCo3aZqe8EHABxJ7UnXm39vdpIlFKww00f5A2pfLPvzwX7510iX_stN8Ze5Fc_24O3JM6Jp54vAmPLt6FxeLvuKAtultnW72n44QQJP45Z_KUG17Xo7OM-9FR3b6Nd1mJDhlF0Zozwm3eE3DYE4chLt9RNpMHN4jmM.T03DcY4ifUPCUjdyUjAKEdwIuhKccr_UR3cKS2wNicY&dib_tag=se&keywords=m35+5g+samsung&qid=1726848234&sprefix=%2Caps%2C1070&sr=8-12-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1",
        "name":"Redmi note 13 pro",
        "target-price":24000
    }
]


def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106"
    }
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')


    price = soup.find("span", {"class": "payBlkBig"})

    if price is None:

        price = soup.find("span", {"class": "a-price-whole"})

    if price:
        return price.getText().strip()
    else:
        return "Price not found"


result_file=open('my_result-file.txt','w')

try:
    for every_product in products_to_track:
        product_price = give_product_price(every_product['product_url'])
        print(f"{product_price} - {every_product['name']}")

        my_product_price = product_price.replace(',', '')
        my_product_price = float(my_product_price)

        if (my_product_price < every_product.get("target-price")):
            print("Availbale at your required price.")
            result_file.write(
                every_product.get("name") + '- \t' + 'Avalilable at target price' + ' Current price-' + str(my_product_price)+ '\n')
        else:
            print("Still at current price")
finally:
    result_file.close()
