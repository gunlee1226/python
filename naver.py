from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = urlopen('https://movie.naver.com/movie/running/current.nhn')

print(req.getcode())

if req.getcode() == 200:
    html = req.read()
    html = html.decode("utf-8")

else:
    print("HTTP ERROR")

bs = BeautifulSoup(html, "html.parser")

movies = bs.select(".lst_detail_t1 > li")

for movie in movies:
    titles = movie.select(".lst_dsc > .tit > a")
    for title in titles:
        print(title.text, title['href'])


