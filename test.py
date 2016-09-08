import urllib2 as ul

url_to_scrape="http://www.shopclues.com/computers/desktops-and-monitors/monitors.html"

page = ul.urlopen(url_to_scrape)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page,"lxml")

#print soup.prettify()

right_div = soup.find_all('div',class_='details')

#print right_div

Title=[]
Url=[]
Thumbnail=[]



#for each_div in right_div:

        #for row in each_div.find_all('a'):
            #print row
            #print row.string
            #print row['href']

for each_div in right_div:
    print each_div