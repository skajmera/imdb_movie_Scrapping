import json,os
from task1 import scrap_short
os.mkdir("data/movie")
def scrape_movie_details(pr):
    for i in pr:
        lis=i["link"]
        listid=(lis[27:-1])
        f=open(f"{listid}.json",'w+')
        json.dump(i,f,indent=4)
        f.close()
task8 = scrap_short()
scrape_movie_details(task8)