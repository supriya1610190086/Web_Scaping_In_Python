from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
import os
from os import path

def pickel():
    if os.path.isfile("pickel.json"):
        with open("pickel.json","r") as file:
            data = json.load(file)
            return data
    else:
        api = "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
        url=requests.get(api)
        soup = BeautifulSoup(url.text,'html.parser')
        div = soup.find('div',class_='_1gX7')
        product_no = div.span.get_text()
        split_list =product_no.split(" ")
        a =int(split_list[1])
        b=a//32+1
        pickel=[]
        number = 0
        pickel_no=1
        pickel_index=1
        while pickel_index<=b:
            pikels_api = "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(pickel_index)
            pikels_url = requests.get(pikels_api)
            pickel_Soup=BeautifulSoup(pikels_url.text,"html.parser")
            pickels_div = pickel_Soup.find('div',class_="_3RA-")
            pical_name = pickels_div.find_all("div",class_ = "UGUy")
            pickles_rate=pickels_div.find_all('div',class_='_1kMS')
            pickles_link= pickels_div.find_all('div',class_='_3WhJ')
            i=0
            while i<len(pical_name):
                number+=1
                pickel_name = pical_name[i].get_text()
                pikel_link = pickles_link[i].a['href']
                pickle_rate = pickles_rate[i].get_text()
                pickel_url = 'https://paytmmall.com'+pikel_link
                pickels_details = {'position':number,'name':pickel_name,'price':pickle_rate,'url':pickel_url}
                pickel.append(pickels_details.copy())
                i=i+1
            pickel_index=pickel_index+1
        with open("pickel.json","w") as _data:
            json.dump(pickel,_data,indent = 4)
        return(pickel)
pprint(pickel())
