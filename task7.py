from task1 import*
from task5 import*
from bs4 import BeautifulSoup
import json,requests
from pprint import pprint
def analyse_movies_language(movies_list):
    director_count={}
    for i in movies_list:
        for j in i["director"]:
            if j not in director_count:
                director_count[j]=1
            else:
                director_count[j]+=1
    f=open("scraping7.json",'w')
    json.dump(director_count,f,indent=4)
    return director_count

task7=analyse_movies_language(task5)  
print(task7)     
    
    