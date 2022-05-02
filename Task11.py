import json
file = open("movie_details.json","r")
a = file.read()
data = json.loads(a)
i = 0
genre = {}
while i < len(data):
        for j in data[i]["genre"]:
                genre[j] = 0
        i+=1
k = 0
while k < len(data):
    for d in genre:
        if d in data[k]["genre"]:
            genre[d]+=1
    k+=1
with open("analyse_movies_genre .json","w") as f:
        json.dump(genre,f,indent=4)