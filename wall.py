import ctypes
import time
from os import listdir
from os.path import isfile, join

info = open("./info.txt","r").readlines()
info = [s.rstrip('\n') for s in info]

path = info[0]
images = [f for f in listdir(path) if isfile(join(path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]

time_to_sleep = int(info[1])
count = 0
no_of_images = len(images)

while True:
    image = images[count]
    
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + "\\" + image , 0)
    
    count += 1
    if count == no_of_images:
        count = 0
    
    time.sleep(time_to_sleep)