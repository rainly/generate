## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
#北京赛车 自动打码神器
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
from selenium.common.exceptions import NoSuchElementException
import sqlite3
import threading  
import time

import urllib
import urllib.request
import urllib.response
import urllib.error
import http.cookiejar
from ajjkk6779 import *



if __name__ == "__main__":
    url_agent = "http://121.40.206.168/soft_net/SBDL_NSkt.php?NS=" + "tingziji"
    #print(url_agent)
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
        exit(0)
    except urllib.error.URLError as e:
        #print('We failed to reach a server.')
        #print('Reason: ' + e.reason)
        print("错误","网络连接错误！")
        exit(0)
    except Exception as msg:
        print("Exception:%s" % msg)
        exit(0)
    except:
        #print("error lineno:" + str(sys._getframe().f_lineno))
        print("错误","网络连接错误！")
        exit(0)
    html = html.strip()
    print(html)
    if html != "1":
        print("错误","账号未注册！")
        exit(0)
    main()
    
