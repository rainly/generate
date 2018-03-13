## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
#梯子游戏
from bs4 import BeautifulSoup  # 引入beautifulsoup 解析html事半功倍
import re
import urllib
import urllib.request
import sys
import io
import json
from collections import deque
import time
import datetime
import http.cookiejar
import json
import pymysql.cursors
import ssl
from selenium import webdriver
from selenium.common.exceptions import *
import sqlite3
import configparser
import random
from selenium import webdriver
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
ssl._create_default_https_context = ssl._create_unverified_context

driver = webdriver.Chrome()
driver.get("http://a8033.com/")



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

#10=20=30=40
#1=3=6=4


class TestThread(threading.Thread):
    def __init__(self, target, thread_num=0, timeout=1.0):
        super(TestThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout
    def run(self):
        self.target.textlog.insert(tk.INSERT,'Thread start\n')                   
        subthread = threading.Thread(target = self.target_func, args=())
        subthread.setDaemon(True)
        subthread.start()

        while not self.stopped:
            subthread.join(self.timeout)

        self.target.textlog.insert(tk.INSERT,'Thread stopped'+ "\n")

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped
    
    def target_func(self):

        url = self.target.url
        print("地址:" + url)

        jump = self.target.jump
        print("输停:" + jump)

        monery = self.target.monery
        print("下注金额:" + monery)
        
        agent = self.target.agent
        print("代理:" + agent)    
        
        url_agent = "http://121.40.206.168/soft_net/SBDL_NSkt.php?NS=" + agent
        print(url_agent)
        request = urllib.request.Request(url_agent, headers = headers)
        try:
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ' + str(e.code))
            print('Error reason: ' + e.reason)
            print("错误","网络连接错误！")
            return
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ' + e.reason)
            print("错误","网络连接错误！")
            return
        except Exception as msg:
            print("Exception:%s" % msg)
            return
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            print("错误","网络连接错误！")
            return
        html = html.strip()
        if html != "1":
            print("错误","账号未注册！")
            return
        
        #jumps   = jump.split("+")
        monerys = monery.split("+")
        if len(monerys) == 0:
            print("错误","金额配置出错")
            return
            
        #if len(jumps) + 1 != len(monerys):
        #    print("输停长度 ！= 下注金额长度")
        #    return
        #jumps.append("0")  
        
        #driver.get(url)
        driver.implicitly_wait(5)
        
        try:
            while self.stopped == False:
                print("检测是否打开梯子游戏")  
                isJump = False
                handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
                for handle in handles:# 切换窗口
                    if handle != driver.current_window_handle:
                        driver.switch_to_window(handle)
                        print(driver.title)
                        if driver.title == "梯子游戏":
                            isJump = True
                            break
                if isJump:
                    break
                time.sleep(5)
                
            print("已经打开梯子游戏")   
            Last_Award_Issue = ""
            Last_Award_Issue_tclass = ""
            Jump_Idx   = 0

            while self.stopped == False:
                try:
                    time.sleep(5)

                    print("********************************************************")
                    Cur_Award_Issue1_1 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[1]/td[1]").text
                    #Cur_Award_Issue1_2 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[1]/td[2]").text
                    #print(Cur_Award_Issue1_1)

                    Cur_Award_Issue2_1 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[2]/td[1]").text
                    #Cur_Award_Issue2_2 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[2]/td[2]").text
                    #print(Cur_Award_Issue2_1)
                    
                    if Cur_Award_Issue1_1 == Last_Award_Issue:
                        print("***等待开奖*** ==>", Cur_Award_Issue1_1)
                        continue

                    Last_Award_Issue = Cur_Award_Issue1_1

                    print("***处理中奖结果*** ==>", Cur_Award_Issue1_1)
                    tclass = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[2]/td[2]/span").get_attribute("class")
                    #print(tclass)
                    #<span class="LD-resultItem LD--s LD--l4o">4单</span>
                    #<span class="LD-resultItem LD--s LD--r4e">4双</span>
                    #<span class="LD-resultItem LD--s LD--r3o">3单</span>
                    #<span class="LD-resultItem LD--s LD--l3e">3双</span>
                    #处理中奖结果
                    Last_Award_Issue_Win = False
                    if Last_Award_Issue_tclass != "":                       
                        Last_Award_Issue_Win = False
                        if tclass == Last_Award_Issue_tclass:
                            Last_Award_Issue_Win = True
                        else:
                            Last_Award_Issue_Win = False
                        #######################################
                        if Last_Award_Issue_Win == True:
                            Jump_Idx    = 0
                            print("***中奖***")
                        else:
                            Jump_Idx    = Jump_Idx + 1
                            print("***未中奖***")
                        #######################################
                        if Jump_Idx >= len(monerys):
                            Jump_Idx = 0;
                    else:
                        print("***未下注***")
                                                 
                    print("********************************************************") 
                    Last_Award_Issue_tclass = "";
                    if tclass == "LD-resultItem LD--s LD--l4o":
                        print("***开奖***4单 ==>不购买")
                        Last_Award_Issue_tclass = ""
                    elif  tclass == "LD-resultItem LD--s LD--r4e":
                        print("***开奖***4双 ==>购买3单")
                        Last_Award_Issue_tclass = "LD-resultItem LD--s LD--r3o"
                    elif  tclass == "LD-resultItem LD--s LD--l3e":
                        print("***开奖***3双 ==>不购买") 
                        Last_Award_Issue_tclass = ""
                    elif  tclass == "LD-resultItem LD--s LD--r3o":
                        print("***开奖***3单 ==>购买4双")  
                        Last_Award_Issue_tclass = "LD-resultItem LD--s LD--r4e"
                    else:
                        print("***开奖***未知道类型")
                        Last_Award_Issue_tclass = ""

                    if Last_Award_Issue_tclass == "":
                        print("***本轮不下注:***" + Cur_Award_Issue1_1, " 金额：", monerys[Jump_Idx])
                        continue
                    else:
                        print("***开始下注:***" + Cur_Award_Issue1_1, " 金额：", monerys[Jump_Idx])


                    input1 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/table/tbody/tr[2]/td[4]/div[1]/input")
                    input2 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/table/tbody/tr[2]/td[4]/div[2]/input")
                    input3 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/table/tbody/tr[2]/td[4]/div[3]/input")
                    input4 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/table/tbody/tr[2]/td[4]/div[4]/input")
                    
                    #<span class="LD-resultItem LD--s LD--l4o">4单</span>
                    #<span class="LD-resultItem LD--s LD--r4e">4双</span>
                    #<span class="LD-resultItem LD--s LD--r3o">3单</span>
                    #<span class="LD-resultItem LD--s LD--l3e">3双</span>
                    
                    if Last_Award_Issue_tclass == "LD-resultItem LD--s LD--r3o":#3单
                        input1.clear()
                        input1.send_keys(monerys[Jump_Idx])
                    elif Last_Award_Issue_tclass == "LD-resultItem LD--s LD--r4e":#4双
                        input4.clear()
                        input4.send_keys(monerys[Jump_Idx])    
                        
                    time.sleep(1)          
                    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/div[2]/button[2]").click()  
                    time.sleep(1)
                    driver.find_element_by_xpath("//*[@id=\"alertify\"]/div/div/div[2]/div[2]/button[2]").click()
                    
                except NoSuchElementException as msg:
                    print("NoSuchElementException:%s" % msg)
                    pass
                except WebDriverException as msg:
                    print("WebDriverException:%s" % msg)
                    pass
                except NoSuchWindowException as msg:
                    print("NoSuchWindowException:%s" % msg)
                    pass
                except NoSuchAttributeException as msg:
                    print("NoSuchAttributeException:%s" % msg)
                    pass
                except NoAlertPresentException as msg:
                    print("NoAlertPresentException:%s" % msg)
                    pass
                except ElementNotVisibleException as msg:
                    print("ElementNotVisibleException:%s" % msg)
                    pass
                except ElementNotSelectableException as msg:
                    print("ElementNotSelectableException:%s" % msg)
                    pass
                except TimeoutException as msg:
                    print("TimeoutException:%s" % msg)
                    pass
                except Exception as msg:
                    print("Exception:%s" % msg)
                    pass
                except:
                    #print("error lineno:" + str(sys._getframe().f_lineno))
                    #self.target.textlog.insert(tk.INSERT,"error lineno:" +
                    #str(sys._getframe().f_lineno))
                    pass
        except NoSuchElementException as msg:
            print("NoSuchElementException:%s" % msg)
            pass
        except WebDriverException as msg:
            print("WebDriverException:%s" % msg)
            pass
        except NoSuchWindowException as msg:
            print("NoSuchWindowException:%s" % msg)
            pass
        except NoSuchAttributeException as msg:
            print("NoSuchAttributeException:%s" % msg)
            pass
        except NoAlertPresentException as msg:
            print("NoAlertPresentException:%s" % msg)
            pass
        except ElementNotVisibleException as msg:
            print("ElementNotVisibleException:%s" % msg)
            pass
        except ElementNotSelectableException as msg:
            print("ElementNotSelectableException:%s" % msg)
            pass
        except TimeoutException as msg:
            print("TimeoutException:%s" % msg)
            pass
        except Exception as msg:
            print("Exception:%s" % msg)
            pass
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            #self.target.textlog.insert(tk.INSERT,"error lineno:" +
            #str(sys._getframe().f_lineno))
            pass    
        
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.thread = None
        #生成config对象
        self.conf = configparser.ConfigParser()
        #用config对象读取配置文件
        self.conf.read("a8033_2.txt")

        if self.conf.has_section("url") == True:
            self.url = self.conf.get("url", "value")
        else:
            self.url = ""
            self.conf.add_section("url")
            self.conf.set("url", "value", "")

        if self.conf.has_section("jump") == True:
            self.jump = self.conf.get("jump", "value")
        else:
            self.jump = ""
            self.conf.add_section("jump")
            self.conf.set("jump", "value", "")

        if self.conf.has_section("monery") == True:
            self.monery = self.conf.get("monery", "value")
        else:
            self.monery = ""
            self.conf.add_section("monery")
            self.conf.set("monery", "value", "")


        if self.conf.has_section("agent") == True:
            self.agent = self.conf.get("agent", "value")
        else:
            self.agent = ""
            self.conf.add_section("agent")
            self.conf.set("agent", "value", "")
        
        self.createWidgets()

    def createWidgets(self):
        # Tab Control introduced here --------------------------------------
        self.tabControl = ttk.Notebook(self)          # Create Tab Control
        self.tab1 = ttk.Frame(self.tabControl)            # Create a tab
        self.tabControl.add(self.tab1, text='第一页')      # Add the tab
        self.tabControl.pack(expand=1, fill="both")  # Pack to make visible
        # ~ Tab Control introduced here
        # -----------------------------------------
        self.createTab1()
        
    def createTab1(self):
        #---------------Tab1控件介绍------------------#
        # Modified Button Click Function  
        # We are creating a container tab3 to hold all other widgets
        self.MyFrame = ttk.LabelFrame(self.tab1, text='操作区')
        self.MyFrame.grid(column=0, row=0, padx=8, pady=4)
        #第一行
        # Changing our Label  
        ttk.Label(self.MyFrame, text="代理:").grid(column=0, row=0, sticky='W')  
  
        # Adding a Textbox Entry widget  
        # self.url = tk.StringVar()  
        self.agentEntered = ttk.Entry(self.MyFrame, width=60, textvariable=self.agent)  
        self.agentEntered.grid(column=1, row=0, sticky='W')  

        #第二行
        ttk.Label(self.MyFrame, text="请选择:").grid(column=0, row=1,sticky='W')
        # Adding a Combobox
        self.book = tk.StringVar()
        self.bookChosen = ttk.Combobox(self.MyFrame, width=60, textvariable=self.book)
        self.bookChosen['values'] = ('大', '小','单','双')
        self.bookChosen.grid(column=1, row=1, sticky='W')
        self.bookChosen.current(0)  #设置初始显示值，值为元组['values']的下标
        self.bookChosen.config(state='readonly')  #设为只读模式
        self.bookChosen.bind("<<ComboboxSelected>>", self.Chosen)  

        # Using a scrolled Text control
        self.scrolW = 80
        self.scrolH = 10
        #第三行
        ttk.Label(self.MyFrame, text="策略配置(3单、4双)(无需配置)").grid(column=0, row=2,sticky='W')
        #第四行
        self.textJump = scrolledtext.ScrolledText(self.MyFrame, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.textJump.grid(column=0, row=3, sticky='WE', columnspan=3)
    
        #第五行
        ttk.Label(self.MyFrame, text="金额配置(10+20+40+80+...)").grid(column=0, row=4,sticky='W')
        #第五行
        self.textMonery = scrolledtext.ScrolledText(self.MyFrame, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.textMonery.grid(column=0, row=5, sticky='WE', columnspan=3)        
        
        
        #第行
        # Adding a Button
        self.btaction = ttk.Button(self.MyFrame,text="保存",width=10,command=self.save).grid(column=1,row=6,sticky='E')   

        #第行
        ttk.Label(self.MyFrame, text="日志信息:").grid(column=0, row=7,sticky='W')
        #第行
        self.textlog = scrolledtext.ScrolledText(self.MyFrame, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.textlog.grid(column=0, row=8, sticky='WE', columnspan=3)
        #第行
        # Adding a Button
        self.btaction = ttk.Button(self.MyFrame,text="开始",width=10,command=self.clickMe)
        self.btaction.grid(column=1,row=9,sticky='E')   
        # 一次性控制各控件之间的距离
        for child in self.MyFrame.winfo_children(): 
            child.grid_configure(padx=3,pady=1)
        # 单独控制个别控件之间的距离
        #self.btaction.grid(column=2,row=1,rowspan=2,padx=6)
        #---------------Tab1控件介绍------------------#
        
        self.agentEntered.insert(END, self.agent)
        self.textJump.insert(tk.INSERT, self.jump)
        self.textMonery.insert(tk.INSERT, self.monery)
            
    def clickMe(self):
        text = self.btaction.config('text')
        if  text[4] == '关闭':
            self.btaction.configure(text='开始')
            self.thread.stop()
            #self.thread.join()
        else:
            self.btaction.configure(text='关闭')
            self.thread = TestThread(self)
            self.thread.start()
            
    def save(self):
        #增加新的section
        #
        self.agent = self.agentEntered.get()
        self.jump = self.textJump.get(1.0, END)
        self.monery = self.textMonery.get(1.0, END)
        
        self.conf.set("agent", "value", self.agentEntered.get())
        self.conf.set("jump", "value", self.textJump.get(1.0, END))
        self.conf.set("monery", "value", self.textMonery.get(1.0, END))
        #写回配置文件
        self.conf.write(open("a8033_2.txt", "w"))
        messagebox.showinfo("提示","配置成功！")
        
    def Chosen(self, *args):
        messagebox.showinfo("提示",self.bookChosen.get())
        
def main():
    app = Application()
    app.title("梯子游戏 自动打码神器")
    app.resizable(0,0) #阻止Python GUI的大小调整
    # 主消息循环:
    app.mainloop()

if __name__ == "__main__":
    main()
