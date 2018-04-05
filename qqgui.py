from tkinter import *


import requests

global headers
#爬虫的请求头
headers = {
            'authority': 'c.y.qq.com',
            'method': 'GET',
            'path': '/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61390050690667846&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E6%88%91%E4%BB%AC%E4%B8%8D%E4%B8%80%E6%A0%B7&g_tk=5381&jsonpCallback=MusicJsonCallback023547204978190184&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'pgv_pvid=424261942; yq_index=0; ts_uid=4926174980; pgv_pvi=9929293824; yqq_stat=0; pgv_si=s1387702272; pgv_info=ssid=s6110750850; ts_last=y.qq.com/portal/search.html',
            'pragma': 'no-cache',
            'referer': 'https://y.qq.com/portal/search.html',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

}

#先构造出主架
root=Tk()
root.title='qq音乐下载'
root.geometry('500x500+400+200')

#这是提示输入
Label(root,text='请输入要下载的歌曲名',bg='green').pack(fill=X)
#这是输入框
var1=StringVar()
var2=StringVar()
var2.set('')
var1.set('')
Entry(root,textvariable=var1).pack(fill=X,pady=40)

#这是按钮
def getvar(var):
    return var.get()



def getsong(n):
    response = requests.get(
        'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61390050690667846&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=' + n + '&g_tk=5381&jsonpCallback=MusicJsonCallback023547204978190184&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0' + n,
        headers=headers)
    html = response.text
    pattern = re.compile('"strMediaMid":"(.*?)"', re.S)  # 用一个正则以元祖形式匹配。。。不会。。。老是只有一组
    paattern = re.compile('"singer".*?"name":(.*?),"title":')  # 其他看似正常的匹配都会匹配到第一个是垃圾
    ressult = re.findall(paattern, html)
    result = re.findall(pattern, html)
    for i in range(0,20):
        print(i,ressult[i])
Button(root,width=30,height=5,text='搜索',command=lambda:getsong(getvar(var1))).pack(pady=20)

Label(root,text='输入你要下的歌的序列',bg='red').pack(fill=X,pady=20)

Entry(root,textvariable=var2).pack(pady=20,fill=X)

Button(root,width=30,height=5,text='下载',command=lambda:download(downloadsong(getvar(var1))[int(getvar(var2))])).pack(side=RIGHT)


def downloadsong(n):
    response = requests.get(
        'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61390050690667846&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=' + n + '&g_tk=5381&jsonpCallback=MusicJsonCallback023547204978190184&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0' + n,
        headers=headers)
    html = response.text
    pattern = re.compile('"strMediaMid":"(.*?)"', re.S)  # 用一个正则以元祖形式匹配。。。不会。。。老是只有一组
    paattern = re.compile('"singer".*?"name":(.*?),"title":')  # 其他看似正常的匹配都会匹配到第一个是垃圾
    ressult = re.findall(paattern, html)
    result = re.findall(pattern, html)
    return result

def download(g):
    res = requests.get(
        'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback12426516233411844&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&uin=0&songmid=' + g + '&filename=C400' + g + '.m4a&guid=424261942').content
    Html = res.decode('utf-8')
    # 接下来去得到vkey,没技术地使用正则
    paaattern = re.compile('"vkey":"(.*?)"', re.S)
    resssult = re.search(paaattern, Html)
    vkey = resssult.group(1)
    # 构造请求
    header = {
        'Host': 'dl.stream.qqmusic.qq.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    parameter = {
        'vkey': vkey,
        'guid': '424261942',
        'uin': '0',
        'fromtag': '66'}
    response = requests.get(
        "http://dl.stream.qqmusic.qq.com/C400" + g + ".m4a?vkey=" + vkey + "&guid=424261942&uin=0&fromtag=66",
        headers=header, params=parameter).content
    with open(getvar(var1)+".mp3", "wb") as f:
        f.write(response)
        f.flush()

















root.mainloop()
