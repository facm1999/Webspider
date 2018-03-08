import re
import requests
url=input('the website of song')
global url

#根据hash值来构造播放网址
def get_hash():
    pattern=re.compile('http.*hash=(.*)',re.S)
    result=re.findall(pattern,url)
    return result[0]

#找到保存.mp3链接和名字的url并获取相关内容
def get_url(hash):
    url="http://www.kugou.com/yy/index.php?r=play/getdata&hash="+str(hash)+"&album_id=1013501&_=1520493831795"
    html=requests.get(url).text
    result=re.search('"play_url"(.*)authors',html,re.S)
    url=result.group(1)[2:-3]
    url=url.replace("\\","")
    return url

def get_name(hash):
    url="http://www.kugou.com/yy/index.php?r=play/getdata&hash="+str(hash)+"&album_id=1013501&_=1520493831795"
    html=requests.get(url).text
    result=re.search('"audio_name"(.*)have_album',html,re.S)
    name=result.group(1)[2:-3]
    name=name.encode()
    name=name.decode('unicode_escape')
    return name


#下载    
def download(name,url):
    html=requests.get(url).content
    with open(name+'.mp3',"wb") as f :
        f.write(html)
        f.flush()    

def main():
    hash=get_hash()
    url=get_url(hash)
    name=get_name(hash)
    download(name,url)
if __name__=='__main__':
    main()            
