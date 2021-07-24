from bs4 import BeautifulSoup
from pprint import pprint
import requests,csv,json,os
res=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
def scrap_short():
    if os.path.exists("scraping.json"):
        f=open("scraping.json",'r')
        file=json.load(f)
        return(file)
    else:
        soup=BeautifulSoup(res.text,'html.parser')
        raw_html=soup.find("tbody",{"class":"lister-list"}).findAll("tr")
        
        movies,position,years,rating,link=[],[],[],[],[]
                
        for i in raw_html:  
            movies.append(i.find("td",{"class":"titleColumn"}).find("a").get_text())
            years.append(i.find("span",{"class":"secondaryInfo"}).text)
            stri=(i.find("td",{"class":"ratingColumn imdbRating"}).text)
            rating.append(float(stri.strip()))
            position.append(int(i.text.strip().split('.')[0]))
            link.append('https://www.imdb.com'+i.find("a").get('href'))
        dic={}
        list1=[]
        for i,j,k,l,m in zip(movies,years,rating,position,link):
            dic["movies"]=i
            j=j[1:5]
            j=int(j)
            dic["years"]=j
            dic["rating"]=k
            dic["position"]=l
            dic["link"]=m
            list1.append(dic.copy())
        f=open("scraping.json",'w')
        json.dump(list1,f,indent=4)
        f.close()
        return(list1)
task1=scrap_short()
print(task1)
