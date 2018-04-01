from random import random
import requests
import re
import json
import time

global headers
headers={
    'Referer':'http://lol.qq.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9'
    }
def geturl():
    html=requests.get("http://lol.qq.com/biz/hero/champion.js",headers=headers).text
    print(requests.get("http://lol.qq.com/biz/hero/champion.js",headers=headers).status_code)

    #匹配出英雄名
    pattern=re.compile('.*champion.*?:(.*?),"data',re.S)
    list=re.search(pattern,html)
    dict=json.loads(list.group(1))
    return dict
#做成list
def getheros(dict):
    heros=[]
    for i  in dict.keys():
        heros.append(dict[i])
    return heros
#找到url下载
def loadsurl(heros):
    for j in heros:
        html=requests.get("http://lol.qq.com/biz/hero/"+j+".js",headers=headers).text
        pattern=re.compile('"id":"(\d*)"',re.S)
        result=re.findall(pattern,html)
        print(result)
        time.sleep(3)
        global m
        for m in result:
            list=[]
            list.append('http://ossweb-img.qq.com/images/lol/web201310/skin/big'+m+'.jpg')
#这里存在循环后重置列表的错误还需要考虑
            return list
def downloads(list):
    for n in list:
        html=requests.get(n,headers=headers).content
        print(requests.get(n,headers=headers).status_code,n)
        if requests.get(n,headers=headers).status_code==200:
            with open("D:/lol/"+m+".jpg","wb") as f:
                f.write(html)
                f.flush()
                time.sleep(3)
def main():
    dict=geturl()
    heros=getheros(dict)
    list=loadsurl(heros)
    downloads(list)
if __name__=='__main__':
    main()

