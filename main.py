from bs4 import BeautifulSoup
import requests
import datetime
import csv
import datefinder

start_date = datetime.date(2019,1,1)
date_csv = {}

for single_date in (start_date + datetime.timedelta(n) for n in range(365)):
    date_csv[single_date.isoformat()]=0
#print(date_csv)

f = csv.writer(open('output.csv', 'w'))

page = requests.get('https://en.wikipedia.org/wiki/2019_in_spaceflight#Orbital_launches')
soup = BeautifulSoup(page.text, 'html.parser')
text = soup.find(text = "LSP").find_parent("table")

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

successful_payloads = [
    "Successful",
    "Operational",
    "En Route"]

table_rows = text.find_all("tr")
toggle = 0

for row in table_rows:
    for month in months:
        if month in str(row):
            if month in str(row.contents[1]):
                if toggle ==1:
                    date_csv[curr_date.isoformat()[:10]]+=1
                toggle = 0
                current_date_index = str(row).index(month) - 3
                current_date = str(row)[current_date_index:len(month)+current_date_index+3]
                if current_date[:2].isnumeric() :
                    curr_date = datetime.datetime.strptime(current_date+' 2019','%d %B %Y')
                    #print(curr_date.isoformat())
                elif  current_date[1:2].isnumeric():
                    curr_date = datetime.datetime.strptime(current_date[1:]+' 2019','%d %B %Y')
                    #print(curr_date.isoformat())
            
    for payload in successful_payloads:
        if payload in str(row):
            toggle = 1
            
        
print(date_csv)
for date in date_csv:
    f.writerow([date+'T00:00:00+00:00',date_csv[date]])
