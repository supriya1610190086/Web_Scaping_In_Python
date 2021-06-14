from Task1 import scrap_top_list
import json

scrapped = scrap_top_list()
def group_by_year(movies):
    years = []
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[] for i in years }
    for i in movies:
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
                with open("movie_year.json","w") as file:
                    json.dump(movie_dict,file,indent=4)
    return movie_dict
group_by_year(scrapped)
