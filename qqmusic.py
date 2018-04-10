import requests
import re
import json

headers={
    'authority': 'c.y.qq.com',
    'method': 'GET',
    'scheme':'https',
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://y.qq.com/portal/search.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

}

n=input('the song you want')

response=requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61390050690667846&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w='+n+'&g_tk=5381&jsonpCallback=MusicJsonCallback023547204978190184&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'+n,headers=headers)

print(response.status_code)
html=response.text
pattern=re.compile('"strMediaMid":"(.*?)"',re.S)#用一个正则以元祖形式匹配。。。不会。。。老是只有一组
paattern=re.compile('"singer".*?"name":(.*?),"title":')#其他看似正常的匹配都会匹配到第一个是垃圾
paterns=re.compile('lyric_hilight.*?mid":"(.*?)","mv"')#这个匹配出的21个mid的后20个是用来填写z，即songmid因为这个东西和m4a前那串不一定相似
ress=re.findall(paterns,html)
result=re.findall(pattern,html)
ressult=re.findall(paattern,html)



for i in range(0,len(ressult)):
    print(i,ressult[i])

m=input("please the name of thesong you want")
f=ressult[int(m)]
g=result[int(m)]
z=ress[int(m)+1]
print(f)
print(g)
#最后发现songmid不一定和m4a前那串即g相似，其实它是z，见上
res=requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback12426516233411844&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&uin=0&songmid='+z+'&filename=C400'+g+'.m4a&guid=424261942').content
Html=res.decode('utf-8')
#接下来去得到vkey,没技术地使用正则
paaattern=re.compile('"vkey":"(.*?)"',re.S)
resssult=re.search(paaattern,Html)
vkey=resssult.group(1)
print(vkey)
#构造请求
header={
    'Host':'dl.stream.qqmusic.qq.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
parameter={
    'vkey':vkey,
    'guid':'424261942',
    'uin':'0',
    'fromtag':'66'}
print("downloading")
response=requests.get("http://dl.stream.qqmusic.qq.com/C400"+g+".m4a?vkey="+vkey+"&guid=424261942&uin=0&fromtag=66",headers=header,params=parameter).content

d=f.replace('"','')
with open("D:/"+d+"."+n+".mp3","wb") as f:
    f.write(response)
    f.flush()
    print("done")
