"""

This is Question 3 of Assignment to shorten Url

Solution :

The solution takes input from file and from console and shorten the Url based on Algorithm implemented below.

file url_list.txt contains list of links to be shorten
after it shortens the url it add it to url_shortening_dict dictionary.
"""

import string
import binascii
import binhex

url_list=['http://www.ffh.com/','http://www.ffggg.com/']
url="http://www.ffh.com/"

alphabet_list=string.lowercase + string.uppercase + string.digits

alphabet_dictionary = {}



url_shortening_dict={}


def shorten(url):
    url_mod = url.replace(".","").replace(":","").replace("//","").replace("/","")
    #print url_mod
    alphabet_count = 0
    for val in alphabet_list:
        alphabet_dictionary[val] = alphabet_count
        alphabet_count = alphabet_count + 1
    """for key in alphabet_dictionary.items():
        print key"""
    bits = bin(int(binascii.hexlify(url_mod.encode("utf-8")), 16))[2:]
    dd = bits.zfill(8 * ((len(bits) + 7) // 8))
    dd_len = dd.__len__()
    #print dd_len
    while (dd_len % 3) != 0:
        dd = dd + str(0)
        dd_len = dd_len+1
        #print dd_len
    #print dd
    #print dd_len
    shorten_url=""
    for i in range(0,len(dd),6):
        #print int(dd[i:i+6],2)
        val = int(dd[i:i+6],2)
        for k,v in alphabet_dictionary.items():
            if val==v:
                shorten_url = shorten_url + k

    url_shortening_dict[url] = shorten_url[ :: -1][0:6]
    #encoding_url = base64.b64encode(md5.new(url).digest()[-5:]).replace('=', '').replace('/', '_')
    #url_shortening_dict[url] = encoding_url


choice = input('Enter choice 1 to take url as input from console or 2 to read from file :  ')
if choice == 1:
    url = raw_input("enter url to shorten : ")
    shorten(url)
elif choice == 2:
    with open('url_list.txt') as fp:
        for line in fp:
            shorten(line)

"""for u in url_list:
   shorten(u)"""

#print url_shortening_dict.__len__()

for j in url_shortening_dict:
    print j + "," + url_shortening_dict[j]




