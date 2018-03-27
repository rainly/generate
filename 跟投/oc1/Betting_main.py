## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
#跟投 自动打码神器
    
import re
import urllib
import urllib.request
import sys
import io
import json
import time
import datetime
import http.cookiejar
import json
#import pymysql.cursors
import ssl
#import sqlite3
import configparser
import random

from bs4 import BeautifulSoup  # 引入beautifulsoup 解析html事半功倍
from collections import deque
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.common.exceptions import NoSuchElementException
from tkinter import *
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import messagebox as mBox

import tkinter.messagebox as messagebox
import tkinter as tk
import threading
import time
import io
# allows for image formats other than gif
from PIL import Image, ImageTk
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen
from Betting import *
ssl._create_default_https_context = ssl._create_unverified_context



if __name__ == "__main__":
    url_agent = "http://121.40.206.168/soft_net/SBDL_NSkt.php?NS=" + "cp_001"
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
    
    

































