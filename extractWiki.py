import urllib2 as ul

#specify the wikipedia page to parse
wiki="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#open page with this url
page = ul.urlopen(wiki)

#from beautiful soup import beautiful soup
from bs4 import BeautifulSoup

#setting html parser for the page
soup = BeautifulSoup(page,"lxml")

#print soup

#print soup.title.string

#print soup.find_all("a")

right_table = soup.find_all("table",class_='wikitable sortable plainrowheaders')
#print right_table
#print all_tables

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for line in right_table:
    for row in line.find_all('tr'):
        cells = row.find_all('td')
        states=row.find_all('th') #To store second column data
        if len(cells)==6: #Only extract table body not heading
            """print cells[0].find(text=True)
            print states[0].find(text=True)
            print cells[1].find(text=True)
            print cells[2].find(text=True)
            print cells[3].find(text=True)
            print cells[4].find(text=True)
            print cells[5].find(text=True)"""
            A.append(cells[0].find(text=True))
            B.append(states[0].find(text=True))
            C.append(cells[1].find(text=True))
            D.append(cells[2].find(text=True))
            E.append(cells[3].find(text=True))
            F.append(cells[4].find(text=True))
            G.append(cells[5].find(text=True))


#import pandas to convert list to data frame
import pandas as pd
pd.set_option('display.width', 1000)
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G

print df














