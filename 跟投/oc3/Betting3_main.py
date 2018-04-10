## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
#梯子游戏
    
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
import pymysql.cursors
import ssl
#import sqlite3
import configparser
import random

from bs4 import BeautifulSoup  # 引入beautifulsoup 解析html事半功倍
from collections import deque
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.common.exceptions import *
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

ssl._create_default_https_context = ssl._create_unverified_context
from Betting3 import *




def RegKey():
    url_agent = "http://duboren.com/ccskey/query?regkey=2286738abd0e8e12c8feb3327cc5aad8"
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


































