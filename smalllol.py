import requests
response=requests.get('http://ossweb-img.qq.com/images/lol/web201310/skin/big81001.jpg').content
with open('D:/1.jpg',"wb") as f:
    f.write(response)
    f.flush()
