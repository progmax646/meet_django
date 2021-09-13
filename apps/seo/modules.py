import requests
from bs4 import BeautifulSoup


class Seo:
    def get_url(type, keyword, page):
        if type == 1:
            url = f'https://www.google.com/search?q={keyword}&start={page}'
        if type == 2:
            url = f'https://yandex.uz/search/?lr=10335&text={keyword}'
        return url


    def get_position(type, keyword):
        position = ''
        if type == 1:
            pages = [0, 10, 20, 30, 40]
            n = 0
            i = 1
            while n < len(pages):
                url = Seo.get_url(1, keyword, pages[n])
                headers = {'user-agent': 'my-app/0.0.1'}
                r = requests.get(url, headers=headers)

                soup = BeautifulSoup(r.content, 'html.parser')
                contents = soup.find_all(class_='kCrYT')

                links = []

                for item in contents:
                    a = item.a
                    if a != None:
                        links.append(a.get('href'))

                status = False
                for item in links:
                    if item[:26] == '/url?q=https://legalact.uz':
                        position = i
                        status = True
                    i = i + 1
                n = n + 1
                if status == True:
                    break

        if type == 2:
            url = get_url(2, keyword)
            headers = {'user-agent': 'my-app/0.0.1'}
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            contents = soup.find_all(class_='serp-item')
            print(soup.prettify())
            link = []
        return position