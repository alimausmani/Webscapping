import json
file = open("top_movie.json","r")
a = file.read()
details = json.loads(a)
i=0
while i<len(details):
    j=0
    while j<len(details):
        if details[i]["year"]<details[j]["year"]:
            temp=details[i]
            details[i]=details[j]
            details[j]=temp
        j+=1
    i+=1
dict1={}
i=0
while i<len(details):
    list1=[]
    j=0
    while j<len(details):
        if details[i]["year"] == details[j]["year"]:
            list1.append(details[j])
        j+=1
    dict1[details[i]["year"]]=list1
    i+=1
with open("group_by_year.json","w") as f:
    json.dump(dict1,f,indent=4)           



