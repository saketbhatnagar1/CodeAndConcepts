from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/")
yc_page = response.text
BeautifulSoup(yc_page,"html.parser")

soup = BeautifulSoup(yc_page,"html.parser")
tag = soup.find(name="a")
text = tag.getText()
link = tag.get("href")
print(f"link :{link}, text: {text}")