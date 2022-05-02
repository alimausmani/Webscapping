# import json
# from bs4 import BeautifulSoup 
# import requests
# import pprint
# urls="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
# page=requests.get(urls)
# soup=BeautifulSoup(page.text,'html.parser')

# def scrap_top_list():
#     main_div=soup.find('div',class_='lister')
#     tbody=main_div.find('tbody',class_='lister-list')
#     trs=tbody.find_all('tr')

#     movie_ranks=[]
#     movie_name=[]
#     year_of_realease=[]
#     movie_urls=[]
#     movie_ratings=[]

#     for tr in trs:
#         position=tr.find('td',class_='titleColumn').get_text().strip()
#         rank=''
#         for i in position:
#             if '.' not in i:
#                 rank=rank+i
#             else:
#                 break
#         movie_ranks.append(rank)

#         tilte=tr.find('td',class_='titleColumn').a.get_text()
#         movie_name.append(tilte)

#         year=tr.find('td',class_='titleColumn').span.get_text()
#         year_of_realease.append(year) 

#         imdb_rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text() 
#         movie_ratings.append(imdb_rating)

#         link=tr.find('td',class_='titleColumn').a['href']
#         movie_link="https://www.imdb.com"+link 
#         movie_urls.append(movie_link)

#     Top_Movies=[]
#     details={'position':'','name':'','year':'','rating':'','url':''}
#     for i in range(0,len(movie_ranks)):
#         details['position']=int(movie_ranks[i]) 
#         details['name']=str(movie_name[i])
#         year_of_realease[i]=year_of_realease[i][1:5] 
#         details['year']=int(year_of_realease[i])
#         details['rating']=float(movie_ratings[i])
#         details['url']= movie_urls[i]
#         Top_Movies.append(details.copy()) 
#     with open("top_movies.json","w") as f:
#         json.dump(Top_Movies,f,indent=4) 
#     return Top_Movies   
 
# pprint.pprint(scrap_top_list())                     



# import json
# file = open("top_movies.json","r")
# a = file.read()
# data = json.loads(a)
# i=0
# while i<len(data):
#     j=0
#     while j<len(data):
#         if data[i]["year"]<=data[j]["year"]:
#             temp=data[i]
#             data[i]=data[j]
#             data[j]=temp
#             j+=1
#         i+=1
# dict1={}
# i=0
# while i<len(data):
#     list1=[]
#     j=0
#     while j<len(data):
#         if data[i]["year"] == data[j]["year"]:
#             list1.append(data[j])
#         j+=1
#     dict1[data[i]["year"]]=list1
#     i+=1
# with open("group_by_year.json","w") as f:
#     json.dump(dict1,f,indent=4)      

# from importlib.resources import path
# from bs4 import BeautifulSoup
# import json,os.path
# import requests
# import json
# import pprint         
# f = open("top_movie.json","r")
# read = f.read()
# data = json.loads(read)
# movie_details = []
# user=input("enter the movie name :- ")
# i = 0
# while i < len(data):
#     if data[i]["movie_rank"]==user:
#         r=data[i]["movie URL"][33:]+".json"
#         rd=None
#         if os.path.exists (r):
#             o=open(r)
#             rd=o.read()
#             print(rd)
#         elif rd==None:
#             def scrape_movie_details(movie_url):
#                 page = requests.get(movie_url)
#                 soup = BeautifulSoup(page.text,'html.parser')
#                 poster = soup.find('div',class_ = "col mob col-center-right col-full-xs mop-main-column")
#                 poster_image = poster.find('button',class_ = "trailer_play_action_button")
#                 if poster_image is None:
#                     poster_image = poster.find('div',class_="movie-thumbnail-wrap").img
#                     image = poster_image["data-src"]
#                 else:
#                     image = poster_image["data-thumbnail"]
            
#                 movie_name = poster.find('div',class_ = "thumbnail-scoreboard-wrap").h1.get_text()

#                 movie_info = poster.find('section',class_ = "panel panel-rt panel-box movie_info media")
#                 info = movie_info.find('div',class_ = "panel-body content_body")
#                 bio = info.find('div',class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
                
#                 movie_genre = info.find('ul',class_="content-meta info")
#                 genre = movie_genre.find('div',class_= "meta-value genre").get_text()
#                 list1=[]
#                 sum = ""
#                 for i in genre:
#                     if "," not in genre :
#                         list1.append(genre.strip())
#                         break
#                     if i != ",":
#                         if i.isalpha():
#                             sum+=i
#                     else:
#                         list1.append(sum)
#                         sum = ""
#                 movie_genre = info.find('ul',class_="content-meta info")
#                 sub_li = movie_genre.find_all('li')
#                 for li in sub_li:
#                     sub = li.find('div',class_="meta-label subtle").get_text().strip()
#                     if sub == "Original Language:" :
#                         lan = li.find('div',class_ = "meta-value").get_text().strip()
#                     if sub == "Director:" :
#                         direct = li.find("div",class_ = "meta-value")
#                         director = direct.find_all('a')
#                         list3 = []
#                         for a in director :
#                             list3.append(a.get_text())
#                     if sub == "Runtime:":
#                         duration = li.find("div",class_="meta-value").get_text().strip()
#                         if len(duration) == 5:
#                             runtime = int(duration[0])*60+int(duration[3:4])
#                         else:
#                             runtime = int(duration[0])*60+int(duration[3:5])
                        
#                 dict1 = {"name":"","Director":"" , "language":"", "poster_image_url":"","bio":"", "runtime":"","genre":""}
#                 dict1["name"] = movie_name
#                 dict1["poster_image_url"] = image
#                 dict1["bio"] = bio
#                 dict1["genre"] = list1
#                 dict1["language"] = lan
#                 dict1["Director"] = list3
#                 dict1["runtime"] = runtime
#                 print(dict1)
#                 movie_details.append(dict1)
#                 with open(url1[33:]+".json","w") as f:
#                     json.dump(dict1 , f , indent=4)
#             url1 = data[i]["movie URL"]
#             with open("movie_details.json","w") as f:
#                 json.dump(movie_details,f,indent=4)
#             scrape_movie_details(url1)
#     i+=1
