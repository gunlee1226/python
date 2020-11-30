from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = urlopen('https://www.10000recipe.com/recipe/6904080')

print(req.getcode())

if req.getcode() == 200:
    html = req.read()
    html = html.decode("utf-8")

else:
    print("HTTP ERROR")

bs = BeautifulSoup(html, "html.parser")

recipe = bs.select(".view_step > #stepDiv2 , #stepDiv3, #stepDiv4, #stepDiv5, #stepDiv6, #stepDiv7, #stepDiv8")


for recipes in recipe:
    print(recipes.get_text(), end = "\n " )




