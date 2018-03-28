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
import pymysql.cursors
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

try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen

import io
# allows for image formats other than gif
from PIL import Image, ImageTk

ssl._create_default_https_context = ssl._create_unverified_context



##加载配置文件
file_object = open('oc.js', encoding= 'utf8')
try:
    all_the_text = file_object.read( )
finally:
    file_object.close( )
if all_the_text.startswith(u'\ufeff'):
    all_the_text = all_the_text.encode('utf8')[3:].decode('utf8')
all_the_oc = json.loads(all_the_text)

##获取游戏类型
def gettype(gname, glv):
    for key in all_the_oc["game_type"]:
        if all_the_oc["game_type"][key] == gname and all_the_oc["game_lv"][key] == glv:
            return key
    return ""
    
print(gettype("庄家", 2))








#def application(environ, start_response):
#    start_response('200 OK', [('Content-Type', 'text/html')])
#    return [u"hello".encode('utf8')]
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
#httpd = make_Betting('', 8000, application)
#print ("Serving HTTP on port 8000...")


g_mutex = threading.Lock()
g_datas = []

    

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

#64801
#print (datetime.datetime.now().strftime('%Y-%m-%d'))   #日期格式化

#t = time.time()
#print(str(int(round(t))))



        
class ServerThread(threading.Thread):
    def __init__(self, target, thread_num=0, timeout=5.0):
        super(ServerThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout
    def run(self):
        print('Thread start\n')                   
        self.target_func()
        print('Thread stopped'+ "\n")

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped

    def logprint(self, log):
        print(log)
        
    def target_func(self):
        print("target_func begin")
        sleepnum = 5
        while self.stopped == False:
            sleepnum = sleepnum + 1
            if sleepnum < 5:
                time.sleep(1)
                continue
            sleepnum = 0
            
            g_mutex.acquire()
            g_datas.clear()
            g_mutex.release()
            
            for user in self.target.users:
                if self.stopped:
                    break
                print("############################查询详细##############################" + user) 
                #https://00271596-xsj.cp168.ws/agent/report/bets?username=zhw999&lottery=BJPK10%2CCQSSC%2CPK10JSC%2CLUCKYSB%2CSSCJSC%2CGDKLSF%2CGXK3%2CXYNC%2CKL8%2CXJSSC%2CTJSSC%2CBJPK10BJL%2CGXKLSF%2CGD11X5%2CPCEGG%2CAULUCKY20%2CAULUCKY10%2CAULUCKY5%2CAULUCKY8%2CHK6&begin=2018-03-25&end=2018-03-25&settle=false
                t = time.time()
                url = self.target.ser_url + "agent/report/bets?username=" + user + "&lottery=BJPK10%2CCQSSC%2CPK10JSC%2CLUCKYSB%2CSSCJSC%2CGDKLSF%2CGXK3%2CXYNC%2CKL8%2CXJSSC%2CTJSSC%2CBJPK10BJL%2CGXKLSF%2CGD11X5%2CPCEGG%2CAULUCKY20%2CAULUCKY10%2CAULUCKY5%2CAULUCKY8%2CHK6&begin=" + datetime.datetime.now().strftime('%Y-%m-%d') + "&end=" + datetime.datetime.now().strftime('%Y-%m-%d') + "&settle=false"
                #url = self.target.ser_url + "agent/report/bets?username=zhw999&lottery=BJPK10%2CCQSSC%2CPK10JSC%2CLUCKYSB%2CSSCJSC%2CGDKLSF%2CGXK3%2CXYNC%2CKL8%2CXJSSC%2CTJSSC%2CBJPK10BJL%2CGXKLSF%2CGD11X5%2CPCEGG%2CAULUCKY20%2CAULUCKY10%2CAULUCKY5%2CAULUCKY8%2CHK6&begin=2018-03-25&end=2018-03-25&settle=true"
                #print(url)
                request = urllib.request.Request(url = url, headers = headers, method = 'GET')
                try:
                    response = opener.open(request, timeout = 5)
                    html = response.read().decode()
                except urllib.error.HTTPError as e:
                    print('The Betting couldn\'t fulfill the request.')
                    print('Error code: ' + str(e.code))
                    #print('Error reason: ' + e.reason)
                    print("错误 ==> 网络连接错误！")
                    continue
                except urllib.error.URLError as e:
                    print('We failed to reach a Betting.')
                    #print('Reason: ' + e.reason)
                    print("错误 ==> 网络连接错误！")
                    continue
                except Exception as msg:
                    print("Exception:%s" % msg)
                    continue
                except:
                    #print("error lineno:" + str(sys._getframe().f_lineno))
                    print("错误 ==> 网络连接错误！")
                    continue
                #print(html)
                g_mutex.acquire()
                soup = BeautifulSoup(html, "lxml")
                for tbody in soup.find_all('tbody'):
                    for tr in tbody.find_all('tr'):
                        data = []
                        for td in tr.find_all('td'):
                            data.append(td.get_text())
                        g_datas.append(data)
                g_mutex.release()
                
            print("注单号    投注时间    投注种类    账号    投注内容    下注金额    退水(%)    下注结果    本级占成    本级结果    占成明细")
            for item in g_datas:
                print(item[0].strip() + " " + item[1].strip() + " " + item[2].strip() + " " + item[3].strip() + " " + item[4].strip() + " " +  item[5].strip() + " " + item[6].strip() + " " + item[7].strip() + " " + item[8].strip() + " " + item[9].strip() + " " + item[10].strip())
        print("target_func end")
                
                
       
class ClientThread(threading.Thread):
    def __init__(self, target, thread_num=0, timeout=5.0):
        super(ClientThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout
    def run(self):
        print('Thread start\n')                   
        self.target_func()
        print('Thread stopped'+ "\n")

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped

    def logprint(self, log):
        print(log)


    def target_func(self):
        g_order_dict = {}
        sleepnum = 5
        while self.stopped == False:
            sleepnum = sleepnum + 1
            if sleepnum < 5:
                time.sleep(1)
                continue
            sleepnum = 0     

            print("############################查询倍率##############################")
            t = time.time()
            #https://3661032706-xsj.cp168.ws/member/odds?lottery=BJPK10BJL&_=1522070776784
            #{"DX_D":1.5,"DX_X":2.5,"LB_X_4":7,"LB_X_6":31,"LB_X":2,"LB_Z_3":5,"LB_X_3":5,"LB_Z_2":3,"LB_Z_4":7,"LB_Z_5":11,"LB_Z_6":31,"LB_Z_1":2,"LB_X_1":2,"LB_Z":2,"LB_X_5":11,"LB_X_2":3,"T_T":8,"XD_XD":12,"ZD_ZD":12,"ZX_Z":1.95,"ZX_X":2,"ZX1_Z":2,"ZX1_X":2}
           
            url = self.target.cli_url + "member/odds?lottery=BJPK10BJL&_=" + str(int(round(t * 1000)))
            #print(url)    
            request = urllib.request.Request(url = url, headers = headers, method = 'GET')
            try:
                response = opener.open(request, timeout = 5)
                html = response.read().decode()
            except urllib.error.HTTPError as e:
                print('The Betting couldn\'t fulfill the request.')
                print('Error code: ' + str(e.code))
                #print('Error reason: ' + e.reason)
                print("错误 ==> 网络连接错误！")
                continue
            except urllib.error.URLError as e:
                print('We failed to reach a Betting.')
                #print('Reason: ' + e.reason)
                print("错误 ==> 网络连接错误！")
                continue
            except Exception as msg:
                print("Exception:%s" % msg)
                continue
            except:
                #print("error lineno:" + str(sys._getframe().f_lineno))
                print("错误 ==> 网络连接错误！")
                continue          
            try:
                #print(html)
                game_lv = json.loads(html)  
                all_the_oc["game_lv"] = game_lv                
            except:
                pass
                
            print("############################查询倍率成功##############################")
            g_mutex.acquire()
            for item in g_datas:
                if self.stopped:
                    break
                '''    
                注单号    
                投注时间    
                投注种类    "彩票百家乐673155-1期"
                账号    
                投注内容    
                下注金额    
                退水(%)    
                下注结果    
                本级占成    
                本级结果    
                占成明细
                '''
                #print(item)
                #['4399421039# ', '2018-03-26 21:28:06 星期一', '彩票百家乐673156-1期', 'qqww110A盘', '小 @ 2.5\n', '2200', '0.5%', '-2189.0', '0%', '11.0', '明细']
                print("############################下注订单##############################")
                print(item)
                
                username = item[3]
                username = username.replace("A盘", "")
                username = username.replace("B盘", "")
                username = username.replace("C盘", "")
                username = username.replace("D盘", "")
                username = username.replace("E盘", "")
                username = username.replace("F盘", "")
                username = username.replace("G盘", "")
                
                bUser = False
                for key in self.target.users:
                    if username == key:
                        bUser = True
                    
                if bUser == False:
                    print("****账号没有找到****" + username)
                    continue
    
                if item[0] in g_order_dict:
                    print("****订单已经处理*****" + item[0])
                    continue
                g_order_dict[item[0]] = 1

                amount = round(float(item[5]) * float(self.target.users[username]))
                #amount =10
                
                drawNumber = item[2]
                if drawNumber.find("彩票百家乐") == -1:
                    print("****不是彩票百家乐订单*****")
                    continue
                drawNumber = drawNumber.replace("彩票百家乐", "")
                drawNumber = drawNumber.replace("期", "")
                order_dict = {}
                order_dict["lottery"] = "BJPK10BJL"
                order_dict["ignore"] = False
                order_dict["drawNumber"] = drawNumber
                order_dict["bets"] = []

                #小 @ 2.5\n
                _split  = item[4].split("@")
                #print(_split)
                _odds           = _split[1]
                _odds           = _odds.replace("\n", "")
                _odds           = _odds.strip()
                _odds            = float(_odds)
                #小
                _type = gettype(_split[0].strip(), _odds)
                #print(_type)
                #DX_D
                _split2 = _type.split("_")
                
                bet = {}
                bet["game"]     = _split2[0]
                bet["contents"] = _split2[1]
                bet["amount"]   = amount
                bet["odds"]     = _odds
                order_dict["bets"].append(bet)
                print(order_dict)
                
                data = json.dumps(order_dict).encode(encoding='UTF8')  
                url = self.target.cli_url + "member/bet"
                
                headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
                headers["Content-Type"] = "application/json; charset=UTF-8"
                print(url)
                request = urllib.request.Request(url = url, data = data, headers = headers, method = 'POST')
                try:
                    response = opener.open(request, timeout = 5)
                    html = response.read().decode()
                except urllib.error.HTTPError as e:
                    print('The Betting couldn\'t fulfill the request.')
                    print('Error code: ' + str(e.code))
                    #print('Error reason: ' + e.reason)
                    print("错误 ==> 网络连接错误！")
                    continue
                except urllib.error.URLError as e:
                    print('We failed to reach a Betting.')
                    #print('Reason: ' + e.reason)
                    print("错误 ==> 网络连接错误！")
                    continue
                except Exception as msg:
                    print("Exception:%s" % msg)
                    continue
                except:
                    #print("error lineno:" + str(sys._getframe().f_lineno))
                    print("错误 ==> 网络连接错误！")
                    continue
                print(html)
                #{"account":{"balance":20.706,"betting":10,"maxLimit":80.3,"result":-49.594,"type":0,"userid":"xsj88-cs0990"},"ids":["4401781315"],"odds":["2,2,3,5,7,11,31"],"status":0}
                try:
                    result = json.loads(html)  
                    if result["status"] == 0:
                        print("****跟单成功****")
                    else:
                        print("****跟单失败****")
                except:
                    print("****跟单失败****")
            
            ###############################
            g_mutex.release()
 

 
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.Close)
        
        #生成config对象
        self.conf = configparser.ConfigParser()
        #用config对象读取配置文件
        self.conf.read("Betting.txt")    
        
        if self.conf.has_section("agent") == True:
            self.agent = self.conf.get("agent", "value")
        else:
            self.agent = ""
            self.conf.add_section("agent")
            self.conf.set("agent", "value", "")

        if self.conf.has_section("searchText") == True:
            self.searchText = self.conf.get("searchText", "value")
        else:
            self.searchText = ""
            self.conf.add_section("searchText")
            self.conf.set("searchText", "value", "")
            
        
        self.ser_initdata()
        self.cli_initdata()
        self.createWidgets()
        
    def createWidgets(self):
        # Tab Control introduced here --------------------------------------
        self.tabControl = ttk.Notebook(self)          # Create Tab Control
        self.ser_tab  = ttk.Frame(self.tabControl)            # Create a tab
        self.tabControl.add(self.ser_tab, text='**采集**')      # Add the tab
        self.tabControl.pack(expand=1, fill="both")  # Pack to make visible
        
        self.cli_tab = ttk.Frame(self.tabControl)            # Create a tab
        self.tabControl.add(self.cli_tab, text='**下注**')      # Add the tab
        self.tabControl.pack(expand=1, fill="both")  # Pack to make visible
        
        self.conf_tab = ttk.Frame(self.tabControl)            # Create a tab
        self.tabControl.add(self.conf_tab, text='**配置**')      # Add the tab
        self.tabControl.pack(expand=1, fill="both")  # Pack to make visible
        
        # ~ Tab Control introduced here
        # -----------------------------------------
        self.ser_createTab()    
        self.cli_createTab()    
        
        #---------------ser_tab控件介绍------------------#
        # Modified Button Click Function  
        # We are creating a container tab3 to hold all other widgets
        self.conf_MyFrame = ttk.LabelFrame(self.conf_tab, text='操作区(名字*赔率)')
        self.conf_MyFrame.grid(column=0, row=0, padx=8, pady=4)
        
        # Using a scrolled Text control
        self.scrolW = 65
        self.scrolH = 20
        #行
        line = 0
        # Changing our Label  
        ttk.Label(self.conf_MyFrame, text="查询账号:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.ser_url = tk.StringVar()  
        self.searchScrolledText = scrolledtext.ScrolledText(self.conf_MyFrame, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.searchScrolledText.grid(column=0, row=line, sticky='WE', columnspan=3)    
        self.searchScrolledText.insert(tk.INSERT, self.searchText)        
          
    def ser_initdata(self):
        self.ser_thread = None

        if self.conf.has_section("ser_name") == True:
            self.ser_name = self.conf.get("ser_name", "value")
        else:
            self.ser_name = ""
            self.conf.add_section("ser_name")
            self.conf.set("ser_name", "value", "")

        if self.conf.has_section("ser_pwd") == True:
            self.ser_pwd = self.conf.get("ser_pwd", "value")
        else:
            self.ser_pwd = ""
            self.conf.add_section("ser_pwd")
            self.conf.set("ser_pwd", "value", "")
            
        if self.conf.has_section("ser_url") == True:
            self.ser_url = self.conf.get("ser_url", "value")
        else:
            self.ser_url = ""
            self.conf.add_section("ser_url")
            self.conf.set("ser_url", "value", "")

        if self.conf.has_section("ser_wd") == True:
            self.ser_wd = self.conf.get("ser_wd", "value")
        else:
            self.ser_wd = ""
            self.conf.add_section("ser_wd")
            self.conf.set("ser_wd", "value", "")    
            
    def ser_createTab(self):
       
        #---------------ser_tab控件介绍------------------#
        # Modified Button Click Function  
        # We are creating a container tab3 to hold all other widgets
        self.ser_MyFrame = ttk.LabelFrame(self.ser_tab, text='操作区')
        self.ser_MyFrame.grid(column=0, row=0, padx=8, pady=4)
         #行
        line = 0
        # Changing our Label  
        ttk.Label(self.ser_MyFrame, text="地址:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.ser_url = tk.StringVar()  
        self.ser_urlEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable=self.ser_url)  
        self.ser_urlEntered.grid(column=1, row=line, sticky='W')    

        #行
        #line = line + 1
        # Changing our Label  
        #ttk.Label(self.ser_MyFrame, text="登录码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.ser_url = tk.StringVar()  
        #self.ser_wdEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable=self.ser_wd)  
        #self.ser_wdEntered.grid(column=1, row=line, sticky='W')

         # Adding a Button
        line = line + 1
        self.ser_btaction = ttk.Button(self.ser_MyFrame,text="进入",width=10,command=self.ser_interMe)
        self.ser_btaction.grid(column=1,row=line,sticky='E')   
    
        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.ser_MyFrame, text="账号:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.ser_url = tk.StringVar()  
        self.ser_nameEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable=self.ser_name)  
        self.ser_nameEntered.grid(column=1, row=line, sticky='W')
        
        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.ser_MyFrame, text="密码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.ser_url = tk.StringVar()  
        self.ser_pwdEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable=self.ser_pwd)  
        self.ser_pwdEntered.grid(column=1, row=line, sticky='W')  

        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.ser_MyFrame, text="验证码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.ser_url = tk.StringVar()  
        self.ser_checkEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable="")  
        self.ser_checkEntered.grid(column=1, row=line, sticky='W')

        #行
        line = line + 1
        self.ser_label = tk.Label(self.ser_MyFrame, bg='brown')
        self.ser_label.grid(column=0,row=line,sticky='W')

        self.ser_btaction = ttk.Button(self.ser_MyFrame,text="刷新",width=10,command=self.ser_interMe)
        self.ser_btaction.grid(column=1,row=line,sticky='E')

         # Adding a Button
        line = line + 1
        self.ser_btaction = ttk.Button(self.ser_MyFrame,text="开始",width=10,command=self.ser_clickMe)
        self.ser_btaction.grid(column=1,row=line,sticky='E')       
        
        
        # 一次性控制各控件之间的距离
        for child in self.ser_MyFrame.winfo_children(): 
            child.grid_configure(padx=3,pady=1)
        # 单独控制个别控件之间的距离
        #self.ser_btaction.grid(column=2,row=1,rowspan=2,padx=6)
        #---------------ser_tab控件介绍------------------#

        self.ser_urlEntered.insert(END, self.ser_url)
        #self.ser_wdEntered.insert(END, self.ser_wd)
        
        self.ser_nameEntered.insert(END, self.ser_name)
        self.ser_pwdEntered.insert(END, self.ser_pwd)
   
    def ser_interMe(self):
        print("################进入代理网站#######################")
        self.ser_url  = self.ser_urlEntered.get()
        #self.ser_wd  = self.ser_wdEntered.get()
        url = self.ser_url
        print("################进入登陆页面#######################")
        #http://54jndgw.ttx158.com/cp5-5-ag/?pagegroup=CP5_5_AG&idcode=64801&rnd=38744&key=E6C257CF128CFFF9ED4A93F61F1312&ts=636574765790000000
        #print(url)
        request = urllib.request.Request(url, headers = headers)
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The Betting couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            #print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except urllib.error.URLError as e:
            print('We failed to reach a Betting.')
            #print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except Exception as msg:
            print("Exception:%s" % msg)
            return
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
            return
        print("################进入代理网站成功#######################")

        self.ser_flushMe()
        
    def ser_flushMe(self):
        url = self.ser_url + "code"
        #print(url)
        request = urllib.request.Request(url, headers = headers)
        try:
            response = opener.open(request, timeout = 5)
            self.ser_image_bytes = response.read()
            # internal data file
            self.ser_data_stream = io.BytesIO(self.ser_image_bytes)
            # open as a PIL image object
            self.ser_pil_image = Image.open(self.ser_data_stream)
            self.ser_tk_image = ImageTk.PhotoImage(self.ser_pil_image)
            self.ser_label["image"] = self.ser_tk_image
        except urllib.error.HTTPError as e:
            print('The Betting couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            #print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
        except urllib.error.URLError as e:
            print('We failed to reach a Betting.')
            #print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
        except Exception as msg:
            print("Exception:%s" % msg)
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")

    def ser_clickMe(self):

        text = self.ser_btaction.config('text')
        if  text[4] == '关闭':
            if self.ser_thread.is_alive():
                self.ser_thread.stop()
                self.ser_thread.join()
            self.ser_thread = None
            self.ser_btaction.configure(text='开始')
            return
                     
        self.ser_name  = self.ser_nameEntered.get()
        self.ser_pwd   = self.ser_pwdEntered.get()
        self.ser_check = self.ser_checkEntered.get()
        self.searchText = self.searchScrolledText.get(1.0, END)
        if self.ser_name == "":
            messagebox.showinfo("提示","账号不能为空！")
            return

        if self.ser_pwd == "":
            messagebox.showinfo("提示","密码不能为空！")
            return

        if self.ser_check == "":
            messagebox.showinfo("提示","验证码不能为空！")
            return
            
        if self.searchText == "":
            messagebox.showinfo("提示","账号查询不能为空！")
            return
            
        self.users = {}
        searchTexts = self.searchText.split("\n")
        for item in searchTexts:
            if item  == "":
                continue
            item  = item.replace("\n", "")
            user  = item.split("*")
            if len(user) < 2:
                messagebox.showinfo("提示","账号查询格式不正确！")
                return                
            self.users[user[0]] = user[1]
        print(self.users)

        self.ser_save()  
        print("############################账号登陆##############################")
        logindict = {}
        logindict["type"]     = 2
        logindict["account"]     = self.ser_name
        logindict["password"] = self.ser_pwd 
        logindict["code"]   = self.ser_check
        
        data = urllib.parse.urlencode(logindict).encode('utf-8')

        url = self.ser_url + "login"
        #print(url)       
        request = urllib.request.Request(url = url, data = data, headers = headers, method = 'POST')
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The Betting couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            #print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except urllib.error.URLError as e:
            print('We failed to reach a Betting.')
            #print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except Exception as msg:
            print("Exception:%s" % msg)
            return
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
            return
        #print(html)

        login = False
        soup = BeautifulSoup(html, "lxml")
        for row in soup.find_all('title'):
            if row.get_text().find("") >= 0:
                login = True
        if login == False:
            print("错误 ==> 登陆错误！")
            return
        
        self.ser_btaction.configure(text='关闭')
        self.ser_thread = ServerThread(self)
        self.ser_thread.start()
            
    def ser_save(self):
        #增加新的section
        #
        self.ser_url  = self.ser_urlEntered.get()
        #self.ser_wd = self.ser_wdEntered.get()
        self.ser_name  = self.ser_nameEntered.get()
        self.ser_pwd = self.ser_pwdEntered.get()
        self.searchText = self.searchScrolledText.get(1.0, END)
        self.conf.set("searchText", "value", self.searchText)      
        self.conf.set("ser_url", "value", self.ser_url)
        self.conf.set("ser_wd", "value", self.ser_wd)
        self.conf.set("ser_name", "value", self.ser_name)
        self.conf.set("ser_pwd", "value", self.ser_pwd)
        #写回配置文件
        self.conf.write(open("Betting.txt", "w"))
        #messagebox.showinfo("提示","配置成功！")
    
    ############################
    def cli_initdata(self):   
        self.cli_thread = None
        
        if self.conf.has_section("cli_name") == True:
            self.cli_name = self.conf.get("cli_name", "value")
        else:
            self.cli_name = ""
            self.conf.add_section("cli_name")
            self.conf.set("cli_name", "value", "")

        if self.conf.has_section("cli_pwd") == True:
            self.cli_pwd = self.conf.get("cli_pwd", "value")
        else:
            self.cli_pwd = ""
            self.conf.add_section("cli_pwd")
            self.conf.set("cli_pwd", "value", "")
            
        if self.conf.has_section("cli_url") == True:
            self.cli_url = self.conf.get("cli_url", "value")
        else:
            self.cli_url = ""
            self.conf.add_section("cli_url")
            self.conf.set("cli_url", "value", "")

        if self.conf.has_section("cli_wd") == True:
            self.cli_wd = self.conf.get("cli_wd", "value")
        else:
            self.cli_wd = ""
            self.conf.add_section("cli_wd")
            self.conf.set("cli_wd", "value", "")  

    def cli_createTab(self):
        #---------------Tab1控件介绍------------------#
        # Modified Button Click Function  
        # We are creating a container tab3 to hold all other widgets
        self.cli_MyFrame = ttk.LabelFrame(self.cli_tab, text='操作区')
        self.cli_MyFrame.grid(column=0, row=0, padx=8, pady=4)
         #行
        line = 0
        # Changing our Label  
        ttk.Label(self.cli_MyFrame, text="地址:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.cli_url = tk.StringVar()  
        self.cli_urlEntered = ttk.Entry(self.cli_MyFrame, width=60, textvariable=self.cli_url)  
        self.cli_urlEntered.grid(column=1, row=line, sticky='W')    

        #行
        #line = line + 1
        # Changing our Label  
        #ttk.Label(self.cli_MyFrame, text="登录码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.cli_url = tk.StringVar()  
        #self.cli_wdEntered = ttk.Entry(self.cli_MyFrame, width=60, textvariable=self.cli_wd)  
        #self.cli_wdEntered.grid(column=1, row=line, sticky='W')

         # Adding a Button
        line = line + 1
        self.cli_btaction = ttk.Button(self.cli_MyFrame,text="进入",width=10,command=self.cli_interMe)
        self.cli_btaction.grid(column=1,row=line,sticky='E')   
    
        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.cli_MyFrame, text="账号:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.cli_url = tk.StringVar()  
        self.cli_nameEntered = ttk.Entry(self.cli_MyFrame, width=60, textvariable=self.cli_name)  
        self.cli_nameEntered.grid(column=1, row=line, sticky='W')
        
        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.cli_MyFrame, text="密码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.cli_url = tk.StringVar()  
        self.cli_pwdEntered = ttk.Entry(self.cli_MyFrame, width=60, textvariable=self.cli_pwd)  
        self.cli_pwdEntered.grid(column=1, row=line, sticky='W')  

        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.cli_MyFrame, text="验证码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.cli_url = tk.StringVar()  
        self.cli_checkEntered = ttk.Entry(self.cli_MyFrame, width=60, textvariable="")  
        self.cli_checkEntered.grid(column=1, row=line, sticky='W')

        #行
        line = line + 1
        self.cli_label = tk.Label(self.cli_MyFrame, bg='brown')
        self.cli_label.grid(column=0,row=line,sticky='W')

        self.cli_btaction = ttk.Button(self.cli_MyFrame,text="刷新",width=10,command=self.cli_interMe)
        self.cli_btaction.grid(column=1,row=line,sticky='E')
        
         # Adding a Button
        line = line + 1
        self.cli_btaction = ttk.Button(self.cli_MyFrame,text="开始",width=10,command=self.cli_clickMe)
        self.cli_btaction.grid(column=1,row=line,sticky='E')       
        
        
        # 一次性控制各控件之间的距离
        for child in self.cli_MyFrame.winfo_children(): 
            child.grid_configure(padx=3,pady=1)
        # 单独控制个别控件之间的距离
        #self.cli_btaction.grid(column=2,row=1,rowspan=2,padx=6)
        #---------------Tab1控件介绍------------------#

        self.cli_urlEntered.insert(END, self.cli_url)
        #self.cli_wdEntered.insert(END, self.cli_wd)
        self.cli_nameEntered.insert(END, self.cli_name)
        self.cli_pwdEntered.insert(END, self.cli_pwd)
            
    def cli_interMe(self):
        print("################进入会员网站#######################")
        self.cli_url  = self.cli_urlEntered.get()
        #self.cli_wd  = self.cli_wdEntered.get()
        url = self.cli_url
        print("################进入会员登陆页面#######################")
        #print(url)
        request = urllib.request.Request(url, headers = headers)
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The Betting couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            #print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except urllib.error.URLError as e:
            print('We failed to reach a Betting.')
            #print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except Exception as msg:
            print("Exception:%s" % msg)
            return
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
            return
        print("################进入会员网站成功#######################")

        self.cli_flushMe()
        
    def cli_flushMe(self):
        url = self.cli_url + "code"
        #print(url)
        request = urllib.request.Request(url, headers = headers)
        try:
            response = opener.open(request, timeout = 5)
            self.cli_image_bytes = response.read()
            # internal data file
            self.cli_data_stream = io.BytesIO(self.cli_image_bytes)
            # open as a PIL image object
            self.cli_pil_image = Image.open(self.cli_data_stream)
            self.cli_tk_image = ImageTk.PhotoImage(self.cli_pil_image)
            self.cli_label["image"] = self.cli_tk_image
        except urllib.error.HTTPError as e:
            print('The Betting couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            #print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
        except urllib.error.URLError as e:
            print('We failed to reach a Betting.')
            #print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
        except Exception as msg:
            print("Exception:%s" % msg)
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
   
    def cli_clickMe(self):
        text = self.cli_btaction.config('text')
        if  text[4] == '关闭':
            if self.cli_thread.is_alive():
                self.cli_thread.stop()
                self.cli_thread.join()
            self.cli_thread = None
            self.cli_btaction.configure(text='开始')
            return
                     
        self.cli_name  = self.cli_nameEntered.get()
        self.cli_pwd   = self.cli_pwdEntered.get()
        self.cli_check = self.cli_checkEntered.get()
        self.searchText = self.searchScrolledText.get(1.0, END)
        if self.cli_name == "":
            messagebox.showinfo("提示","账号不能为空！")
            return

        if self.cli_pwd == "":
            messagebox.showinfo("提示","密码不能为空！")
            return

        if self.cli_check == "":
            messagebox.showinfo("提示","验证码不能为空！")
            return
            
        if self.searchText == "":
            messagebox.showinfo("提示","账号查询不能为空！")
            return
            
        self.users = {}
        searchTexts = self.searchText.split("\n")
        for item in searchTexts:
            if item  == "":
                continue
            item  = item.replace("\n", "")
            user  = item.split("*")
            if len(user) < 2:
                messagebox.showinfo("提示","账号查询格式不正确！")
                return                
            self.users[user[0]] = user[1]

        self.cli_save()  
        print("############################账号登陆##############################")
        logindict = {}
        logindict["type"]     = 2
        logindict["account"]     = self.cli_name
        logindict["password"] = self.cli_pwd 
        logindict["code"]   = self.cli_check
        
        data = urllib.parse.urlencode(logindict).encode('utf-8')
        print(data)

        url = self.cli_url + "login"
        #print(url)        
        request = urllib.request.Request(url = url, data = data, headers = headers, method = 'POST')
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The Betting couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            #print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except urllib.error.URLError as e:
            print('We failed to reach a Betting.')
            #print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except Exception as msg:
            print("Exception:%s" % msg)
            return
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
            return
        #print(html)

        login = False
        soup = BeautifulSoup(html, "lxml")
        for row in soup.find_all('li'):
            if row.get_text().find("用户协议") >= 0:
                login = True
        if login == False:
            print("错误 ==> 登陆错误！")
            return
        print("登录 ==> 登陆成功！")
        
        print("############################同意登录##############################")
        #https://3661032706-xsj.cp168.ws/member/index
        url = self.cli_url + "member/index"
        #print(url)   
        request = urllib.request.Request(url = url, headers = headers, method = 'GET')
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The Betting couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            #print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except urllib.error.URLError as e:
            print('We failed to reach a Betting.')
            #print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except Exception as msg:
            print("Exception:%s" % msg)
            return
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
            return
        #print(html)
        
        self.cli_btaction.configure(text='关闭')
        self.cli_thread = ClientThread(self)
        self.cli_thread.start()
            
    def cli_save(self):
        #增加新的section
        #
        self.cli_url  = self.cli_urlEntered.get()
        #self.cli_wd = self.cli_wdEntered.get()
        
        self.cli_name  = self.cli_nameEntered.get()
        self.cli_pwd = self.cli_pwdEntered.get()
        
        self.conf.set("cli_url", "value", self.cli_url)
        self.conf.set("cli_wd", "value", self.cli_wd)
        self.conf.set("cli_name", "value", self.cli_name)
        self.conf.set("cli_pwd", "value", self.cli_pwd)
        #写回配置文件
        self.conf.write(open("Betting.txt", "w"))
        #messagebox.showinfo("提示","配置成功！")
            
    def Close(self):
        if self.ser_thread != None and self.ser_thread.is_alive():
            self.ser_thread.stop()
            self.ser_thread.join()
            self.ser_thread = None
    
        if self.cli_thread != None and self.cli_thread.is_alive():
            self.cli_thread.stop()
            self.cli_thread.join()
            self.cli_thread = None
        
        self.destroy()    
    
    
        
def main():

    
    app = Application()
    app.title("跟投 自动打码神器")
    app.resizable(0,0) #阻止Python GUI的大小调整
    # 主消息循环:
    app.mainloop()

if __name__ == "__main__":
    main()
