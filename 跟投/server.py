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

        
class ServerThread(threading.Thread):
    def __init__(self, target, thread_num=0, timeout=5.0):
        super(ServerThread, self).__init__()
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
            url = self.target.ser_baseurl + "opadmin/mreport_new_detail.aspx?memberno=tbgd002&gameno=6;8;11;12;13;20;21;22;23;&sdate=2018-03-24&edate=2018-03-24&roundno1=&roundno2=&wagerroundno=&wagertypeno=&onlyself=0&isbupai=&isjs=0&datetime=2018-03-24&curpage=1&ts=1521858951523"
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
        
        self.ser_initdata()
        self.createWidgets()
        
    def ser_initdata(self):
        self.ser_thread = None
        #生成config对象
        self.ser_conf = configparser.ConfigParser()
        #用config对象读取配置文件
        self.ser_conf.read("server.txt")

        if self.ser_conf.has_section("name") == True:
            self.ser_name = self.ser_conf.get("name", "value")
        else:
            self.ser_name = ""
            self.ser_conf.add_section("name")
            self.ser_conf.set("name", "value", "")

        if self.ser_conf.has_section("pwd") == True:
            self.ser_pwd = self.ser_conf.get("pwd", "value")
        else:
            self.ser_pwd = ""
            self.ser_conf.add_section("pwd")
            self.ser_conf.set("pwd", "value", "")

        if self.ser_conf.has_section("agent") == True:
            self.ser_agent = self.ser_conf.get("agent", "value")
        else:
            self.ser_agent = ""
            self.ser_conf.add_section("agent")
            self.ser_conf.set("agent", "value", "")
 
        if self.ser_conf.has_section("url") == True:
            self.ser_url = self.ser_conf.get("url", "value")
        else:
            self.ser_url = ""
            self.ser_conf.add_section("url")
            self.ser_conf.set("url", "value", "")

        if self.ser_conf.has_section("wd") == True:
            self.ser_wd = self.ser_conf.get("wd", "value")
        else:
            self.ser_wd = ""
            self.ser_conf.add_section("wd")
            self.ser_conf.set("wd", "value", "")    
        
       

    def createWidgets(self):
        # Tab Control introduced here --------------------------------------
        self.tabControl = ttk.Notebook(self)          # Create Tab Control
        self.ser_tab  = ttk.Frame(self.tabControl)            # Create a tab
        self.tabControl.add(self.ser_tab, text='**采集**')      # Add the tab
        self.tabControl.pack(expand=1, fill="both")  # Pack to make visible
        
        self.tab2 = ttk.Frame(self.tabControl)            # Create a tab
        self.tabControl.add(self.tab2, text='**下注**')      # Add the tab
        self.tabControl.pack(expand=1, fill="both")  # Pack to make visible
        # ~ Tab Control introduced here
        # -----------------------------------------
        self.ser_createTab()
            
    def ser_createTab(self):
       
        #---------------ser_tab控件介绍------------------#
        # Modified Button Click Function  
        # We are creating a container tab3 to hold all other widgets
        self.ser_MyFrame = ttk.LabelFrame(self.ser_tab, text='操作区')
        self.ser_MyFrame.grid(column=0, row=0, padx=8, pady=4)
        
        # Using a scrolled Text control
        self.ser_scrolW = 80
        self.ser_scrolH = 10
         #行
        line = 0
        # Changing our Label  
        ttk.Label(self.ser_MyFrame, text="地址:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.ser_url = tk.StringVar()  
        self.ser_urlEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable=self.ser_url)  
        self.ser_urlEntered.grid(column=1, row=line, sticky='W')    

        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.ser_MyFrame, text="登录码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.ser_url = tk.StringVar()  
        self.ser_wdEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable=self.ser_wd)  
        self.ser_wdEntered.grid(column=1, row=line, sticky='W')

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

        self.ser_btaction = ttk.Button(self.ser_MyFrame,text="刷新",width=10,command=self.ser_flushMe)
        self.ser_btaction.grid(column=1,row=line,sticky='E')

        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.ser_MyFrame, text="查询账号:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        # self.ser_url = tk.StringVar()  
        self.ser_searchEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable="")  
        self.ser_searchEntered.grid(column=1, row=line, sticky='W')

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

        self.ser_urlEntered.insert(END, "http://77t.snk686.com/search.aspx")
        self.ser_wdEntered.insert(END, "64801")
        
        self.ser_nameEntered.insert(END, "tbcs111")
        self.ser_pwdEntered.insert(END, "5134abab")

        
        
    def ser_interMe(self):
        print("################进入网站#######################")
        self.ser_url  = self.ser_urlEntered.get()
        self.ser_wd  = self.ser_wdEntered.get()
        print(self.ser_url)
        print(self.ser_wd)
        url = self.ser_url
        inter_dict = {'wd':self.ser_wd}
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
        self.ser_baseurl = urls[0]
        print(self.ser_baseurl)

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
        self.ser_loginurl = url
        self.ser_logindict = {}
        soup = BeautifulSoup(html, "lxml")
        for row in soup.find_all('input'):
            if row.has_attr("name") and row.has_attr("value"):
                self.ser_logindict[row["name"]] = row["value"]
        
        print("################进入网站成功#######################")
        self.ser_flushMe()
        
    def ser_flushMe(self):
        url = self.ser_baseurl + "checknum.aspx"
        print(url)
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



        
        
    def ser_clickMe(self):
        self.ser_save()
        text = self.ser_btaction.config('text')
        if  text[4] == '关闭':
            if self.ser_thread.is_alive():
                self.ser_thread.stop()
            self.ser_thread = None
            self.ser_btaction.configure(text='开始')
            return
            
        self.ser_name  = self.ser_nameEntered.get()
        self.ser_pwd   = self.ser_pwdEntered.get()
        self.ser_check = self.ser_checkEntered.get()
        if self.ser_name == "":
            messagebox.showinfo("提示","账号不能为空！")
            return

        if self.ser_pwd == "":
            messagebox.showinfo("提示","密码不能为空！")
            return

        if self.ser_check == "":
            messagebox.showinfo("提示","验证码不能为空！")
            return
        
        print("############################账号登陆##############################")
        print(self.ser_loginurl)
        print(self.ser_logindict)
        self.ser_logindict["txt_U_name"]     = self.ser_name
        self.ser_logindict["txt_U_Password"] = self.ser_pwd 
        self.ser_logindict["txt_validate"]   = self.ser_check
        
        data = urllib.parse.urlencode(self.ser_logindict).encode('utf-8')
        request = urllib.request.Request(url = self.ser_loginurl, data = data, headers = headers, method = 'POST')
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

        login = False
        soup = BeautifulSoup(html, "lxml")
        for row in soup.find_all('title'):
            if row.get_text().find("协议与规则") >= 0:
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
        url = self.ser_baseurl + "ch/agreement.aspx/LocationUrl"
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
        #http://54jndgw.ttx158.com/cp5-5-ag/opadmin/main.aspx
        agreement_dict = {}
        agreement_dict["stype"] = "1"
        data = urllib.parse.urlencode(agreement_dict).encode('utf-8')
        url = self.ser_baseurl + "opadmin/main.aspx"
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
            returnf
        print(html)

        print("############################报表查询##############################")
        html = ""
        #http://54jndgw.ttx158.com/cp5-5-ag/opadmin/mreport_new.aspx
        agreement_dict = {}
        agreement_dict["stype"] = "1"
        data = urllib.parse.urlencode(agreement_dict).encode('utf-8')
        url = self.ser_baseurl + "opadmin/mreport_new.aspx"
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
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误 ==> 网络连接错误！")
            return
        print(html)
        
        self.ser_btaction.configure(text='关闭')
        self.ser_thread = ServerThread(self)
        self.ser_thread.start()
            
    def ser_save(self):
        #增加新的section
        #
        self.ser_url  = self.ser_urlEntered.get()
        self.ser_wd = self.ser_wdEntered.get()
        
        self.ser_name  = self.ser_nameEntered.get()
        self.ser_pwd = self.ser_pwdEntered.get()
        
        self.ser_conf.set("url", "value", self.ser_url)
        self.ser_conf.set("wd", "value", self.ser_wd)
        self.ser_conf.set("name", "value", self.ser_name)
        self.ser_conf.set("pwd", "value", self.ser_pwd)
        #写回配置文件
        self.ser_conf.write(open("server.txt", "w"))
        messagebox.showinfo("提示","配置成功！")
        
    def Close(self):
        if self.ser_thread != None:
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
