import os
import h5py
# we first do a simple task, train a cnn to classify two difference authors
import matplotlib.pyplot as plt

for root, dirs, files in os.walk("./processed"):
    for filename in files:
        readfile=h5py.File(root+"/"+filename, 'r')
        for key in readfile.keys():
            if(key.endswith("author")):
                keydata=key.replace("author","-data")
                print(readfile.get(key).value)
                # print(readfile.get(keydata).value)
                plt.imshow(readfile.get(keydata).value)
                plt.show()


readfile=h5py.File("./processed/一_32x32.h5","r")

# a=readfile[list(readfile.keys())[1]].value

                
        
