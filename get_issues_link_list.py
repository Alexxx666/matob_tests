import requests
from bs4 import BeautifulSoup


def writeResult(data):
    with open("issues_link_list.txt", "a") as text_file:
        text_file.write(data)


response = requests.get("https://matob.ru/archive.html")
response.encoding = 'utf8'
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', download=True)
    writeResult(str(links))
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
