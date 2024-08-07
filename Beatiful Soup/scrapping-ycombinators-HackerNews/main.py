from bs4 import BeautifulSoup
import requests
import re

idk = {}

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

titles = soup.select(".athing")

for i in titles:

    first_a = i.select_one(".titleline a")
    title_text = first_a.getText()
    href = first_a.get("href")

    score = i.find_next_sibling("tr").select_one(".score")
    if score:
        points = score.getText()
        numbers = re.findall(r'\d+', points)
        for i in numbers:
            points_int = int(i)
    else:
        points_int = 0
    idk[title_text] = [href, points_int]

highest_points = -1

for key, value in idk.items():
    if value[1] > highest_points:
        highest_points = value[1]
        highest_article = key
        highest_article_url = value[0]



print(f"Best Article: {highest_article}\nArticle URL: {highest_article_url}\nHighest points: {highest_points}")
