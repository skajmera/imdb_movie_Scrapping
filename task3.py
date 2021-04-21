from task2_scrap import*
from pprint import pprint
import json
def year_group(moviee):
    moviedec={}
    list1=[]
    for i in moviee:
        mod=i%10
        decade=i-(mod)
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    print(moviedec)
    for i in moviedec:
        dec10=i+9
        for x in moviee:
            if x<=dec10 and x>=i:
                for v in moviee[x]:
                    moviedec[i].append(v)
    f=open("scraping3.json",'w')
    json.dump(moviedec,f,indent=4)  
    print("task3 complete")
                   
    return (moviedec)
task3=(year_group(task2))
# pprint(task3)
    