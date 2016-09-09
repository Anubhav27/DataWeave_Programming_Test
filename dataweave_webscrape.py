from lxml import html
import requests
import json
url_to_scrape = requests.get('http://www.shopclues.com/computers/desktops-and-monitors/monitors.html')

html_tree = html.fromstring(url_to_scrape.content)

root = html_tree.xpath('//div[@class="details"]')

Url=[]
Url_text=[]
Price=[]
Price_Currency=[]
Thumbnail=[]
product_json_list=[]


Url = html_tree.xpath('//div[@class="details"]/a[@class="name"]/@href')
Url_text = html_tree.xpath('//div[@class="details"]/a[@class="name"]/text()')
Price = html_tree.xpath('//div[@class="details"]/div[@class="product-price"]/span[@class="price"]/text()')
Price_Currency = html_tree.xpath('//div[@class="details"]/div[@class="product-price"]/span[@class="price-substrip"]/text()')

for j in range(len(Url)):
    #print Url[j]
    link_to_scrape = requests.get(Url[j])
    url_html_tree = html.fromstring(link_to_scrape.content)
    img_link = url_html_tree.xpath('//div[@class="slide"]//img/@src2')
    Thumbnail.append(img_link)



for i in range(len(root)):
    json_dict={}
    json_dict['Url'] = Url[i]
    json_dict['Title'] = Url_text[i]
    json_dict['Price'] = Price_Currency[i]+Price[i]
    json_dict['Thumbnail'] = Thumbnail[i]
    product_json_list.append(json_dict)



f = open("product_list.txt","w")
for i in product_json_list:
    json.dump(i,f)

f.close()






