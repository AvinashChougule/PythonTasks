import requests
from bs4 import BeautifulSoup
price = [
            {
                'URL_price' : 'https://www.flipkart.com/apple-iphone-12-mini-black-64-gb/p/itm38b727191eb08?pid=MOBFWBYZXSEGBS6F&lid=LSTMOBFWBYZXSEGBS6FTONJ6W&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=browse&fm=neo%2Fmerchandising&iid=c24de0ef-d1bb-49c4-b2a6-913e746210ba.MOBFWBYZXSEGBS6F.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=ivzwr049m80000001645522875629',
                'name':'Iphone 12',
                'targetPrice':16000
            },
            {
                'URL_price' : 'https://www.flipkart.com/realme-c11-2021-cool-grey-32-gb/p/itmbd856acb97c38?pid=MOBG4BEGX8QYNKGZ&lid=LSTMOBG4BEGX8QYNKGZXOJ4Y8&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=clp_banner_2_8.bannerX3.BANNER_mobile-phones-store_BAB8E5MUKP8U&fm=neo%2Fmerchandising&iid=26ef937c-2987-4082-9be4-868cdafbabf4.MOBG4BEGX8QYNKGZ.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=vdu0usvx8g0000001645522927585',
                'name':'RealMe C11',
                'targetPrice':16000
            },
            {
                'URL_price' : 'https://www.flipkart.com/google-pixel-4a-just-black-128-gb/p/itm023b9677aa45d?pid=MOBFUSBNAZGY7HQU&lid=LSTMOBFUSBNAZGY7HQUPPRQAA&otracker=clp_banner_2_27.bannerX3.BANNER_mobile-phones-store_YAI1YW5J1R5D&fm=neo%2Fmerchandising&iid=M_49550474-d8bf-44a1-9534-c26e3e80ccea_27.YAI1YW5J1R5D&ppt=clp&ppn=mobile-phones-store',
                'name':'Pixel',
                'targetPrice': 16500
            },
            {
                'URL_price': 'https://www.flipkart.com/samsung-galaxy-f12-sky-blue-64-gb/p/itm0319ce24f74aa?pid=MOBGFG79BVGDHGWV&lid=LSTMOBGFG79BVGDHGWVGF2CRI&marketplace=FLIPKART&q=Samsung&store=search.flipkart.com&spotlightTagId=BestsellerId_search.flipkart.com&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=dbcd6a80-a8cc-42ce-94fa-bd3ef32ac287.MOBGFG79BVGDHGWV.SEARCH&ppt=sp&ppn=sp&ssid=h36wqduehs0000001645592841617&qH=3910b1e0ccab19bc',
                'name':'SAMSUNG Galaxy F12',
                'targetPrice':10400
            },
            {
                'URL_price': 'https://www.flipkart.com/motorola-g60-dynamic-gray-128-gb/p/itmf1d5d2978289e?pid=MOBFWSF8U37QFQGK&lid=LSTMOBFWSF8U37QFQGKG9BJEQ&marketplace=FLIPKART&q=mobiles&store=search.flipkart.com&srno=s_1_19&otracker=search&otracker1=search&fm=Search&iid=bf29bd7e-6f42-48de-81b9-23fda76ecd6b.MOBFWSF8U37QFQGK.SEARCH&ppt=sp&ppn=sp&ssid=am24kk6ssg0000001645592921672&qH=eb4af0bf07c16429',
                'name':'MOTOROLA G60',
                'targetPrice':10000
            }
        ]

def product_Trace(URL_price):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    page = requests.get(URL_price, headers=header)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)

    item = soup.find('div', class_=["_30jeq3 _16Jk6d"," "])
    if (item == None):
        item = soup.find('div', class_=["_30jeq3 _16Jk6d"," "])
    return item.getText()

result = open('result_file.txt','w')

try:

    for all_product in price:
        allPrice = product_Trace(all_product.get('URL_price'))
        print(allPrice + " - ", all_product.get('name'))

        cartPrice = allPrice[1:]
        cartPrice = cartPrice.replace(',', '')
        cartPrice = int(cartPrice)
        print(cartPrice)
        if cartPrice < all_product.get('targetPrice'):
            print('Product Available at your cart')
            result.write(all_product.get('name') + '-\t' + 'Available at Target Price' + ' and Current Price is ' + str(cartPrice)+' Rs.'+'\n')
        else:
            print('Price is High')
finally:
    result.close()