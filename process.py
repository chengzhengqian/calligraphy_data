from PIL import Image
import numpy as np

style="楷"
filename="一_10-虞世南.svg.png"
# file="./{style}/{file}".format(style=style,file=filename)

def readImage(file):
    return 1.0-np.array(Image.open(file))/65535

def readText(file):
    with open(file, 'r') as myfile:
        return myfile.read()

def readInfo(word):
    return [ i.split("/")[-1] for i in readText("./{style}/{word}_info.txt".format(style=style,word=word)).split()]



import os
font_dict={}
directory="./{style}".format(style=style)
processed_font_dict={}
def readAllInfo():
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            word=filename[0]
            font_dict[word]=readInfo(word)

readAllInfo()
# a=readfile(file);plt.imshow(a,cmap="gray");plt.show()

for k in font_dict:
    print("processing {0}".format(k))
    processed_font_dict[k]=[processInfo(info) for info in font_dict[k]]

import h5py
datafile=h5py.File('楷_32x32.h5', 'w')
for word in processed_font_dict:
    print(word)
    for index, info in enumerate(processed_font_dict[word]):
        keydata="{word}-{index}-data".format(word=word,index=index)
        keyauthor="{word}-{index}-author".format(word=word,index=index)
        print(keydata)
        datafile.create_dataset(keydata,data=info[0])
        datafile.create_dataset(keyauthor,data=info[1])
datafile.close()
# datafile.update("main",data=[1,2])
# datafile.close()

# readfile=h5py.File('楷_32x32.h5', 'r')
# readfile.close()


import re
pattern=re.compile("(.)_(.+)-(.+).svg.png")
def parseInfo(file):
    m=pattern.match(file)
    return m.group(3)

def processInfo(file):
    image=readImage("./{style}/{file}".format(style=style,file=file))
    author=parseInfo(file)
    return (image,author)

# avg=sum([len(font_dict[k])  for k in font_dict])/len(font_dict)
# min([len(font_dict[k])  for k in font_dict])
# max([len(font_dict[k])  for k in font_dict])
   
# from matplotlib import pyplot as plt


