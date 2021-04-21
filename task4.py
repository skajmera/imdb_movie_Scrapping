from task1 import*
from bs4 import BeautifulSoup
import json,requests
from pprint import pprint
def movie_details(x):
    res=requests.get(x)
    soup=BeautifulSoup(res.text,'html.parser')
    
    name_data=soup.find("div",class_="title_wrapper").h1.get_text()
    name=""
    for i in name_data:
        if "(" not in i:
            name=name+i
            name=name.strip()
        else:
            break
    
    summary=soup.find('div',class_="plot_summary").find('div',class_="summary_text").get_text().strip()
    poster=soup.find('div',class_="poster").a['href']
    posterlink='https://www.imdb.com'+poster
    main=soup.find(class_="title-overview")
    time=main.find(class_="title_block").find(class_="subtext").find('time').text.strip()
    runtime=int(time[0])*60
    if 'min' in time:
        minute=int(time[3:].strip('min'))
        runtime+=minute
    director_div=soup.find("div",class_="credit_summary_item")
    director_name=director_div.find_all("a")
    dr=[i.get_text() for i in director_name]
    
    genre_1=soup.find("div",class_="subtext").find_all('a')
    genre_1.pop()
    genre=[]
    for gen in genre_1:
        genre_2=gen.get_text()
        genre.append(genre_2)
    country=main.find(class_="title_block").find(class_="subtext").find(title="See more release dates").text.strip()[-6:-1]     
    lang=soup.find("div",id="main_bottom").find("div",class_="article",id="titleDetails").find_all('div')
    for l in lang:
        la=l.find_all("h4")
        for j in la:
            if "Language:" in j:
                aaa=l.find_all('a')
                languag=[language.get_text()for language in aaa]
 
    dictionary={'name':name,"director":dr,"country":country,"language":languag,"posterimage":posterlink,"bio":summary,"runtime":runtime,"genre":genre}  
    f=open("scraping4.json",'w')
    json.dump(dictionary,f,indent=4)
    print("task4 complete")
    return(dictionary)
url=task1[0]["link"]            
task4=movie_details(url)
# print(task4)
 



###############################################################################################







