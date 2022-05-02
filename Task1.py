from bs4 import BeautifulSoup
import requests
import json
import pprint

def adventure_movie():
    adventure_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    adventure_api=requests.get(adventure_url)
    print(adventure_url.text)

    htmlcontent=adventure_api.content
    soup=BeautifulSoup(htmlcontent,"html.parser")
    table_tag=soup.find("table",class_="table")
    tr=table_tag.find_all("tr")
    top_movie=[]
    serial_no=1
    for i in tr:
        movie_rank=i.find_all("td",class_="bold")
        for j in movie_rank:
            rank=j.get_text()
        movie_rating=i.find_all("span",class_="tMeterScore")
        for rate in  movie_rating:
            rating=rate.get_text().strip()
        movie_name=i.find_all("a",class_="unstyled articleLink")
        for name in movie_name:
            title=name.get_text().strip()
            list=title.split()
            year=list[-1][1:5]
            year1=int(year)
            name_lenght=len(list)-1
            name=""
            for l in range(name_lenght):
                name+=""
                name+=list[l]
            movie_name=name
        movie_reviews=i.find_all("td",class_="right hidden-xs")
        for rev in movie_reviews:
            reviews=rev.get_text()
        url=i.find_all("a",class_="unstyled articleLink")
        for i in url:
            link=i["href"]
            movie_link="https://www.rottentomatoes.com"+link
            details={"movie_rank":"","movie_rating":"","movie_name":"","movie_reviews":"","movie URL":"","year":""}
            details["movie_rank"]=rank
            details["movie_rating"]=rating
            details["movie_name"]=movie_name
            details["movie_reviews"]=reviews
            details["movie URL"]=movie_link
            details["year"]=year1
            top_movie.append(details.copy())
            print(top_movie)
    with open("top_movie.json","w")as file:
        json.dump(top_movie,file,indent=4)
    return top_movie
data=adventure_movie()
pprint.pprint(adventure_movie())

# from bs4 import BeautifulSoup
# import requests
# import json
# import pprint

# def adventure_movie():
#     adventure_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
#     adventure_api=requests.get(adventure_url)

#     htmlcontent=adventure_api.content
#     soup=BeautifulSoup(htmlcontent,"html.parser")
#     table_tag=soup.find("table",class_="table")
#     tr=table_tag.find_all("tr")
#     top_movie=[]
#     serial_no=1
#     for i in tr:
#         movie_rank=i.find_all("td",class_="bold")
#         for j in movie_rank:
#             rank=j.get_text()
#         movie_rating=i.find_all("span",class_="tMeterScore")
#         for rate in  movie_rating:
#             rating=rate.get_text().strip()
#         movie_name=i.find_all("a",class_="unstyled articleLink")
#         for name in movie_name:
#             title=name.get_text().strip()
#             list=title.split()
#             year=list[-1][1:5]
#             year1=int(year)
#             name_lenght=len(list)-1
#             name=""
#             for l in range(name_lenght):
#                 name+=""
#                 name+=list[l]
#             movie_name=name
#         movie_reviews=i.find_all("td",class_="right hidden-xs")
#         for rev in movie_reviews:
#             reviews=rev.get_text()
#         url=i.find_all("a",class_="unstyled articleLink")
#         for i in url:
#             link=i["href"]
#             movie_link="https://www.rottentomatoes.com"+link
#             details={"movie_rank":rank,"movie_rating":rating,"movie_name":movie_name,"movie_reviews":reviews,"movie URL":movie_link,"year":year1}
#             top_movie.append(details.copy())
#             print(top_movie)
#     with open("group_by_year.json","w")as file:
#         json.dump(top_movie,file,indent=4)
#     return top_movie
# data=adventure_movie()
# pprint.pprint(adventure_movie())