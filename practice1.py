import requests 
from bs4 import BeautifulSoup
import pandas as pd
import time


url = 'https://yachtanahi.com/availability-2024/'
req = requests.get(url)
soup=BeautifulSoup(req.content,  'html.parser')
travel=[]
for row in soup.select('div.question.active'):
    date = row.find('td', class_ = 'htMiddle htCenter bg-001a4b color-ffffff bold').get_text()
    tour = row.find('td', class_ = 'htMiddle htCenter bold color-444242').find('a', class_ = 'p-tableTour').get_text()
    duration = row.find('td', class_ = 'htMiddle htCenter bold color-444242').get_text()
    avail1 = row.find_all('td', class_='htMiddle htCenter bold color-444242')[1].get_text()
    avail2 = row.find_all('td', class_='htMiddle htCenter bold color-444242')[2].get_text()
    promotion = row.find('td', class_='htMiddle htCenter bold color-444242').get_text()
    travel.append([date, tour, duration, avail1, avail2, promotion])
df = pd.DataFrame(travel, columns=['Date', 'Tour', 'Duaration', 'Avail1', 'Avail2', 'Promotion'])
time.sleep(1)
text = soup.get_text()
print(text)
df.to_csv('Output.csv') 
