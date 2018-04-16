## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
#北京赛车

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

import urllib
import urllib.request
import urllib.response
import urllib.error
import http.cookiejar
import configparser
import re
import ssl
import random

ssl._create_default_https_context = ssl._create_unverified_context


#driver = webdriver.Chrome()
##driver.get("http://0190022.com")
#driver.get("http://baidu.com")






#本方案累计赢[1000]元跳转到方案[1]
#本方案累计输[1000]元跳转到方案[1]

import re  #python的正则表达式模块
#input = '1:3.125 false,hello'
input = '本方案累计赢[1000]元跳转到方案[1]'
#(a, b, c, d) = re.search('^(\d+):([\d.]+) (\w+),(\w+)$',input).groups()
(a, b) = re.search('^本方案累计赢\\[(\d+)\\]元跳转到方案\\[(\d+)\\]$',input).groups()
print(a)
print(b)



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


class BettingThread(threading.Thread):
    def __init__(self, target, thread_num=0, timeout=5.0):
        super(BettingThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout
    def run(self):
        self.target_func()

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped

    def logprint(self, log):
        print(log)
        self.target.textlog.insert(tk.INSERT, log + "\n")

    def delBallNo(self, road, buyno, BALL_DATA):
        #Temp_Strategy         = BALL_DATA["Temp_Strategy"]
        #Temp_Monery           = BALL_DATA["Temp_Monery"]
        #Temp_Win              = BALL_DATA["Temp_Win"]
        #Temp_Strategy_Win     = BALL_DATA["Temp_Strategy_Win"]
        #Temp_Rule             = BALL_DATA["Temp_Rule"]
        #Temp_Rule_Idx         = BALL_DATA["Temp_Rule_Idx"]
        #处理中奖结果
        Win = 0
        if BALL_DATA["Temp_Rule"] != None:
            if road[buyno - 1] == BALL_DATA["Temp_Rule"][1][BALL_DATA["Temp_Rule_Idx"]]:
                Win = 1
                BALL_DATA["Temp_Win"]              = BALL_DATA["Temp_Win"] + int(BALL_DATA["Temp_Monery"][1]);
                BALL_DATA["Temp_Strategy_Win"]     = BALL_DATA["Temp_Strategy_Win"] + int(BALL_DATA["Temp_Monery"][1])    
                self.logprint("位置" + str(buyno) + "***中奖***金额:" + BALL_DATA["Temp_Monery"][1])
            else:
                Win = 0
                BALL_DATA["Temp_Win"]              = BALL_DATA["Temp_Win"] - int(BALL_DATA["Temp_Monery"][1]);
                BALL_DATA["Temp_Strategy_Win"]     = BALL_DATA["Temp_Strategy_Win"] - int(BALL_DATA["Temp_Monery"][1])    
                self.logprint("位置" + str(buyno) + "***未中奖***")
            ##[1, 10, 2, 2]    
            for monery in BALL_DATA["Temp_Strategy"]["monerys"]:
                if  Win == 1 and monery[0] == BALL_DATA["Temp_Monery"][2]:
                    BALL_DATA["Temp_Monery"] = monery
                    break
                if  Win == 0 and monery[0] == BALL_DATA["Temp_Monery"][3]:
                    BALL_DATA["Temp_Monery"] = monery
                    break
            self.logprint("位置" + str(buyno) + "***当前方案输赢:" + str(BALL_DATA["Temp_Strategy_Win"]))
            #Win = [1000, 1]    
            if BALL_DATA["Temp_Strategy_Win"] > int(BALL_DATA["Temp_Strategy"]["jumps"]["Win"][0]):
                BALL_DATA["Temp_Strategy_Win"] = 0
                BALL_DATA["Temp_Strategy"] = self.target.Strategys[int(BALL_DATA["Temp_Strategy"]["jumps"]["Win"][1])]
                BALL_DATA["Temp_Rule"]     = None
                BALL_DATA["Temp_Rule_Idx"] = 0
                BALL_DATA["Temp_Monery"]   = BALL_DATA["Temp_Strategy"]["monerys"][0]
                self.logprint("位置" + str(buyno) + "***本方案累计赢跳转***")
                        
            #Faild = [1000, 1]    
            if BALL_DATA["Temp_Strategy_Win"] < -int(BALL_DATA["Temp_Strategy"]["jumps"]["Faild"][0]):
                BALL_DATA["Temp_Strategy_Win"] = 0
                BALL_DATA["Temp_Strategy"] = self.target.Strategys[int(BALL_DATA["Temp_Strategy"]["jumps"]["Faild"][1])]
                BALL_DATA["Temp_Rule"]     = None
                BALL_DATA["Temp_Rule_Idx"] = 0
                BALL_DATA["Temp_Monery"]   = BALL_DATA["Temp_Strategy"]["monerys"][0]
                self.logprint("位置" + str(buyno) + "***本方案累计输跳转***")
        else:
            self.logprint("位置" + str(buyno) + "***未下注***")


                    

        self.logprint("位置" + str(buyno) + "***检测规则是否下注***")
        if BALL_DATA["Temp_Rule"] != None:
            BALL_DATA["Temp_Rule_Idx"] = BALL_DATA["Temp_Rule_Idx"] + 1
            if len(BALL_DATA["Temp_Rule"][1]) <= BALL_DATA["Temp_Rule_Idx"]:
                BALL_DATA["Temp_Rule"] = None
                BALL_DATA["Temp_Rule_Idx"] = 0
                
        if BALL_DATA["Temp_Rule"] == None:
            keys = sorted(self.roads)
            tmp  = ""
            for key in keys:
                tmp = tmp + self.roads[key][buyno - 1]

            for rule in BALL_DATA["Temp_Strategy"]["rules"]:
                #[大大， 小小]
                tmp1 = rule[0]
                tmp2 = ""
                self.logprint("位置" + str(buyno) + "***查找规则***" + tmp1)
                if len(tmp) > len(tmp1):
                    tmp2 = tmp[len(tmp) - len(tmp1):]
                else:
                    tmp2 = tmp
                self.logprint("位置" + str(buyno) + "***路单规则***" + tmp)

                if tmp1 == tmp2:
                    BALL_DATA["Temp_Rule"] = rule
                    BALL_DATA["Temp_Rule_Idx"] = 0
                    self.logprint("位置" + str(buyno) + "***规则符合条件***" + str(rule[0]) + "=" + str(rule[1]))
                    break
                else:
                    self.logprint("位置" + str(buyno) + "***规则不符合条件***" + str(rule[0]) + "=" + str(rule[1]))    
                            
        #双面玩法
        if BALL_DATA["Temp_Rule"] != None:
            '''
            if BALL_DATA["Temp_Rule"][1][BALL_DATA["Temp_Rule_Idx"]] == "大":
                driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div[1]/div[2]/button[1]")
            if BALL_DATA["Temp_Rule"][1][BALL_DATA["Temp_Rule_Idx"]] == "小":
                driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div[1]/div[2]/button[2]")
            if BALL_DATA["Temp_Rule"][1][BALL_DATA["Temp_Rule_Idx"]] == "单":
                driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div[1]/div[2]/button[3]")
            if BALL_DATA["Temp_Rule"][1][BALL_DATA["Temp_Rule_Idx"]] == "双":
                driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div[1]/div[2]/button[4]")
            '''

            self.logprint("位置" + str(buyno) + "***购买:" + BALL_DATA["Temp_Rule"][1][BALL_DATA["Temp_Rule_Idx"]] + "金额：" + str(BALL_DATA["Temp_Monery"][1]))

            '''
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[4]/div[1]/div[1]/input").clear()
            driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[4]/div[1]/div[1]/input").send_keys(BALL_DATA["Temp_Monery"][1])
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[4]/div[1]/div[1]/button").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[4]/div[2]/button[3]").click()
            '''    
    def target_func(self):
    
        print("**********target_func begin***********")
        
        #buyno = int(self.target.buyno)
        #self.logprint("位置:" + self.target.buyno)
        #if buyno < 1 or buyno > 10:
        #    self.logprint("错误 ==> 购买位置配置出错")
        #    return  

        if len(self.target.Strategys) <= 0:
            self.logprint("错误 ==> 购买位置配置出错")
            return   

        print(self.target.Strategys)  
                 
        '''
        driver.implicitly_wait(5)           
        while self.stopped == False:
            print("**********find title***********")
            isStrategy = False
            try:
                handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
                #print(handles) # 输出句柄集合
                for handle in handles:# 切换窗口
                    if handle != driver.current_window_handle:
                        driver.switch_to_window(handle)
                        print(driver.title)
                        if driver.title == "彩票游戏官方版":
                            isStrategy = True
                            break
                if isStrategy:
                    break
                time.sleep(5)
            except NoSuchElementException as msg:
                self.logprint("NoSuchElementException:%s" % msg)
                pass
            except WebDriverException as msg:
                self.logprint("WebDriverException:%s" % msg)
                pass
            except NoSuchWindowException as msg:
                self.logprint("NoSuchWindowException:%s" % msg)
                pass
            except NoSuchAttributeException as msg:
                self.logprint("NoSuchAttributeException:%s" % msg)
                pass
            except NoAlertPresentException as msg:
                self.logprint("NoAlertPresentException:%s" % msg)
                pass
            except ElementNotVisibleException as msg:
                self.logprint("ElementNotVisibleException:%s" % msg)
                pass
            except ElementNotSelectableException as msg:
                self.logprint("ElementNotSelectableException:%s" % msg)
                pass
            except TimeoutException as msg:
                self.logprint("TimeoutException:%s" % msg)
                pass
            except Exception as msg:
                print("error lineno:" + str(sys._getframe().f_lineno))
                self.logprint("Exception:%s" % msg)
                pass
            except:
                print("error lineno:" + str(sys._getframe().f_lineno))
                #self.target.textlog.insert(tk.INSERT,"error lineno:" +
                #str(sys._getframe().f_lineno))
                pass
        '''
        Last_Award_Issue = ""
        Last_Award_Issue_Have = False
        self.roads = {}
        SleepTime             = 1

        BALL_DATAS = {}
        items = self.target.buyno.split(",")
        for item in items:
            BALL_DATA = {
                "Temp_Strategy": self.target.Strategys[1],
                "Temp_Monery": self.target.Strategys[1]["monerys"][0],    
                "Temp_Win": 0,
                "Temp_Strategy_Win": 0,
                "Temp_Rule": None,
                "Temp_Rule_Idx": 0,
            }
            BALL_DATAS[item] = BALL_DATA;
        Test_no               = 0
        while self.stopped == False:
            try:
                SleepTime = SleepTime + 1
                if SleepTime < 2:
                    time.sleep(1)
                    continue
                    
                SleepTime = 0  
                self.logprint("**********************************************")   
                
                #Cur_Award_Issue1 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[2]/div[2]").text
                #Cur_Award_Issue2 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[1]").text
                Cur_Award_Issue1  = "No. " + str(1001 + Test_no)
                Cur_Award_Issue2  = "No. " + str(1000 + Test_no)
                Test_no = Test_no + 1

                if Cur_Award_Issue1 == "" or Cur_Award_Issue2 == "":
                    continue

                Cur_Award_Issue1 = Cur_Award_Issue1.replace("No. ", "")
                Cur_Award_Issue2 = Cur_Award_Issue2.replace("No. ", "")
                
                if int(Cur_Award_Issue2) + 1 != int(Cur_Award_Issue1):
                    self.logprint("***期号不相等***")   
                    continue
                    
                if Last_Award_Issue != "" and int(Last_Award_Issue) != int(Cur_Award_Issue2):
                    self.logprint("***等待开奖***")   
                    continue

                self.logprint("*******获取开奖结果**********")

                '''
                Ball01 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[2]/span[1]").text
                Ball02 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[2]/span[2]").text
                Ball03 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[2]/span[3]").text
                Ball04 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[2]/span[4]").text
                Ball05 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[2]/span[5]").text
                Ball06 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[2]/span[6]").text
                Ball07 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[2]/span[7]").text
                Ball08 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[2]/span[8]").text
                Ball09 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[2]/span[9]").text
                Ball10 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[2]/span[10]").text
                '''

                Ball01 = str(random.randint(1,10))
                Ball02 = str(random.randint(1,10))
                Ball03 = str(random.randint(1,10))
                Ball04 = str(random.randint(1,10))
                Ball05 = str(random.randint(1,10))
                Ball06 = str(random.randint(1,10))
                Ball07 = str(random.randint(1,10))
                Ball08 = str(random.randint(1,10))
                Ball09 = str(random.randint(1,10))
                Ball10 = str(random.randint(1,10))

                if Ball01 == "" or Ball02 == "" or Ball03 == "" or Ball04 == "" or Ball05 == "" or Ball06 == "" or Ball07 == "" or Ball08 == "" or Ball09 == "" or Ball10 == "":
                    self.logprint("***数据还在加载中***")   
                    continue
                    
                def GetType(BallNo):
                    if int(BallNo) > 5:
                        return '大'
                    else:
                        return '小'   
                
                
                road = [GetType(Ball01), GetType(Ball02), GetType(Ball03), GetType(Ball04), GetType(Ball05), GetType(Ball06), GetType(Ball07), GetType(Ball08), GetType(Ball09), GetType(Ball10)]
                self.roads[Cur_Award_Issue2] = road

                '''
                for idx  in range(1,5):
                    Award_Issue = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[1]").text
                    Ball01 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[2]/span[1]").text
                    Ball02 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[2]/span[2]").text
                    Ball03 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[2]/span[3]").text
                    Ball04 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[2]/span[4]").text
                    Ball05 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[2]/span[5]").text
                    Ball06 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[2]/span[6]").text
                    Ball07 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[2]/span[7]").text
                    Ball08 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[2]/span[8]").text
                    Ball09 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[2]/span[9]").text
                    Ball10 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[2]/span[10]").text
                    road = [GetType(Ball01), GetType(Ball02), GetType(Ball03), GetType(Ball04), GetType(Ball05), GetType(Ball06), GetType(Ball07), GetType(Ball08), GetType(Ball09), GetType(Ball10)]
                    self.roads[Award_Issue] = road   
                '''
    
                Last_Award_Issue = Cur_Award_Issue1
                items = self.target.buyno.split(",")
                for item in items:
                    self.delBallNo(road, int(item), BALL_DATAS[item])

            except NoSuchElementException as msg:
                self.logprint("NoSuchElementException:%s" % msg)
                pass
            except WebDriverException as msg:
                self.logprint("WebDriverException:%s" % msg)
                pass
            except NoSuchWindowException as msg:
                self.logprint("NoSuchWindowException:%s" % msg)
                pass
            except NoSuchAttributeException as msg:
                self.logprint("NoSuchAttributeException:%s" % msg)
                pass
            except NoAlertPresentException as msg:
                self.logprint("NoAlertPresentException:%s" % msg)
                pass
            except ElementNotVisibleException as msg:
                self.logprint("ElementNotVisibleException:%s" % msg)
                pass
            except ElementNotSelectableException as msg:
                self.logprint("ElementNotSelectableException:%s" % msg)
                pass
            except TimeoutException as msg:
                self.logprint("TimeoutException:%s" % msg)
                pass
            '''
            except Exception as msg:
                self.logprint("Exception:%s" % msg)
                self.logprint("error lineno:" + str(sys._getframe().f_lineno))
                pass
            #except:
                #self.logprint("error lineno:" + str(sys._getframe().f_lineno))
                #self.target.textlog.insert(tk.INSERT,"error lineno:" +
                #str(sys._getframe().f_lineno))
                pass
            '''
        print("**********target_func end***********")       
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.Close)
        self.thread = None
        #生成config对象
        self.conf = configparser.ConfigParser()
        #用config对象读取配置文件
        self.conf.read("bjpk.txt")

        if self.conf.has_section("url") == True:
            self.url = self.conf.get("url", "value")
        else:
            self.url = ""
            self.conf.add_section("url")
            self.conf.set("url", "value", "")
            
        if self.conf.has_section("buyno") == True:
            self.buyno = self.conf.get("buyno", "value")
        else:
            self.buyno = ""
            self.conf.add_section("buyno")
            self.conf.set("buyno", "value", "")            
            

        if self.conf.has_section("Strategy") == True:
            self.Strategy = self.conf.get("Strategy", "value")
        else:
            self.Strategy = ""
            self.conf.add_section("Strategy")
            self.conf.set("Strategy", "value", "")
            
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
        # Using a scrolled Text control
        self.scrolW = 60
        self.scrolH = 10
        
    
        #行
        line = 0
        # Changing our Label
        ttk.Label(self.MyFrame, text="地址:").grid(column=0, row=line, sticky='W')  
  
        # Adding a Textbox Entry widget
        self.urlEntered = ttk.Entry(self.MyFrame, width=60, textvariable=self.url)  
        self.urlEntered.grid(column=1, row=line, sticky='W')

        self.btaction = ttk.Button(self.MyFrame,text="进入",width=10,command=self.enterMe)
        self.btaction.grid(column=2,row=line,sticky='E')  
        
        #行
        line = line + 1
        # Changing our Label
        ttk.Label(self.MyFrame, text="购买位置:").grid(column=0, row=line, sticky='W')  
  
        # Adding a Textbox Entry widget
        self.buynoEntered = ttk.Entry(self.MyFrame, width=60, textvariable=self.buyno)  
        self.buynoEntered.grid(column=1, row=line, sticky='W')

        '''
        ==============================

        庄庄=闲庄
        闲闲=庄闲

        1=10=1=1

        本方案累计赢[1000]元跳转到方案[1]
        本方案累计输[1000]元跳转到方案[1]

        ==============================
        '''   
             
        #行
        line = line + 1
        ttk.Label(self.MyFrame, text="配置信息").grid(column=0,row=line,sticky='W',columnspan=3)
        #行
        line = line + 1
        self.textStrategy = scrolledtext.ScrolledText(self.MyFrame,width=self.scrolW,height=self.scrolH,wrap=tk.WORD)
        self.textStrategy.grid(column=0,row=line,sticky='WE',columnspan=3)
            
        #行
        # Adding a Button
        line = line + 1
        self.btaction = ttk.Button(self.MyFrame,text="保存",width=10,command=self.save).grid(column=2,row=line,sticky='E')   
        #行
        line = line + 1
        ttk.Label(self.MyFrame,text="日志信息:").grid(column=0,row=line,sticky='W')
        #行
        line = line + 1
        self.textlog = scrolledtext.ScrolledText(self.MyFrame,width=self.scrolW,height=self.scrolH,wrap=tk.WORD)
        self.textlog.grid(column=0,row=line,sticky='WE',columnspan=3)
        #行
        # Adding a Button
        line = line + 1
        self.btaction = ttk.Button(self.MyFrame,text="开始",width=10,command=self.clickMe)
        self.btaction.grid(column=2,row=line,sticky='E')  
        
        # 一次性控制各控件之间的距离
        for child in self.MyFrame.winfo_children(): 
            child.grid_configure(padx=3,pady=1)
        # 单独控制个别控件之间的距离
        #self.btaction.grid(column=2,row=1,rowspan=2,padx=6)
        #---------------Tab1控件介绍------------------#
        
        self.urlEntered.insert(END,self.url)
        self.buynoEntered.insert(END,self.buyno)
        self.textStrategy.insert(tk.INSERT,self.Strategy)

    def enterMe(self):
        self.url = self.urlEntered.get()
        driver.get(self.url)
            
    def clickMe(self):
        if  self.thread != None:
            self.btaction.configure(text='开始')
            if self.thread.is_alive():
                self.thread.stop()
            self.thread.join()
            self.thread = None
            return
        self.url      = self.urlEntered.get()
        self.buyno    = self.buynoEntered.get()
        self.Strategy = self.textStrategy.get(1.0,END)
        if self.url == "":
            messagebox.showinfo("提示","地址不能为空")
            return
            
        if self.buyno == "":
            messagebox.showinfo("提示","地址不能为空")
            return
            
        if self.Strategy == "":
            messagebox.showinfo("提示","停次数不能为空！")
            return
        self.Paser();   
        self.btaction.configure(text='关闭')
        self.thread = BettingThread(self)
        self.thread.start()

    def Paser(self):
        Jump_idx = 0
        self.Strategys = {}
        blocks = self.Strategy.split("==============================")
        for block in blocks:
            if block == "" or block == "\n":
                continue
            Strategy = {}
            inblocks = re.split('\n\n', block)
            for inblock in inblocks:
                if inblock == "" or block == "\n":
                    continue
                if "rules" not in Strategy:
                    rules = []
                    line = inblock.split("\n")
                    for item in line:
                        rule = re.split('=', item)
                        rules.append(rule) 
                    Strategy["rules"] = rules
                elif "monerys" not in Strategy:
                    monerys = []
                    line = inblock.split("\n")
                    for item in line:
                        monery = re.split('=',item)
                        monerys.append(monery) 
                    Strategy["monerys"] = monerys
                elif "jumps" not in Strategy:
                    Jumps = {}
                    #本方案累计赢[1000]元跳转到方案[1]
                    #本方案累计输[1000]元跳转到方案[1]
                    line = inblock.split("\n")
                    for input in line:
                        searchObj  = re.search('^本方案累计赢\\[(\d+)\\]元跳转到方案\\[(\d+)\\]$',input)
                        if searchObj:
                            (a, b) = searchObj .groups()
                            Jumps["Win"] = [a, b]
                        searchObj  = re.search('^本方案累计输\\[(\d+)\\]元跳转到方案\\[(\d+)\\]$',input)
                        if searchObj:
                            (a, b) = searchObj .groups()
                            Jumps["Faild"] = [a, b]
                    Strategy["jumps"] = Jumps
            Jump_idx = Jump_idx + 1
            self.Strategys[Jump_idx] = Strategy           
    def save(self):
        #增加新的section
        self.Strategy = self.textStrategy.get(1.0,END)
        self.url = self.urlEntered.get()
        self.buyno = self.buynoEntered.get()
        self.conf.set("url","value",self.url)
        self.conf.set("buyno","value",self.buyno)
        self.conf.set("Strategy","value",self.Strategy)
        #写回配置文件
        self.conf.write(open("bjpk.txt","w"))
        self.Paser();
        messagebox.showinfo("提示","配置成功！")
        
    def Chosen(self,*args):
        messagebox.showinfo("提示",self.bookChosen.get())
        
    def Close(self):
        if  self.thread != None:
            self.btaction.configure(text='开始')
            if self.thread.is_alive():
                self.thread.stop()
            self.thread.join()
            self.thread = None
        self.destroy()    
    
    
def main():
    app = Application()
    app.title("北京赛车 自动打码神器(开发者QQ：87954657)")
    app.resizable(0,0) #阻止Python GUI的大小调整
    # 主消息循环:
    app.mainloop()
    #driver.close()
    #driver.quit()
if __name__ == "__main__":
    main()
