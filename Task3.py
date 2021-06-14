from Task1 import scrap_top_list
from Task2 import group_by_year
import json

scrapped = scrap_top_list()
dec_arg= group_by_year(scrapped)

def group_by_decade(movies):
    mod_dic={}
    list=[]
    for i in movies:
        mod = i%10
        decade=i-mod
        if decade not in list:
            list.append(decade)
    list.sort()
    for i in list:
        mod_dic[i]=[]
    for i in mod_dic:
        dec10=i+9
        for j in movies:
            if j<dec10 and j>=i:
                for k in movies[j]:
                    mod_dic[i].append(k)
                    with open("decade_year.json","w") as f:
                        json.dump(mod_dic,f,indent=4)
    return (mod_dic)
group_by_decade(dec_arg)

                    

    

