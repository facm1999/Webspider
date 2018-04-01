
import urllib.request
import urllib.error
from urllib.parse import urlencode
import http.cookiejar


data={
    'TPL_username':'13940204365',
    'TPL_password':'an123789',
    'slideCodeShow':'false',
    'useMobile':'false'
                        }
headers={
    'method':'POST',

    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
data=urlencode(data).encode()

#操作cookie
cookie_filename='cookie.txt'
cookie=http.cookiejar.MozillaCookieJar(cookie_filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)

result=urllib.request.Request('https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F',data,headers)
try:
    response=opener.open(result)
    print(response.read().encode("utf-8"))
except urllib.error.URLError as e:
    print(e.reason)

#保存cookie    
cookie.save(ignore_discard=True,ignore_expires=True)    


