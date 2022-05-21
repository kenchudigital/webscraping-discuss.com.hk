import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://ladies.discuss.com.hk/viewthread.php?tid=30568678"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
title = soup.find_all('span')[0].get_text()
last_page = soup.find_all("a", class_='last')[0].get_text()
last_page = last_page.split(' ')[1]
last_page = int(last_page)
print(f"title is: {title}")
print(f"the last page is {last_page}")

comment_list = []
for page_no in range(last_page):
    page_no += 1
    page = requests.get(url + f"&extra=&page={page_no}")
    soup = BeautifulSoup(page.text, 'html.parser')
    num = 0
    result = True
    while result is True:
        try:
            comment = soup.find_all('span', id = re.compile('^postorig_'))[num].get_text()
            comment_list.append(comment)
            num += 1
            result = True
        except:
            result = False

# show the comment list as dataframe
df = pd.DataFrame(comment_list)
df