import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://supu-test-app.firebaseapp.com/')
soup = bs(res.text,'html.parser')
# td_titles = soup.find_all('td',class='title') 
td_titles = soup.find_all('td',class_='title')

for t in td_titles:
  print(t.string)