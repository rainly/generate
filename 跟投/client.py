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
from wsgiref.simple_server import make_server




ssl._create_default_https_context = ssl._create_unverified_context


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


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [u"hello".encode('utf8')]



# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print ("Serving HTTP on port 8000...")

    

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

#1521852795404
#1521853169130
ticks = time.time()
print ("当前时间戳为:" , ticks)
print ("当前时间戳为:" , ticks * 1000)

        
class ClientThread(threading.Thread):
    def __init__(self, target, thread_num=0, timeout=5.0):
        super(ClientThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout
    def run(self):
        print('Thread start\n')                   
        subthread = threading.Thread(target = self.target_func, args=())
        subthread.setDaemon(True)
        subthread.start()

        while not self.stopped:
            #print("***subthread.join***")
            subthread.join(self.timeout + 1)

        print('Thread stopped'+ "\n")

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped

    def logprint(self, log):
        print(log)
        
    def target_func(self):
        while self.stopped == False:
            time.sleep(5)
            html = ""
            print("############################查询详细##############################") 
            #http://54jndgw.ttx158.com/cp5-5-ag/opadmin/mreport_new_detail.aspx?memberno=tbgd002&gameno=6;8;11;12;13;20;21;22;23;&sdate=2018-03-24&edate=2018-03-24&roundno1=&roundno2=&wagerroundno=&wagertypeno=&onlyself=0&isbupai=&isjs=0&datetime=2018-03-24&curpage=1&ts=1521858951523
            url = self.target.cli_baseurl + "opadmin/mreport_new_detail.aspx?memberno=tbgd002&gameno=6;8;11;12;13;20;21;22;23;&sdate=2018-03-24&edate=2018-03-24&roundno1=&roundno2=&wagerroundno=&wagertypeno=&onlyself=0&isbupai=&isjs=0&datetime=2018-03-24&curpage=1&ts=1521858951523"
            print(url)
            request = urllib.request.Request(url = url, headers = headers, method = 'GET')
            try:
                response = opener.open(request, timeout = 5)
                html = response.read().decode()
            except urllib.error.HTTPError as e:
                print('The server couldn\'t fulfill the request.')
                print('Error code: ' + str(e.code))
                print('Error reason: ' + e.reason)
                print("错误 ==> 网络连接错误！")
                continue
            except urllib.error.URLError as e:
                print('We failed to reach a server.')
                print('Reason: ' + e.reason)
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
            soup = BeautifulSoup(html, "lxml")
            for tr in soup.find_all('tr'):
                if tr.has_attr("class"):
                    continue
                if tr.has_attr("style") == False:
                    continue
                #print(row["style"])
                if tr["style"] != "height: 18px; background-color: #FFFFFF;":
                    continue;
                '''
                编号
                游戏名称
                单号/时间
                账号
                退水率
                投注内容
                赔率
                投注金额
                退水
                结果
                净利
                '''
                for td in tr.find_all('td'):
                    print(td.get_text())
                print("##########################################################")
            
        
        
                

        
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.Close)
        self.cli_initdata()
        self.createWidgets()
            
    def cli_initdata(self):   
        self.cli_thread = None
        #生成config对象
        self.cli_conf = configparser.ConfigParser()
        #用config对象读取配置文件
        self.cli_conf.read("client.txt")

        if self.cli_conf.has_section("name") == True:
            self.cli_name = self.cli_conf.get("name", "value")
        else:
            self.cli_name = ""
            self.cli_conf.add_section("name")
            self.cli_conf.set("name", "value", "")

        if self.cli_conf.has_section("pwd") == True:
            self.cli_pwd = self.cli_conf.get("pwd", "value")
        else:
            self.cli_pwd = ""
            self.cli_conf.add_section("pwd")
            self.cli_conf.set("pwd", "value", "")

        if self.cli_conf.has_section("agent") == True:
            self.cli_agent = self.cli_conf.get("agent", "value")
        else:
            self.cli_agent = ""
            self.cli_conf.add_section("agent")
            self.cli_conf.set("agent", "value", "")
 
        if self.cli_conf.has_section("url") == True:
            self.cli_url = self.cli_conf.get("url", "value")
        else:
            self.cli_url = ""
            self.cli_conf.add_section("url")
            self.cli_conf.set("url", "value", "")

        if self.cli_conf.has_section("wd") == True:
            self.cli_wd = self.cli_conf.get("wd", "value")
        else:
            self.cli_wd = ""
            self.cli_conf.add_section("wd")
            self.cli_conf.set("wd", "value", "")    

    def createWidgets(self):
        # Tab Control introduced here --------------------------------------
        self.cli_tabControl = ttk.Notebook(self)          # Create Tab Control
        self.cli_tab1 = ttk.Frame(self.cli_tabControl)            # Create a tab
        self.cli_tabControl.add(self.cli_tab1, text='第一页')      # Add the tab
        self.cli_tabControl.pack(expand=1, fill="both")  # Pack to make visible
        # ~ Tab Control introduced here
        # -----------------------------------------
        self.ser_createTab()
        
    def ser_createTab(self):
       
        #---------------Tab1控件介绍------------------#
        # Modified Button Click Function  
        # We are creating a container tab3 to hold all other widgets
        self.cli_MyFrame = ttk.LabelFrame(self.cli_tab1, text='操作区')
        self.cli_MyFrame.grid(column=0, row=0, padx=8, pady=4)
        
        # Using a scrolled Text control
        self.cli_scrolW = 80
        self.cli_scrolH = 10
         #行
        line = 0
        # Changing our Label  
        ttk.Label(self.cli_MyFrame, text="地址:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.cli_url = tk.StringVar()  
        self.cli_urlEntered = ttk.Entry(self.cli_MyFrame, width=60, textvariable=self.cli_url)  
        self.cli_urlEntered.grid(column=1, row=line, sticky='W')    

        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.cli_MyFrame, text="登录码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.cli_url = tk.StringVar()  
        self.cli_wdEntered = ttk.Entry(self.cli_MyFrame, width=60, textvariable=self.cli_wd)  
        self.cli_wdEntered.grid(column=1, row=line, sticky='W')

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

        self.cli_btaction = ttk.Button(self.cli_MyFrame,text="刷新",width=10,command=self.cli_flushMe)
        self.cli_btaction.grid(column=1,row=line,sticky='E')

        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.cli_MyFrame, text="查询账号:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.cli_url = tk.StringVar()  
        self.cli_searchEntered = ttk.Entry(self.cli_MyFrame, width=60, textvariable="")  
        self.cli_searchEntered.grid(column=1, row=line, sticky='W')

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

        self.cli_urlEntered.insert(END, "http://93k.zsz585.com/search.aspx")
        self.cli_wdEntered.insert(END, "95712")
        
        self.cli_nameEntered.insert(END, "vf01ha009")
        self.cli_pwdEntered.insert(END, "5134abab")

        
        
    def cli_interMe(self):
        print("################进入网站#######################")
        self.cli_url  = self.cli_urlEntered.get()
        self.cli_wd  = self.cli_wdEntered.get()
        print(self.cli_url)
        print(self.cli_wd)
        url = self.cli_url
        inter_dict = {'wd':self.cli_wd}
        data = urllib.parse.urlencode(inter_dict).encode('utf-8')
        request = urllib.request.Request(url = url, data = data, headers = headers, method = 'POST')
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except Exception as msg:
            print("Exception:%s" % msg)
            return
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
            return
        print(html)
        print("################获取框架地址#######################")
        soup = BeautifulSoup(html, "lxml")
        for row in soup.find_all('iframe'):
            url = row["src"]
        print(url)
        
        print("################获取根地址#######################")
        urls = url.split('?')
        self.cli_baseurl = urls[0]
        print(self.cli_baseurl)

        print("################进入登陆页面#######################")
        #http://54jndgw.ttx158.com/cp5-5-ag/?pagegroup=CP5_5_AG&idcode=64801&rnd=38744&key=E6C257CF128CFFF9ED4A93F61F1312&ts=636574765790000000
        request = urllib.request.Request(url, headers = headers)
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except Exception as msg:
            print("Exception:%s" % msg)
            return
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
            return
        
        print("################保存登录地址#######################")
            
        #保存登录地址
        self.cli_loginurl = url
        self.cli_logindict = {}
        soup = BeautifulSoup(html, "lxml")
        for row in soup.find_all('input'):
            if row.has_attr("name") and row.has_attr("value"):
                self.cli_logindict[row["name"]] = row["value"]
        
        print("################进入网站成功#######################")
        self.cli_flushMe()
        
    def cli_flushMe(self):
        url = self.cli_baseurl + "checknum.aspx"
        print(url)
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
            print('The server couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ' + e.reason)
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
            self.cli_thread = None
            self.cli_btaction.configure(text='开始')
            return

        
        self.cli_name  = self.cli_nameEntered.get()
        self.cli_pwd   = self.cli_pwdEntered.get()
        self.cli_check = self.cli_checkEntered.get()
        self.cli_save()
        if self.cli_name == "":
            messagebox.showinfo("提示","账号不能为空！")
            return

        if self.cli_pwd == "":
            messagebox.showinfo("提示","密码不能为空！")
            return

        if self.cli_check == "":
            messagebox.showinfo("提示","验证码不能为空！")
            return
        
        print("############################账号登陆##############################")
        print(self.cli_loginurl)
        print(self.cli_logindict)
        self.cli_logindict["txt_U_name"]     = self.cli_name
        self.cli_logindict["txt_U_Password"] = self.cli_pwd 
        self.cli_logindict["txt_validate"]   = self.cli_check
        
        data = urllib.parse.urlencode(self.cli_logindict).encode('utf-8')
        request = urllib.request.Request(url = self.cli_loginurl, data = data, headers = headers, method = 'POST')
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except Exception as msg:
            print("Exception:%s" % msg)
            return
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
            return
        print(html)

        login = False
        soup = BeautifulSoup(html, "lxml")
        for row in soup.find_all('h2'):
            if row.get_text().find("用户协议与规则") >= 0:
                login = True;
        if login == False:
            print("错误 ==> 登陆错误！")
            return
        
        print("############################同意登陆##############################")            
        #http://61xudgw.ttx158.com/cp5-5-ag/ch/agreement.aspx/LocationUrl
        ##########################################################
        '''
        agreement_dict = {}
        agreement_dict["stype"] = "1"
        data = urllib.parse.urlencode(agreement_dict).encode('utf-8')
        url = self.cli_baseurl + "ch/agreement.aspx/LocationUrl"
        print(url)
        request = urllib.request.Request(url = url, data = data, headers = headers, method = 'POST')
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
        except Exception as msg:
            print("Exception:%s" % msg)
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
        print(html)
        '''
        print("############################管理界面##############################") 
        #http://54jndgw.ttx158.com/cp5-5-ag/ch/main.aspx
        agreement_dict = {}
        agreement_dict["stype"] = "1"
        data = urllib.parse.urlencode(agreement_dict).encode('utf-8')
        url = self.cli_baseurl + "ch/main.aspx"
        print(url)
        request = urllib.request.Request(url = url, data = data, headers = headers, method = 'POST')
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ' + e.reason)
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

        print("############################下注订单##############################")

        #http://60xxdgw.ttx158.com/cp7-5-mb/ch/left.aspx/GetMemberMtran
        #{wagerround:"D",transtring:"621,,1,,1.94,2;",arrstring:"621:1:2;",wagetype:0,allowcreditquota:4013,hasToken:true,playgametype:0}
        order_dict = {}
        order_dict["wagerround"] = "D"
        order_dict["transtring"] = "621,,1,,1.94,2;"
        order_dict["arrstring"] = "621:1:2;"
        order_dict["wagetype"] = 0
        order_dict["allowcreditquota"] = 4013
        order_dict["hasToken"] = True
        order_dict["playgametype"] = 0
        
        #data = urllib.parse.urlencode(order_dict).encode('utf-8')
        
        url = self.cli_baseurl + "ch/left.aspx/GetMemberMtran"
        print(url)
        #headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
        headers["Content-Type"] = "application/json; charset=UTF-8"
        print(headers)
        
        request = urllib.request.Request(url = url, data = json.dumps(order_dict).encode(encoding='UTF8'), headers = headers, method = 'POST')
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except Exception as msg:
            print("Exception:%s" % msg)
            return
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
            return
        print(html)

        text = json.loads(html)
        spls = text["d"].split('$@')
        token = spls[len(spls) - 1]
        print(token)
        #http://60xxdgw.ttx158.com/cp7-5-mb/ch/left.aspx/mtran_XiaDan_New
        #{gameno:11,wagerroundstring:"D",arrstring:"601:10:2;",roundno:"672724",lianma_transtrin:"",token:"DB046C224A703C88BC5A7AC551C0938C"}
        order_dict = {}
        order_dict["gameno"] = "11"
        order_dict["wagerroundstring"] = "D"
        order_dict["arrstring"] = "601:10:2;"
        order_dict["roundno"] = "672724"
        order_dict["lianma_transtrin"] = ""
        order_dict["token"] = token
        data = urllib.parse.urlencode(order_dict).encode('utf-8')
        url = self.cli_baseurl + "ch/left.aspx/mtran_XiaDan_New"
        print(url)
        
        headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
        headers["Content-Type"] = "application/json; charset=UTF-8"
        request = urllib.request.Request(url = url, data = json.dumps(order_dict).encode(encoding='UTF8'), headers = headers, method = 'POST')
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            print('Error reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ' + e.reason)
            print("错误 ==> 网络连接错误！")
            return
        except Exception as msg:
            print("Exception:%s" % msg)
            return
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
            return
        print(html)
        
        
        
        return
    
        self.cli_btaction.configure(text='关闭')
        self.cli_thread = ClientThread(self)
        self.cli_thread.start()
            
    def cli_save(self):
        #增加新的section
        #
        self.cli_url  = self.cli_urlEntered.get()
        self.cli_wd = self.cli_wdEntered.get()
        
        self.cli_name  = self.cli_nameEntered.get()
        self.cli_pwd = self.cli_pwdEntered.get()
        
        self.cli_conf.set("url", "value", self.cli_url)
        self.cli_conf.set("wd", "value", self.cli_wd)
        self.cli_conf.set("name", "value", self.cli_name)
        self.cli_conf.set("pwd", "value", self.cli_pwd)
        #写回配置文件
        self.cli_conf.write(open("client.txt", "w"))
        #messagebox.showinfo("提示","配置成功！")
        
    def Close(self):
        if self.cli_thread != None:
            messagebox.showinfo("提示","请先关闭自动打码！")
            return
        self.destroy()    
    
def serve_forever():
    # 开始监听HTTP请求:
    httpd.serve_forever()        
        
def main():
    subthread = threading.Thread(target = serve_forever, args=())
    subthread.setDaemon(True)
    subthread.start()
    
    app = Application()
    app.title("梯子游戏 自动打码神器")
    app.resizable(0,0) #阻止Python GUI的大小调整
    # 主消息循环:
    app.mainloop()

if __name__ == "__main__":
    main()
