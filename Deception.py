import time
import urllib.request

with open(r"C:\Users\ElNiNo\Desktop\Boardgame\deception cards\Scene and location\myp.txt","r") as r:
    reader = r.read()
i = 1
for line in reader.splitlines():
    img_name = r"C:\Users\ElNiNo\Desktop\Boardgame\deception cards\Scene and location\tile"+str(i)+".png"
    time.sleep(4)
    urllib.request.urlretrieve(line, img_name)
    print(f"wohoo! {i} done Out of "+str(len(reader.splitlines())))
    i = i+1