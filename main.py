import requests
import re
from bs4 import BeautifulSoup


def check_keywords(words, text):
    pattern = r"("+'|'.join(words)+")"
    regex = re.compile(pattern, re.IGNORECASE)
    find_words = regex.findall(text)
    if len(find_words) == 0:
        return 0
    else:
        return 1


def search_keywords():
    soup = BeautifulSoup(response.text, features='html.parser')
    articles = soup.find_all('article')

    for article in articles:
        title = article.find('a', class_='post__title_link')
        date = article.find('span', class_='post__time')
        preview = article.find('div', class_='post__text')

        if check_keywords(keywords, preview.text) == 1:
            print(date.text, title.text, title.get('href'), 'preview', sep=' - ')
        else:
            article_response = requests.get(title.get('href'))

            article_soup = BeautifulSoup(article_response.text, features='html.parser')
            article_text = article_soup.find('div', class_='post__text')

            if check_keywords(keywords, article_text.get_text()) == 1:
                print(date.text, title.text, title.get('href'), 'article', sep=' - ')


if __name__ == '__main__':
    keywords = ['дизайн', 'фото', 'web', 'python']
    response = requests.get('https://habr.com/ru/all/')
    search_keywords()