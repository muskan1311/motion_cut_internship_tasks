import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

def item_title(soup):
    try:
        title = soup.find("span", attrs={"id":'productTitle'})
        title_value = title.text
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

def item_price(soup):

    try:
        
        price = soup.find("span",attrs={'class':"a-offscreen"}).string.strip()

    except AttributeError:
            price = ""

    return price

def item_brand(soup):
    try:
        brand = soup.find("span",{'class':"a-size-base po-break-word"}).text.strip()
    except:
        brand = ''

    return brand
     


def item_rating(soup):
    try:
        rating = soup.find("span", attrs={'class':"a-icon-alt"}).string.strip()
   
    except:
        rating = ""	

    return rating

def item_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available_text = available.find("span").string.strip()
    

    except AttributeError:
        available_text = "Not Available"	

    return available_text


if __name__ == '__main__':
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0', 'Accept-Language': 'en-US, en;q=0.5'})
    url = 'https://www.amazon.in/mobile-under-50000-5g-phone/s?k=mobile+under+50000+5g+phone'
    page = requests.get(url, headers= HEADERS)

    soup = BeautifulSoup(page.content,'html.parser')

    links = soup.find_all('a', attrs= {'class':"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
    # print(links[0])
    link_list = []

    for link in links:
        link_list.append(link.get("href"))

    d = {"title":[], "price":[], "brand":[], "availability":[],"rating":[]}

    for link in link_list:
        item_pages = requests.get("https://www.amazon.in" + link, headers=HEADERS)
        item_soup = BeautifulSoup(item_pages.content,'html.parser')
   
        # function calls 
        d['title'].append(item_title(item_soup))
        d['brand'].append(item_brand(item_soup))
        d['price'].append(item_price(item_soup))
        d['availability'].append(item_availability(item_soup))
        d['rating'].append(item_rating(item_soup))


    
    phones_under_50k_df = pd.DataFrame.from_dict(d)
    phones_under_50k_df['title'].replace('', np.nan, inplace=True)
    phones_under_50k_df = phones_under_50k_df.dropna(subset=['title'])
    phones_under_50k_df.to_csv("phones_under_50k.csv", header=True, index=False)
        

