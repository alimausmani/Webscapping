import json
file = open("movie_details.json","r")
a = file.read()
data = json.loads(a)
i = 0
director = {}
while i < len(data):
        for j in data[i]["Director"]:
                director[j] = {}
        i+=1
k = 0
while k < len(data):
        for d in director:
                if d in data[k]["Director"]:
                        director[d][data[k]["language"]] = 0
        k+=1
l = 0
while l < len(data):
        for d in director:
                if d in data[l]["Director"]:
                   director[d][data[l]["language"]] += 1     
        l+=1
with open("analyse_language_and_directors.json","w") as f:
        json.dump(director,f,indent=4)

