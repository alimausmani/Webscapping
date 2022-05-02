import requests
from bs4 import BeautifulSoup
import json , os.path
import pprint
f = open("top_movie.json","r")
read = f.read()
data = json.loads(read)
get_all_movie_details = []
i  = 0 
while i < len(data):
    print(str(i+1)+".",data[i]["movie_name"])
    i+=1
n = 0
user = input("enter a movie name:")
actor_list = []
while n < len(data):
    if data[n]["movie_name"].strip() == user:
        if os.path.exists(str(data[n]["movie_name"].strip())+"cast.json"):
            with open(str(data[n]["movie_name"].strip())+"cast.json","r") as f:
                data = json.load(f)
                print(data)
        else:
            def analyse_actors (movie_url):
                page = requests.get(movie_url)
                soup = BeautifulSoup(page.text,'html.parser')
                actor = soup.find('div',class_ = "col mob col-center-right col-full-xs mop-main-column")
                castsection = actor.find('section',id ="movie-cast")
                crew = castsection.find_all('div',class_="media-body")
                for i in crew :
                    dict1 = {"id":"","name":""}
                    character = i.find('span',class_ = "characters subtle smaller").get_text().strip()
                    # print(character)
                    if character == "Director":
                        break
                    else:
                        if i.find('a') != None :
                            dict1["name"]= i.span.get_text().strip()
                            dict1["id"]= i.a["href"].strip()
                            actor_list.append(dict1)
            url1 = data[n]["movie URL"]
            analyse_actors(url1)
            with open(str(data[n]["name"].strip())+"cast.json","w") as f:
                json.dump(actor_list,f,indent=4)
    n+=1