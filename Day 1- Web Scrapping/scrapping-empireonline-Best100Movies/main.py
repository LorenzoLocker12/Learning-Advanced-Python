import requests as re
from bs4 import BeautifulSoup

response = re.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

titles_html = soup.find_all(name="h3", class_="title")

titles_name = [title.getText() for title in titles_html]

reversed_titles_name = titles_name[::-1]


with open("movies.txt", "w", encoding="utf-8") as file:
    for title in reversed_titles_name:
        file.write(title + "\n")


