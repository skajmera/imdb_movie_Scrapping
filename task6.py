from task1 import*
from task5 import*
from bs4 import BeautifulSoup
import json,requests
from pprint import pprint
def analyse_movies_language(movies_list):
    language_count={}
    for i in movies_list:
        for j in i["language"]:
            if j not in language_count:
                language_count[j]=1
            else:
                language_count[j]+=1
    f=open("scraping6.json",'w')
    json.dump(language_count,f,indent=4)
    return language_count

task6=analyse_movies_language(task5)  
#print(task6)     
    
    