#!/usr/bin/env python3
import os
import signal
import time
from os.path import getmtime
import sys


a=1

#help(os.execv)
os.chdir(".")
#os.system("bundle exec jekyll serve")
last_modification=os.stat('./_config.yml').st_mtime

     
def kill_proccess():
    output=os.popen('lsof -iTCP:4000').read().split()
    for i in output:
        if 'ruby' in i:
            PID=int(output[output.index(i)+1])
            os.kill(PID,signal.SIGINT)

while a==1 :
    modification=os.stat('./_config.yml').st_mtime
    if last_modification != modification :
        os.system("gnome-terminal -e 'bash -c \"bundle exec jekyll serve\" '")
        last_modification=modification
        continue
        #kill_proccess()
        #os.execv(sys.executable, ['python3'] + sys.argv)
        
        
       

        
        
    
