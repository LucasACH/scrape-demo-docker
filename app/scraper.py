import requests
from bs4 import BeautifulSoup

def getDellXPS():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    url = "https://www.dell.com/en-us/shop/dell-laptops/new-xps-15-laptop/spd/xps-15-9500-laptop/xn9500ecxns?view=configurations&configurationid=95224666-5e10-4468-a3fb-a31523ae2312"

    response = requests.get(url, headers)
    content = response.content
    soup = BeautifulSoup(content, features = "lxml")

    laptopName = ""
    laptopPrice = 0


    for title in soup.findAll('div', attrs={'class':'cf-product-order'}):
        laptopName = title.text.replace("\n", "")

    for price in soup.findAll('div', attrs={'class':'cf-dell-price'}):
        laptopPrice = float(price.text.replace(" ", "").replace("\n", "").replace("$", "").replace(",", ""))
        
    result = """
    The {laptopName} costs ${laptopPrice}
    """.format(laptopName = laptopName, laptopPrice = laptopPrice)
    
    print(result)


if __name__ == "__main__":
    getDellXPS()
