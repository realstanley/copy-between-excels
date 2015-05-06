#coding=utf-8
import os
import sys
import time
import subprocess as sub
tomcat=r"D:\debug\tomcat6.0\bin"
fox=r"C:\Program Files\Mozilla Firefox"

os.chdir(tomcat)
bat=sub.Popen(r'startup.bat')
time.sleep(1)
os.chdir(fox)
ff=sub.Popen(r"firefox.exe")

'''
os.system('pause')
ff.kill()
time.sleep(1)
bat.kill()'''
