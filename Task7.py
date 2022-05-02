import json 
import pprint
f = open("movie_details.json","r")
read = f.read()
data = json.loads(read)
i = 0
count_of_Director = {}
while i < len(data):
    for k in data[i]["Director"]:
        j = 0
        c = 0
        sum=""
        while j < len(data):
            if k in data[j]["Director"]:
                c+=1
                sum=k 
            j+=1
        count_of_Director[sum]=c
    i+=1
pprint.pprint(count_of_Director)    
