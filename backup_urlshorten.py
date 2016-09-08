import math
import base64
import md5

def shorten(url):
    url_len = url.__len__()
    print url.__len__()
    # print string.lowercase + string.uppercase + string.digits
    alpha = string.lowercase + string.uppercase + string.digits + string.punctuation
    print alpha
    alpha_len = alpha.__len__()
    print alpha_len

    # for l in range(url_len):
    # print url[l]
    # print alpha.index(url[l])
    # num = num * alpha_len + alpha.index(url[l])

    # print base64.b64encode(md5.new(url).digest()[-5:]).replace('=','').replace('/','_')
    print md5.new(url).digest()


shorten(url)
