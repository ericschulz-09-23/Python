import requests
from bs4 import BeautifulSoup
response = requests.get('https://yachtanahi.com/availability-2024/')
soup = BeautifulSoup(response.content, 'html.parser')
text=soup.get_text()
print(text)