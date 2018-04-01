#导入库
from PIL import Image
#定义对应灰度值的函数
ascii_char = list("abcdefg$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!;:,\"^`'.")
global ascii_char
def get_char(r,g,b,alpha=256):
    if alpha == 0 :
        return ' '
    length=len(ascii_char)
    gray= 0.2126* r + 0.7152 * g + 0.0722 * b
    return ascii_char [int((gray/(256+1)) * length)]
#写成字符画
def parse(width=80,height=60,filename='3.jpg'):
    im=Image.open(filename)
    im=im.resize((width,height))
    txt=""
    for i in range (height) :
        for j in range (width) :
            txt= txt+ get_char(*im.getpixel((j,i)))
            save(txt)
        txt  = txt + '\n'
    print(txt)
def save(content):
    with open("2.txt","w") as f :
        f.write(content)
def main():
    parse(width=80,height=80,filename='3.jpg')
if __name__=='__main__':
    main()    