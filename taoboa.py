import requests
import re 
import os,sys
import random
import time 

i=input("the name of the product")
global path
path="D:/"+i
os.mkdir(path)

headers={
    'referer':'https://www.taobao.com',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'cookie':'thw=cn; t=cbbebb253d89f5acc069b3bfeee932c3; cna=CiksE90eLSYCAXWIBWq+x+yf; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; lgc=an1466226205; tracknick=an1466226205; uc3=nk2=An8CSiW6PaUk4Ect&id2=UNN0mI49dGHB9Q%3D%3D&vt3=F8dBz4KArlbRqda%2FNGw%3D&lg2=URm48syIIVrSKA%3D%3D; mt=np=&ci=0_1; _cc_=U%2BGCWk%2F7og%3D%3D; v=0; cookie2=2dfe0ca1a7cbae4f437ff988a4d4be75; _tb_token_=e7397d73673b6; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; JSESSIONID=F5BF347ED2819F87CBC96C810879F8FD; isg=BOzsOGL2mgQ6_I4wqwuG8RK4vcPeDd_OeLZt_UYt-hc6UYxbbrVg3-LjdRFpWcin; swfstore=100234'
}
response=requests.get("https://s.taobao.com/search?q="+i,headers=headers).text
print(response)
pattern=re.compile('pic_url\":\"(.*?)\"',re.S)
result=re.findall(pattern,response)
for s in result:
    response=requests.get("http:"+s).content
    a=s.replace("//",'')
    with open(path+'/'+str(random.randint(1,1000))+'.jpg',"wb") as f:
        f.write(response)
        f.flush()
