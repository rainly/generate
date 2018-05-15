## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
#梯子游戏

from tkinter import *
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import messagebox as mBox
import tkinter.messagebox as messagebox
import tkinter as tk
from selenium import webdriver
from selenium.common.exceptions import *
#import sqlite3
import threading  
import time
import json
import urllib
import urllib.request
import urllib.response
import urllib.error
import http.cookiejar
import configparser
import re
import ssl
import sys
from c48_bjpk import *
ssl._create_default_https_context = ssl._create_unverified_context


#声明一个CookieJar对象实例来保存cookie
cookiejar = cookiejar = http.cookiejar.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookiejar)
#通过handler来构建opener
opener = urllib.request.build_opener(handler)

#此处的open方法同urllib2的urlopen方法，也可以传入request
#response = opener.open('http://www.baidu.com')
user_agent = 'Mozilla/5.0 (Windows NT 6.1 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'  
headers = { 'User-Agent' : user_agent }  


def RegKey():
    url_agent = "http://duboren.com/ccskey/query?regkey=1981c8aeb5b973ef3a578156d5527eb9"
    request = urllib.request.Request(url_agent, headers = headers)
    try:
        #response = urllib.request.urlopen(request)
        response = opener.open(request, timeout = 5)
        html = response.read().decode()
    except urllib.error.HTTPError as e:
        #print('The server couldn\'t fulfill the request.')
        #print('Error code: ' + str(e.code))
        #print('Error reason: ' + e.reason)
        print("错误","网络连接错误！")
        return False
    except urllib.error.URLError as e:
        #print('We failed to reach a server.')
        #print('Reason: ' + e.reason)
        print("错误","网络连接错误！")
        return False
    except Exception as msg:
        print("Exception:%s" % msg)
        return False
    except:
        #print("error lineno:" + str(sys._getframe().f_lineno))
        print("错误","网络连接错误！")
        return False
    html = html.strip()
    #print(html)
    json_data = json.loads(html)
    if json_data["success"] != True:
        print("错误","账号未注册！")
        if "datas" in json_data:  
            print("错误", json_data["datas"]["notice"])
        return False
    else:
        return True

if __name__ == "__main__":
    if RegKey():
        main()
        


































