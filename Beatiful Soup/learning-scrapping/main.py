from bs4 import BeautifulSoup
# import lxml


with open("./website.html", encoding="utf-8") as file:
    website = file.read()

soup = BeautifulSoup(website, "html.parser")

# print(soup.prettify())

# print(soup.title.name)

# print(soup.title.string)

# all_anchor_tags = soup.find_all("a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# name = soup.find(name="h1", id="name")
# print(name)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))