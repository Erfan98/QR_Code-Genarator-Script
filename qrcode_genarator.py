from PIL import Image,ImageDraw
import qrcode
import os
print("Enter Your Name=")
name=input()
#os.mkdir(name)
print("How many qrcode you want to genarate?")
num=int(input())
for i in range(num):
    print("Enter your data to genarate your QRCODE")
    data=input()
    pic=qrcode.make(data)
    pic.save("{0}-{1}.png".format(name,i+1))
