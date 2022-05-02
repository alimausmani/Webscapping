import requests
from bs4 import BeautifulSoup
import json , os.path , random , time
import pprint
f = open("top_movie.json","r")
read = f.read()
top_data = json.loads(read)
get_all_movie_details = []
n = 0
while n < len(top_data):
    def scrape_movie_details(movie_url):
        random_sleep = random.randint(1,3)
        r = str(n+1)+top_data[n]["movie URL"][33:]+".json"
        rd = None
        if os.path.exists(r):
            o = open(r)
            rd = o.read()
            movie = json.loads(rd)
            get_all_movie_details.append(movie)
            for i in movie:
                if i == "cast":
                    print(movie)
                else:
                    if os.path.exists(str(top_data[n]["movie_name"].strip())+"cast.json"):
                        with open(str(top_data[n]["movie_name"].strip())+"cast.json") as f:
                            list6 = json.load(f)
                            s = {"cast":list6}
                            with open(r , "r+") as file:
                                dat = json.load(file)
                                dat.update(s)
                                file.seek(0)
                                json.dump(dat, file , indent=4) 
                    else:
                            actor_list = []
                            page = requests.get(url1)
                            soup = BeautifulSoup(page.text,'html.parser')
                            actor = soup.find('div',class_ = "col mob col-center-right col-full-xs mop-main-column")
                            castsection = actor.find('section',id ="movie-cast")
                            crew = castsection.find_all('div',class_="media-body")
                            for i in crew :
                                dict1 = {"id":"","movie_name":""}
                                character = i.find('span',class_ = "characters subtle smaller").get_text().strip()
                                if character == "Director":
                                    break
                                else:
                                    if i.find('a') != None :
                                        dict1["movie_name"]= i.span.get_text().strip()
                                        dict1["id"]= i.a["href"].strip()
                                        actor_list.append(dict1)
                            with open(str(top_data[n]["movie_name"].strip())+"cast.json","w") as cfile:
                                json.dump(actor_list,cfile,indent=4)
        if rd == None:
                time.sleep(random_sleep)
                page = requests.get(movie_url)
                soup = BeautifulSoup(page.text,'html.parser')
                poster = soup.find('div',class_ = "col mob col-center-right col-full-xs mop-main-column")
                poster_image = poster.find('button',class_ = "trailer_play_action_button")
                if poster_image is None:
                    poster_image = poster.find('div',class_="movie-thumbnail-wrap").img
                    image = poster_image["data-src"]
                else:
                    image = poster_image["data-thumbnail"]
            
                movie_name = poster.find('div',class_ = "thumbnail-scoreboard-wrap").h1.get_text()

                movie_info = poster.find('section',class_ = "panel panel-rt panel-box movie_info media")
                info = movie_info.find('div',class_ = "panel-body content_body")
                bio = info.find('div',class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
                
                movie_genre = info.find('ul',class_="content-meta info")
                genre = movie_genre.find('div',class_= "meta-value genre").get_text()
                list1=[]
                sum = ""
                for i in genre:
                    if "," not in genre :
                        list1.append(genre.strip())
                        break
                    if i != ",":
                        if i.isalpha():
                            sum+=i
                    else:
                        list1.append(sum)
                        sum = ""
                movie_genre = info.find('ul',class_="content-meta info")
                sub_li = movie_genre.find_all('li')
                for li in sub_li:
                    sub = li.find('div',class_="meta-label subtle").get_text().strip()
                    if sub == "Original Language:" :
                        lan = li.find('div',class_ = "meta-value").get_text().strip()
                    if sub == "Director:" :
                        direct = li.find("div",class_ = "meta-value")
                        director = direct.find_all('a')
                        list3 = []
                        for a in director :
                            list3.append(a.get_text())
                    if sub == "Runtime:":
                        duration = li.find("div",class_="meta-value").get_text().strip()
                        if len(duration) == 5:
                            runtime = int(duration[0])*60+int(duration[3:4])
                        else:
                            runtime = int(duration[0])*60+int(duration[3:5])
                actor_list = []
                actor = soup.find('div',class_ = "col mob col-center-right col-full-xs mop-main-column")
                castsection = actor.find('section',id ="movie-cast")
                crew = castsection.find_all('div',class_="media-body")
                for i in crew :
                    dict1 = {"id":"","movie_name":""}
                    character = i.find('span',class_ = "characters subtle smaller").get_text().strip()
                    if character == "Director":
                        break
                    else:
                        if i.find('a') != None :
                            dict1["movie_name"]= i.span.get_text().strip()
                            dict1["id"]= i.a["href"].strip()
                            actor_list.append(dict1)
                with open(str(top_data[n]["movie_name"].strip())+"cast.json","w") as cfile:
                    json.dump(actor_list,cfile,indent=4) 
                dict1 = {"name":"","Director":"" , "language":"", "poster_image_url":"","bio":"", "runtime":"","genre":""}
                dict1["name"] = movie_name
                dict1["poster_image_url"] = image
                dict1["bio"] = bio
                dict1["genre"] = list1
                dict1["language"] = lan
                dict1["Director"] = list3
                dict1["runtime"] = runtime
                dict1["cast"] = actor_list
                get_all_movie_details.append(dict1)
                js = str(n+1)+url1[33:]+".json"
                with open(js,"w") as f:
                    json.dump(dict1 , f , indent=4)
    
    url1 = top_data[n]["movie URL"]
    scrape_movie_details(url1)
    n+=1
with open("all_movie1_details.json","w") as f :
    json.dump(get_all_movie_details,f,indent=4)