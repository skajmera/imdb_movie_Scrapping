import json
from pprint import pprint
from task1 import*
def task_2(mov):
    years_list=[]
    for i in mov:
        year1=i["years"]
        if year1 not in years_list:
            years_list.append(year1)
    movies_dic={i:[]for i in years_list} 
    for i in mov:
        year1=i["years"]
        for x in movies_dic:
            if str(x)==str(year1):
                movies_dic[x].append(i)
    f=open("scraping2.json",'w')
    json.dump(movies_dic,f,indent=4) 
    print("task2 complete")
    return movies_dic
    

task2=(task_2(task1)) 
# print(task2)
    
    