# 
# 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser
from PIL import Image
from io import BytesIO

#web page of choosing
site = "https://www.smithsonianmag.com/category/photo-of-the-day/"

with open("index.html", "r") as file:
	html = file.read()

soup = BeautifulSoup(html, 'html.parser')

image_place = soup.find('aside', {'class': 'day-feature'})

image = image_place.find('img')['src']

"""im = BytesIO(image.read())
i = Image.open(im)
i.show()"""

webbrowser.open(image)

print(image)