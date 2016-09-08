from lxml import html
import requests

url_to_scrape = requests.get('http://www.shopclues.com/computers/desktops-and-monitors/monitors.html')

tree = html.fromstring(url_to_scrape.content)



tree = html.fromstring(url_to_scrape.content)

root = tree.xpath('//div[@class="details"]')


for d in root:
    for url in d.xpath('//a[@class="name"]'):
        print url.text

        #print url['text']










