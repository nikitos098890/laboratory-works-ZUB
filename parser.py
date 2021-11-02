import requests
from bs4 import BeautifulSoup as BS

page = 1

while True:
    print(str(page))
    current_link = "https://stopgame.ru/review/new/izumitelno/p" + str(page)
    print(current_link)
    r = requests.get("https://stopgame.ru/review/new/izumitelno/p" + str(page))
    html = BS(r.content, 'html.parser')
    items = html.select(".items > .article-summary")

    if(len(items)):
        for el in items:
            title = el.select('.caption > a')
            print(title[0].text)
        page += 1
    else:
        break
f=open('parser.py')
i=0
for line in f:
    i
    i+=1
print('строк выведено',i)



