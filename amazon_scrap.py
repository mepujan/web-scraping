from bs4 import BeautifulSoup
from selenium import webdriver
url = "https://www.amazon.com/b?node=283155&fbclid=IwAR2r2BhS_sKmIxjeqa5Sx2t7y969J7TrwA2IDJjLFQlC7pkzGqxqPEppcJk"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')
driver = webdriver.Chrome()
try:
    request = driver.get(url)
except:
    print("No connection found")

page = BeautifulSoup(driver.page_source, "html.parser")

all_data = page.findAll("li",{"class":"a-carousel-card"})

for data in all_data:
    image = data.find("img")['src']
    title = data.find("span",{"class":"a-truncate-full a-offscreen"})
    author = data.find("span",{"class": "a-truncate acs-product-block__contributor a-size-base"}).span
    price = data.find("div",{"class":"a-section a-spacing-micro acs-product-block__price"}).find("span",{"class":"a-offscreen"})
    if price is not None and title is not None and author is not None:
        print(image)
        print(title.text)
        print(author.text)
        print(price.text)




