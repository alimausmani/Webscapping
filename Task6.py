import json
f = open("movie_details.json","r")
read = f.read()
data = json.loads(read)
i = 0
count_of_language = {}
while i < len(data):
    j = 0
    count = 0 
    while j < len(data[i]["language"]):
        count = 0
        k = 0 
        while k < len(data):
            for l in data[k]["language"]:
                if  data[i]["language"][j] == l :
                    count+=1
            k+=1
        count_of_language[data[i]["language"]] = count
        j+=1
    i+=1
print(count_of_language)