#!/usr/bin/python2.7
import requests
import os
import datetime

"""
#Juste in case I want stop this script remotly

r = requests.get("https://pastebin.com/raw/9vzu2CA5")

cmd=str(r.text)
check ="stopit"
if check == cmd :
        os.system('cp /home/alice/script/log.py /home/alice/script/log.bak')

"""


path="/var/log/apache2"
dir = os.listdir(path)
date = str(datetime.datetime.now())
for logfile in dir :
        clear = open(path+"/"+logfile, "w")
        clear.truncate(0)
        clear.close()
logfile = open("/home/alice/script/clear.log","w")
logfile.write("last clear apache log "+date)
logfile.close()
