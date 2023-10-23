import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://xipgroc.cat/ca/curses/Bombers2023/10k/resultats?&ordre=finish_time&page=66"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table_data = soup.find('table', class_ = 'resultats finalitzada')

headers = ["Posició", "Posició por sexe", "Dorsal", "Nom", "Temps Oficial", "Temps Real"]
# for i in table_data.find_all('th'):
#     title = i.text
#     headers.append(title)

print(headers)

df = pd.DataFrame(columns = headers)

print(df)

i = 0

for data in table_data.find_all('tr')[1:]:
    i += 1
    if i % 3 != 2:
        continue
    #print(j)
    row_data = data.find_all('td')
    #print(row_data)

    j = 0
    row = []
    for tr in row_data:
        j += 1
        if j in (2, 3, 4, 6, 7):
            text = " ".join(tr.text.split())

            if j == 7:
                officialAndRealTime = text.partition(" (tr ")
                officialTime = officialAndRealTime[0]
                realTime = officialAndRealTime[2][:-1]

                row.append(officialTime)
                row.append(realTime)

            else:
                row.append(text)
            
    print(row)
    length = len(df)
    #print(length)
    print("---------------------------------------------------------------------------------------------------------------------------------")
    df.loc[length] = row

print(df)