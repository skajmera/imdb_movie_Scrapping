from task1 import*
from task4 import movie_details 
from bs4 import BeautifulSoup
import json,requests
from pprint import pprint
def get_movie_list_details(top_movie):
    movie_details_list=[]
    for i in top_movie:
        task4_url=i["link"]
        a=(movie_details(task4_url))
        movie_details_list.append(a)
    f=open("scraping5.json",'w')
    json.dump(movie_details_list,f,indent=4)
    return movie_details_list
    
task5=get_movie_list_details(task1[0:10])
# print(task5)

