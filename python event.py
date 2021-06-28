from bs4 import BeautifulSoup
import requests
import json

def python_event():
    python_event_api = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    python_event_url = requests.get(python_event_api)
    python_event_data = python_event_url.json
    soup = BeautifulSoup(python_event_url.text,'html.parser')
    k = soup.find("div",class_ = "mw-body")
    l=k.find("table",class_ = "infobox vevent")
    n=l.find("tbody")
    j=l.find("caption",class_="infobox-title summary").get_text()
    name =n.find_all("tr")
    list = []
    for i in name:
        python_event_chart = j+i.get_text()
        list.append(python_event_chart)
        with open ("python_event_chart.json","w") as python_data:
            json.dump(list,python_data,indent = 4)
    return(list)
print(python_event())

