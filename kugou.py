import re
import requests
global hash
hash=input('your hash')

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


    
def download(name,url):
    html=requests.get(url).content
    with open(name+'.mp3',"wb") as f :
        f.write(html)
        f.flush()    
def main():
    url=get_url(hash)
    name=get_name(hash)
    download(name,url)
if __name__=='__main__':
    main()            