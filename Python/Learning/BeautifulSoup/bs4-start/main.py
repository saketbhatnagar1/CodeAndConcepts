from bs4 import BeautifulSoup
with open("website.html") as fil:
    content = fil.read()

soup = BeautifulSoup(content,"html.parser")
print(soup.title.string)
print(soup.prettify())
print(soup.a.href,"STRING")
print(soup.find_all("a"))
print(soup.find(id="name")) 