from bs4 import BeautifulSoup
import requests
import json
import pprint
f = open("top_movie.json","r")
read = f.read()
data = json.loads(read)
user = (input("enter a position of movie :"))
i = 0
while i < len(data):
    if data[i]["movie_rank"] == user:
        def scrape_movie_details(movie_url):
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
                    
            dict1 = {"name":"","Director":"" , "language":"", "poster_image_url":"","bio":"", "runtime":"","genre":""}
            dict1["name"] = movie_name
            dict1["poster_image_url"] = image
            dict1["bio"] = bio
            dict1["genre"] = list1
            dict1["language"] = lan
            dict1["Director"] = list3
            dict1["runtime"] = runtime
            print(dict1)
            with open(dict1["name"]+".json","w") as f:
                json.dump(dict1 , f , indent=4)
        url1 = data[i]["movie URL"]
        scrape_movie_details(url1)
    i+=1