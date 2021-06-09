#coding:utf-8
from urllib3 import *

import re
import os

import urllib3

global word
word = ""
 
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
    "referer": "https://image.baidu.com"
}

http = urllib3.PoolManager()

def gen_url():
    url = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+word+"&pn=0&gsm=140&ct=&ic=0&lm=-1&width=0&height=0"
    return url

def gethtml(url):
    r = http.request('GET',url,headers=head)
    return r.data.decode('utf-8')

def getimg(html):
    reg = r'"objURL":"(.*?)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

def download(urllist,path):
    index = 1
    path = path+word
    if(os.path.exists(path)!= True):
        os.mkdir(path)
    for url in urllist:
        print("dowloading:",url)
        try:
            res = http.request('GET',url,headers=head)
        except Exception as e:
            print("failed!",url)
        filename = path + r"/"+str(index)+ ".jpg"
        f=open(filename,"wb+")
        f.write(res.data)
        f.close()
        print('download complete！：',filename)
        index += 1

if __name__ == "__main__":
    word = str(input("请输入要查找内容："))
    url = gen_url()
    urllist = getimg(gethtml(url))
    download(urllist,r'K:/')
    #for url in urllist:
    #    print(http.request('GET',url,headers=head))
