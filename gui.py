import tkinter 
import re
import requests
root=tkinter.Tk()
root.title('酷狗')
root.geometry('400x300')
label=tkinter.Label(root,text='输入网址上的hash值')
label.pack()
var=tkinter.StringVar()
entry=tkinter.Entry(root,textvariable=var)
entry.pack()
def get_hash():
    return var.get()

def get_song(hash):
    
    url="http://www.kugou.com/yy/index.php?r=play/getdata&hash="+str(hash)+"&album_id=1013501&_=1520493831795"
    html=requests.get(url).text
    result=re.search('"play_url"(.*)authors',html,re.S)
    url=result.group(1)[2:-3]
    song_url=url.replace("\\","")
    url="http://www.kugou.com/yy/index.php?r=play/getdata&hash="+str(hash)+"&album_id=1013501&_=1520493831795"
    html=requests.get(url).text
    result=re.search('"audio_name"(.*)have_album',html,re.S)
    name=result.group(1)[2:-3]
    name=name.encode()
    name=name.decode('unicode_escape')
    html=requests.get(song_url).content
    with open(name+'.mp3',"wb") as f :
        f.write(html)
        f.flush()  
 
     

button=tkinter.Button(root,text='下载',command=lambda:get_song(get_hash()))
button.pack()


root.mainloop()


