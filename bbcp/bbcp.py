## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
#BB彩票-双面玩法

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
import threading  
import time

import urllib
import urllib.request
import urllib.response
import urllib.error
import http.cookiejar
import configparser
import ssl
import random
import copy
import re  #python的正则表达式模块
import os
import sys
import wmi
import zlib
import hashlib
import json
import datetime


ssl._create_default_https_context = ssl._create_unverified_context

#本方案累积赢[1000]元跳转到方案[1]
#本方案累积输[1000]元跳转到方案[1]
#input = '1:3.125 false,hello'
#input = '本方案累积赢[1000]元跳转到方案[1]'
#(a, b, c, d) = re.search('^(\d+):([\d.]+) (\w+),(\w+)$',input).groups()
#(a, b) = re.search('^本方案累积赢\\[(\d+)\\]元跳转到方案\\[(\d+)\\]$',input).groups()
#print(a)
#print(b)
#print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


test_flag = False
softname  = "bbcp"
version   = "1.0.0.0"

#headflag => 1:No. 20180424-033, 2:No. 20180424001 3:#No. 1766125
#buyflag  => 1:单面，2：双面
config_cptype = {}
config_cptype["北京PK拾"]   = {"BallNum":10, "headflag":3, "buyflag":2, "bubit":2} #No. 678277
config_cptype["BB PK3"]     = {"BallNum":3,  "headflag":2,  "buyflag":1, "bubit":0} #No. 20180424401
config_cptype["BB 雷电PK"]  = {"BallNum":10, "headflag":2, "buyflag":2, "bubit":0} #No. 20180424111
config_cptype["重庆时时彩"]  = {"BallNum":5, "headflag":1, "buyflag":1, "bubit":0} #No. 20180424-058
config_cptype["新疆时时彩"]  = {"BallNum":5, "headflag":2, "buyflag":1, "bubit":0} #No. 2018042435
config_cptype["新疆时时彩"]  = {"BallNum":5, "headflag":2, "buyflag":1, "bubit":0} #No. 2018042435
config_cptype["天津时时彩"]  = {"BallNum":5,  "headflag":1,  "buyflag":1, "bubit":0} #No. 20180424-042

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

if test_flag == False:
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    #option.add_argument('headless')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    #driver = webdriver.Chrome()
    driver.get("http://www.caiptong.com/")
    #driver.get("http://baidu.com")
else:
    pass;
    
def http_reg(softname, version, phydriverserial, regkey):
    signkey = '&key=0z#z#b#094kls#040jkas892#z#z#b#0' 
    data= {}
    data["softname"]            = softname
    data["version"]             = version
    data["phydriverserial"]     = phydriverserial
    data["regkey"]              = regkey
    keys = sorted(data)
    src  = ""
    for key in keys:
        if len(src):
            src = src + "&"
        src = src + key
        src = src + "="
        src = src + data[key]
    str = src + signkey
    str = str.encode("utf8")
    
    tips = "网络连接错误！"
    m=hashlib.md5()
    m.update( str )
    result = m.hexdigest()
    data   = src.encode("utf8")
    url    = "http://caiptong.com/share/share_registdeviceid?sign=%s"%(result)
    #print(data)
    request = urllib.request.Request(url = url, data = data, headers = headers, method = 'POST')
    try:
        #response = urllib.request.urlopen(request)
        response = opener.open(request, timeout = 5)
        html = response.read().decode()
    except urllib.error.HTTPError as e:
        #print('The server couldn\'t fulfill the request.')
        #print('Error code: ' + str(e.code))
        #print('Error reason: ' + e.reason)
        print("错误","网络连接错误！")
        return False, tips
    except urllib.error.URLError as e:
        #print('We failed to reach a server.')
        #print('Reason: ' + e.reason)
        print("错误","网络连接错误！")
        return False, tips
    '''
    except Exception as msg:
        print("Exception:%s" % msg)
        return False, tips
    except:
        #print("error lineno:" + str(sys._getframe().f_lineno))
        print("错误","网络连接错误！")
        return False, tips
    '''
    html = html.strip()
    #print(html)
    json_data = json.loads(html)
    #{"msg":"登录成功.","success":true,"datas":{"ckregkey":false,"userid":195,"topics":[],"expired":""}}
    if json_data["success"] != True:
        print("错误","账号未注册！")
        if "datas" in json_data:  
            print("错误", json_data["datas"]["notice"])
        return False, tips
    else:
        if "datas" not in json_data:
            return False, tips
        
        datas = json_data["datas"]
        if "ckregkey" not in datas:
            return False, tips
            
        if datas["ckregkey"] == True:
            tips = "注册成功(%s)"%(datas["expired"])
            return True, tips
        elif datas["expired"] == "":
            tips = "注册码不存在"
            return False, tips                
        else:
            tips = "注册码已过期(%s)"%(datas["expired"])
            return False, tips                
        return False

def get_phydriverserial_info(softname):
    tmplist = []
    encrypt_str = ""
    c = wmi.WMI ()
    for cpu in c.Win32_Processor():
        #cpu 序列号
        encrypt_str = encrypt_str+cpu.ProcessorId.strip()
        #print ("cpu id:", cpu.ProcessorId.strip())
    for physical_disk in c.Win32_DiskDrive():
        encrypt_str = encrypt_str+physical_disk.SerialNumber.strip()
        #硬盘序列号
        #print ('disk id:', physical_disk.SerialNumber.strip())
    for board_id in c.Win32_BaseBoard():
        #主板序列号
        encrypt_str = encrypt_str+board_id.SerialNumber.strip()
        #print ("main board id:",board_id.SerialNumber.strip())
    for bios_id in c.Win32_BIOS():
        #bios 序列号
        encrypt_str = encrypt_str+bios_id.SerialNumber.strip()
        #print ("bios number:", bios_id.SerialNumber.strip())
    #print(encrypt_str)
    encrypt_str = softname + encrypt_str
    m = hashlib.md5()
    m.update(encrypt_str.encode(encoding='UTF-8'))
    encrypt_str = m.hexdigest()
    #print(encrypt_str)
    return encrypt_str


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
        tf = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(tf + log)
        self.target.textlog.insert(tk.INSERT, tf + log + "\n")

    def delBallNo(self, road, buyno, BALL_NO_DATA):
        #Temp_Strategy         = BALL_NO_DATA["Temp_Strategy"]
        #Temp_Monery           = BALL_NO_DATA["Temp_Monery"]
        #Temp_Win              = BALL_NO_DATA["Temp_Win"]
        #Temp_Strategy_Win     = BALL_NO_DATA["Temp_Strategy_Win"]
        #Temp_Rule             = BALL_NO_DATA["Temp_Rule"]
        #Temp_Rule_Idx         = BALL_NO_DATA["Temp_Rule_Idx"]
        #BALL_NO_DATA["Temp_Cut"]             =  0
        #BALL_NO_DATA["Temp_Cut_Flag"]        =  0
        #self.cutin  = self.target.cutin.get()
        #self.cutout = self.target.cutout.get()

        self.logprint("位置" + str(buyno) + "***当前方案***:" + str(BALL_NO_DATA["Temp_Strategy"]["Jump_idx"]))

        Win = 0
    
        #处理中奖结果
        if BALL_NO_DATA["Temp_Rule"] != None:
            if  BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] in road[buyno - 1]:
                Win = 1
                BALL_NO_DATA["Temp_Win"]              = BALL_NO_DATA["Temp_Win"] + int(BALL_NO_DATA["Temp_Monery"][1])
                BALL_NO_DATA["Temp_Strategy_Win"]     = BALL_NO_DATA["Temp_Strategy_Win"] + int(BALL_NO_DATA["Temp_Monery"][1])
                BALL_NO_DATA["Temp_Cut"]              = BALL_NO_DATA["Temp_Cut"] + int(BALL_NO_DATA["Temp_Monery"][1])

                if BALL_NO_DATA["Temp_Cut_Flag"] == 1:
                    BALL_NO_DATA["Temp_CutIn"]              = BALL_NO_DATA["Temp_CutIn"] + int(BALL_NO_DATA["Temp_Monery"][1])

                self.logprint("位置" + str(buyno) + "***中奖***金额:" + BALL_NO_DATA["Temp_Monery"][1])
            else:
                Win = 0
                BALL_NO_DATA["Temp_Win"]              = BALL_NO_DATA["Temp_Win"] - int(BALL_NO_DATA["Temp_Monery"][1])
                BALL_NO_DATA["Temp_Strategy_Win"]     = BALL_NO_DATA["Temp_Strategy_Win"] - int(BALL_NO_DATA["Temp_Monery"][1])
                BALL_NO_DATA["Temp_Cut"]              = BALL_NO_DATA["Temp_Cut"] - int(BALL_NO_DATA["Temp_Monery"][1])
                
                if BALL_NO_DATA["Temp_Cut_Flag"] == 1:
                    BALL_NO_DATA["Temp_CutIn"]              = BALL_NO_DATA["Temp_CutIn"] - int(BALL_NO_DATA["Temp_Monery"][1])

                self.logprint("位置" + str(buyno) + "***未中奖***")
            
            self.logprint("位置" + str(buyno) + "***当前输赢:" + str(BALL_NO_DATA["Temp_Win"]))
            self.logprint("位置" + str(buyno) + "***当前方案输赢:" + str(BALL_NO_DATA["Temp_Strategy_Win"]))
            self.logprint("位置" + str(buyno) + "***当前切入切出输赢:" + str(BALL_NO_DATA["Temp_Cut"]))
            self.logprint("位置" + str(buyno) + "***当前切入输赢:" + str(BALL_NO_DATA["Temp_CutIn"]))
            
            ##[1, 10, 2, 2]    
            for monery in BALL_NO_DATA["Temp_Strategy"]["monerys"]:
                if  Win == 1 and monery[0] == BALL_NO_DATA["Temp_Monery"][2]:
                    BALL_NO_DATA["Temp_Monery"] = monery
                    break
                elif  Win == 0 and monery[0] == BALL_NO_DATA["Temp_Monery"][3]:
                    BALL_NO_DATA["Temp_Monery"] = monery
                    break
            self.logprint("位置" + str(buyno) + "***当前方案输赢:" + str(BALL_NO_DATA["Temp_Strategy_Win"]))
            #Win = [1000, 1]    
            if BALL_NO_DATA["Temp_Strategy_Win"] > int(BALL_NO_DATA["Temp_Strategy"]["jumps"]["Win"][0]):
                BALL_NO_DATA["Temp_Strategy_Win"] = 0
                BALL_NO_DATA["Temp_Strategy"] = self.Strategys[int(BALL_NO_DATA["Temp_Strategy"]["jumps"]["Win"][1])]
                BALL_NO_DATA["Temp_Rule"]     = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0
                BALL_NO_DATA["Temp_Monery"]   = BALL_NO_DATA["Temp_Strategy"]["monerys"][0]

                self.logprint("位置" + str(buyno) + "***本方案累积赢跳转***" + str(BALL_NO_DATA["Temp_Strategy"]["Jump_idx"]))
                        
            #Faild = [1000, 1]    
            elif BALL_NO_DATA["Temp_Strategy_Win"] < -int(BALL_NO_DATA["Temp_Strategy"]["jumps"]["Faild"][0]):
                BALL_NO_DATA["Temp_Strategy_Win"] = 0
                BALL_NO_DATA["Temp_Strategy"] = self.Strategys[int(BALL_NO_DATA["Temp_Strategy"]["jumps"]["Faild"][1])]
                BALL_NO_DATA["Temp_Rule"]     = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0
                BALL_NO_DATA["Temp_Monery"]   = BALL_NO_DATA["Temp_Strategy"]["monerys"][0]
                
                self.logprint("位置" + str(buyno) + "***本方案累积输跳转***" + str(BALL_NO_DATA["Temp_Strategy"]["Jump_idx"]))

            #切入切出
            if self.cutout != 0 and BALL_NO_DATA["Temp_Cut"] > 0 and BALL_NO_DATA["Temp_Cut"] > self.cutout:
                self.logprint("位置" + str(buyno) + "***切出***" + str(BALL_NO_DATA["Temp_Cut"]))
                BALL_NO_DATA["Temp_Cut"] = 0
                BALL_NO_DATA["Temp_Cut_Flag"] = 0
            elif  self.cutin != 0 and BALL_NO_DATA["Temp_Cut"] < 0 and BALL_NO_DATA["Temp_Cut"] < -self.cutin:
                self.logprint("位置" + str(buyno) + "***切入***" + str(BALL_NO_DATA["Temp_Cut"]))
                BALL_NO_DATA["Temp_Cut"] = 0
                BALL_NO_DATA["Temp_Cut_Flag"] = 1

        else:
            self.logprint("位置" + str(buyno) + "***未下注***")

        #处理中奖结果

        if BALL_NO_DATA["Temp_Rule"] != None:
            BALL_NO_DATA["Temp_Rule_Idx"] = BALL_NO_DATA["Temp_Rule_Idx"] + 1
            if len(BALL_NO_DATA["Temp_Rule"][1]) <= BALL_NO_DATA["Temp_Rule_Idx"]:
                BALL_NO_DATA["Temp_Rule"] = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0

            #不回揽
            if self.backup == 0:
                self.logprint("位置" + str(buyno) + "***不回揽***")
                pass
            #中回揽
            elif self.backup == 1 and Win == 1:
                BALL_NO_DATA["Temp_Rule"] = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0
                self.logprint("位置" + str(buyno) + "***中回揽***")
            #错回揽
            elif self.backup == 2 and Win == 1:
                BALL_NO_DATA["Temp_Rule"] = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0
                self.logprint("位置" + str(buyno) + "***错回揽***")
           
        #处理路单规则
                             
        if BALL_NO_DATA["Temp_Rule"] == None:
            keys = sorted(self.roads)
            tmp  = ""
            for key in keys:
                tmp = tmp + str(self.roads[key][buyno - 1])

            self.logprint("位置" + str(buyno) + "***当前路单***" + tmp)

            for rule in BALL_NO_DATA["Temp_Strategy"]["rules"]:
                #[大大， 小小]
                rule0 = rule[0]
                self.logprint("位置" + str(buyno) + "***查找规则***" + rule0)
                len_keys  = len(keys)
                len_rule0 = len(rule0)
                isEqual   = False
                if len_keys >= len_rule0:
                    isEqual = True
                    start   = len_keys - len_rule0
                    for idx in range(0, len_rule0):
                        #[大， 双]
                        _isEqual = False
                        roadKey  = keys[start + idx]
                        for item in self.roads[roadKey][buyno - 1]:
                            if item == rule0[idx]:
                                _isEqual = True
                        if _isEqual == False:
                            isEqual = False
                            break
                if isEqual:
                    BALL_NO_DATA["Temp_Rule"]     = rule
                    BALL_NO_DATA["Temp_Rule_Idx"] = 0
                    self.logprint("位置" + str(buyno) + "***规则符合条件***" + str(rule[0]) + "=" + str(rule[1]))
                    break
                else:
                    self.logprint("位置" + str(buyno) + "***规则不符合条件***" + str(rule[0]) + "=" + str(rule[1]))  
                    pass 
        else: 
            self.logprint("位置" + str(buyno) + "***回揽未结束***")
            pass
                      
        #双面玩法

        if BALL_NO_DATA["Temp_Rule"] != None:
            if test_flag == False :
                if BALL_NO_DATA["Temp_Cut_Flag"] == 1:
                    if config_cptype[self.cptype]["buyflag"] == 1:
                        if BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] == "大":
                            driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div/div[2]/button[1]").click()
                        elif BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] == "小":
                            driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div/div[2]/button[2]").click()
                        elif BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] == "单":
                            driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div/div[2]/button[3]").click()
                        elif BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] == "双":
                            driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div/div[2]/button[4]").click()
                        else:
                            self.logprint("***不支持类型***") 
                    elif config_cptype[self.cptype]["buyflag"] == 2:
                        if BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] == "大":
                            driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div[1]/div[2]/button[1]").click()
                        elif BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] == "小":
                            driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div[1]/div[2]/button[2]").click()
                        elif BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] == "单":
                            driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div[1]/div[2]/button[3]").click()
                        elif BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] == "双":
                            driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div[1]/div[2]/button[4]").click()
                        else:
                            self.logprint("***不支持类型***")
                    else:
                        self.logprint("***类型不支持***")
                        pass
                else:
                    self.logprint("***模拟买入***")
                    pass;
            else:
                self.logprint("***测试数据买入***")
                pass;

            self.logprint("位置" + str(buyno) + "***购买:" + BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] + "金额：" + str(BALL_NO_DATA["Temp_Monery"][1]))

            if test_flag == False:
                if BALL_NO_DATA["Temp_Cut_Flag"] == 1:
                    time.sleep(1)
                    driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[4]/div[1]/div[1]/input").clear()
                    time.sleep(1)
                    driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[4]/div[1]/div[1]/input").send_keys(BALL_NO_DATA["Temp_Monery"][1])
                    time.sleep(1)
                    driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[4]/div[1]/div[1]/button").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[4]/div[2]/button[3]").click()
                else:
                    self.logprint("***模拟买入***")
                    pass
            else:
                self.logprint("***测试数据数据***")
                pass

    def target_func(self):
    
        print("**********target_func begin***********")

        self.logprint("位置:" + self.target.buyno)
        buynos = self.target.buyno.split(",")
        if len(buynos) <= 0:
            self.logprint("错误 ==> 购买位置配置出错")
            return
        
        self.backup = self.target.backup.get()
        self.Strategys = copy.deepcopy(self.target.Strategys)

        if len(self.Strategys) <= 0:
            self.logprint("错误 ==> 方案配置出错")
            return

        self.cutin  = self.target.cutin.get()
        self.cutout = self.target.cutout.get()
        
        self.cptype = self.target.cptype.get()


        print(self.Strategys)  
                 
        if test_flag == False:
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
                '''
                except Exception as msg:
                    self.logprint("Exception:%s" % msg)
                    pass
                except:
                    self.logprint("error lineno:" + str(sys._getframe().f_lineno))
                    pass
                '''
        else:
            pass
        
        Last_Award_Issue = ""
        Last_Award_Issue_Have = False
        self.roads = {}

        BALL_NO_DATAS = {}
        for buyno in buynos:
            BALL_NO_DATA = {}
            BALL_NO_DATA["Temp_Strategy"]        =  self.Strategys[1]
            BALL_NO_DATA["Temp_Monery"]          =  self.Strategys[1]["monerys"][0]
            BALL_NO_DATA["Temp_Win"]             =  0
            BALL_NO_DATA["Temp_Strategy_Win"]    =  0
            BALL_NO_DATA["Temp_Rule"]            =  None
            BALL_NO_DATA["Temp_Rule_Idx"]        =  0

            BALL_NO_DATA["Temp_Cut"]             =  0
            if self.cutin == 0:
                BALL_NO_DATA["Temp_Cut_Flag"]    =  1
            else:
                BALL_NO_DATA["Temp_Cut_Flag"]    =  0
            BALL_NO_DATA["Temp_CutIn"]           =  0
            BALL_NO_DATAS[buyno]                 =  BALL_NO_DATA

        if test_flag == False:
            pass
        else:
            Test_no = 0

        SleepTime  = 5        
        while self.stopped == False:
            try:
                SleepTime = SleepTime + 1
                if SleepTime < 5:
                    time.sleep(1)
                    continue
                SleepTime = 0  
                self.logprint("**********************************************")
                #              No. 20180603-114
                #headflag => 1:No. 20180424-033, 
                #headflag => 2:No. 20180422001  
                #headflag => 3:No. 1766125
                if config_cptype[self.cptype]["headflag"] == 1:
                    headflag = "No. " + datetime.datetime.now().strftime('%Y%m%d') + "-"
                elif config_cptype[self.cptype]["headflag"] == 2:
                    headflag = "No. " + datetime.datetime.now().strftime('%Y%m%d')
                elif config_cptype[self.cptype]["headflag"] == 3:
                    headflag = "No. "
                else:
                    self.logprint("***类型未处理***")   
                    continue
                
                
                if test_flag == False:
                    Cur_Award_Issue1 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[2]/div[2]").text
                    Cur_Award_Issue2 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[1]").text
                else:
                    Cur_Award_Issue1  = headflag + str(2 + Test_no)
                    Cur_Award_Issue2  = headflag + str(1 + Test_no)
                    Test_no = Test_no + 1

                if Cur_Award_Issue1 == "" or Cur_Award_Issue2 == "":
                    self.logprint("***等待开奖***")   
                    continue
                    
                #print("headflag:" + headflag)
                #print("Cur_Award_Issue1:" + Cur_Award_Issue1)
                #print("Cur_Award_Issue2:" + Cur_Award_Issue2)

                Cur_Award_Issue1 = Cur_Award_Issue1.replace(headflag, "")
                Cur_Award_Issue2 = Cur_Award_Issue2.replace(headflag, "")

                
                if int(Cur_Award_Issue2) + 1 != int(Cur_Award_Issue1):
                    self.logprint("***等待开奖***")   
                    continue
                    
                if Last_Award_Issue != "" and int(Last_Award_Issue) != int(Cur_Award_Issue2):
                    self.logprint("***等待开奖***")   
                    continue

                self.logprint("*******获取开奖结果**********")
                    
                def GetType(BallNo):
                    type1 = "大"
                    if int(BallNo) > 5:
                        type1 = '大'
                    else:
                        type1 = '小'
                        
                    type2 = "单"        
                    if int(BallNo) % 2 == 1:
                        type2 = '单'
                    else:
                        type2 = '双'
                    return [type1, type2]

                Cur_Award_Issue2_Road = []    
                if test_flag == False:
                    for BallIdx in range(1, config_cptype[self.cptype]["BallNum"] + 1):
                        BallText = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[2]/span[" + str(BallIdx) + "]").text
                        if BallText == "":
                            self.logprint("***数据还在加载中***")   
                            break;
                        Cur_Award_Issue2_Road.append(GetType(BallText))
                else:
                    for BallIdx in range(1, config_cptype[self.cptype]["BallNum"] + 1):
                        BallText = str(random.randint(1,10))
                        if BallText == "":
                            self.logprint("***数据还在加载中***")   
                            break;
                        Cur_Award_Issue2_Road.append(GetType(BallText))

                if config_cptype[self.cptype]["BallNum"] != len(Cur_Award_Issue2_Road):
                    self.logprint("***数据还在加载中***")   
                    continue

                self.roads[Cur_Award_Issue2] = Cur_Award_Issue2_Road

                if test_flag == False:
                    for idx  in range(1,5):
                        Award_Issue = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[1]").text
                        Award_Issue_Road = []
                        for BallIdx in range(1, config_cptype[self.cptype]["BallNum"]):
                            BallText = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) + "]/div[2]/span[" + str(BallIdx) + "]").text
                            Award_Issue_Road.append(GetType(BallText))
                        
                        if config_cptype[self.cptype]["bubit"] > 0:
                            Award_Issue = Cur_Award_Issue2[0:config_cptype[self.cptype]["bubit"]] + Award_Issue
                        self.roads[Award_Issue] = Award_Issue_Road   
                else:
                    pass
                
                for item in self.roads: 
                    print(item + str(self.roads[item]))
    
                Last_Award_Issue = Cur_Award_Issue1

                for buyno in buynos:
                    self.delBallNo(Cur_Award_Issue2_Road, int(buyno), BALL_NO_DATAS[buyno])

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
            except:
                self.logprint("error lineno:" + str(sys._getframe().f_lineno))
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
        self.conf.read("bbcp.txt")

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

        self.pump = IntVar()
        if self.conf.has_section("pump") == True:
            self.pump.set(int(self.conf.get("pump", "value")))
        else:
            self.pump.set(0)
            self.conf.add_section("pump")
            self.conf.set("pump", "value", "0")

        self.backup = IntVar()
        if self.conf.has_section("backup") == True:
            self.backup.set(int(self.conf.get("backup", "value")))
        else:
            self.backup.set(0)
            self.conf.add_section("backup")
            self.conf.set("backup", "value", "0")

        self.cutout = IntVar()
        if self.conf.has_section("cutout") == True:
            self.cutout.set(int(self.conf.get("cutout", "value")))
        else:
            self.cutout.set(1000)
            self.conf.add_section("cutout")
            self.conf.set("cutout", "value", "1000")

        self.cutin = IntVar()
        if self.conf.has_section("cutin") == True:
            self.cutin.set(int(self.conf.get("cutin", "value")))
        else:
            self.cutin.set(1000)
            self.conf.add_section("cutin")
            self.conf.set("cutin", "value", "1000")  

        ##############
        phydriverserial = get_phydriverserial_info(softname)
        
        self.regcode = tk.StringVar()  
        if self.conf.has_section("regcode") == True:
            self.regcode.set(self.conf.get("regcode", "value"))
        else:
            self.regcode.set(phydriverserial)
            self.conf.add_section("regcode")
            self.conf.set("regcode", "value", phydriverserial)  
            
        self.phydriverserial = tk.StringVar()   
        if self.conf.has_section("phydriverserial") == True:
            self.phydriverserial.set(self.conf.get("phydriverserial", "value"))
        else:
            self.phydriverserial.set(phydriverserial)
            self.conf.add_section("phydriverserial")
            self.conf.set("phydriverserial", "value", phydriverserial)  

        #不相等，则重置
        if self.phydriverserial.get() != phydriverserial:
            self.phydriverserial.set(phydriverserial)
            self.regcode.set(phydriverserial)
            
            
            
        self.tips = tk.StringVar()  
        ##############
        self.createWidgets()
        self.regMe();
        self.enterMe();


    def createWidgets(self):
        # Tab Control introduced here --------------------------------------
        self.tabControl = ttk.Notebook(self)          # Create Tab Control
        self.tab1 = ttk.Frame(self.tabControl)        # Create a tab
        self.tab2 = ttk.Frame(self.tabControl)        # Create a tab
        self.tabControl.add(self.tab1, text='操作区')  # Add the tab
        self.tabControl.add(self.tab2, text='注册')  # Add the tab
        self.tabControl.pack(expand=1, fill="both")   # Pack to make visible
        # ~ Tab Control introduced here
        # -----------------------------------------
        # Using a scrolled Text control
        self.scrolW = 60
        self.scrolH = 15
        self.createTab1()
        self.createTab2()

    def regMe(self):
        self.conf.set("phydriverserial","value",self.phydriverserial.get())
        self.conf.set("regcode","value",self.regcode.get())        
        #写回配置文件
        self.conf.write(open("bbcp.txt","w"))
        self.reg = False;
        self.reg, tips = http_reg(softname, version, self.phydriverserial.get(), self.regcode.get())
        self.reg = True
        self.tips.set(tips)
    
    def createTab2(self):   
        #---------------Tab2控件介绍------------------#
        # Modified Button Click Function
        # We are creating a container tab3 to hold all other widgets
        self.MyFrame2 = ttk.LabelFrame(self.tab2, text='操作区')
        self.MyFrame2.grid(column=0, row=0, padx=8, pady=4, sticky=E+W)
        
        #行
        line = 0
        # Changing our Label
        ttk.Label(self.MyFrame2, text="机器码:").grid(column=0, row=line, sticky='W')  
        
        # Adding a Textbox Entry widget
        self.phydriverserialEntered = ttk.Entry(self.MyFrame2, width=75, state='readonly', textvariable=self.phydriverserial)  
        self.phydriverserialEntered.grid(column=1, row=line, sticky='W', columnspan=3)
        
        line = line + 1
        # Changing our Label
        ttk.Label(self.MyFrame2, text="").grid(column=0, row=line, sticky='W')  

        line = line + 1
        # Changing our Label
        ttk.Label(self.MyFrame2, text="注册码:").grid(column=0, row=line, sticky='W')  

        # Adding a Textbox Entry widget
        self.regcodeEntered = ttk.Entry(self.MyFrame2, width=75, textvariable=self.regcode)  
        self.regcodeEntered.grid(column=1, row=line, sticky='W', columnspan=3)

        line = line + 1
        # Changing our Label
        ttk.Label(self.MyFrame2, text="").grid(column=0, row=line, sticky='W', columnspan=3) 

        line = line + 1
        # Changing our Label
        ttk.Label(self.MyFrame2, text="", textvariable=self.tips, background='red', compound = 'right').grid(column=0, row=line, sticky='W', columnspan=3) 

        line = line + 1
        self.btreg = ttk.Button(self.MyFrame2,text="注册",width=10,command=self.regMe)
        self.btreg.grid(column=3, row=line, sticky='E')   
  
    def createTab1(self):
        #---------------Tab1控件介绍------------------#
        # Modified Button Click Function
        # We are creating a container tab3 to hold all other widgets
        self.MyFrame1 = ttk.LabelFrame(self.tab1, text='操作区')
        self.MyFrame1.grid(column=0, row=0, padx=8, pady=4, sticky=W)
        #行
        line = 0
        # Changing our Label
        ttk.Label(self.MyFrame1, text="地址:").grid(column=0, row=line, sticky='W')  

        # Adding a Textbox Entry widget
        self.urlEntered = ttk.Entry(self.MyFrame1, width=60, textvariable=self.url)  
        self.urlEntered.grid(column=1, row=line, sticky='W')

        self.btenter = ttk.Button(self.MyFrame1,text="进入",width=10,command=self.enterMe)
        self.btenter.grid(column=2,row=line,sticky='E')  
    
        #行
        line = line + 1
        # Changing our Label
        ttk.Label(self.MyFrame1, text="彩票类型:").grid(column=0, row=line, sticky='W')  
        
        mytype = ()
        for key in config_cptype:
            temp   = (key, )
            mytype = mytype + temp

        # 创建一个下拉列表
        self.cptype = tk.StringVar()
        self.cptypeChosen = ttk.Combobox(self.MyFrame1, width=12, textvariable=self.cptype)
        self.cptypeChosen['values'] = mytype     # 设置下拉列表的值
        self.cptypeChosen.grid(column=1, row=line,sticky='WE',columnspan=3)      # 设置其在界面中出现的位置  column代表列   row 代表行
        self.cptypeChosen.current(0)    # 设置下拉列表默认显示的值，0为 cptypeChosen['values'] 的下标值        
        
        #行
        line = line + 1
        # Changing our Label
        ttk.Label(self.MyFrame1, text="购买位置:").grid(column=0, row=line, sticky='W')  
  
        # Adding a Textbox Entry widget
        self.buynoEntered = ttk.Entry(self.MyFrame1, width=60, textvariable=self.buyno)  
        self.buynoEntered.grid(column=1, row=line, sticky='W')             
        #行
        line = line + 1
        ttk.Label(self.MyFrame1, text="配置信息(大小单双)").grid(column=0,row=line,sticky='W',columnspan=3)
        #行
        line = line + 1
        self.textStrategy = scrolledtext.ScrolledText(self.MyFrame1,width=self.scrolW,height=self.scrolH,wrap=tk.WORD)
        self.textStrategy.grid(column=0,row=line,sticky='WE',columnspan=3)
        
        #行
        line = line + 1
        cbtpump = Checkbutton(self.MyFrame1, text = "抽水", variable = self.pump, command = self.processCheckbutton)
        cbtpump.grid(row = line, column = 0)  
        #行
        line = line + 1
        backUp0 = Radiobutton(self.MyFrame1, text = "不回揽", bg = "red", variable = self.backup, value = 0, command = self.processRaidobutton)
        backUp1 = Radiobutton(self.MyFrame1, text = "中回揽", bg = "yellow", variable=self.backup, value = 1, command = self.processRaidobutton)
        backUp2 = Radiobutton(self.MyFrame1, text = "错回揽", bg = "blue", variable=self.backup, value = 2, command = self.processRaidobutton)
        backUp0.grid(row=line, column=0)
        backUp1.grid(row=line, column=1)
        backUp2.grid(row=line, column=2)

        #行
        line = line + 1
        # Changing our Label
        ttk.Label(self.MyFrame1, text="赢切出:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget
        self.cutoutEntered = ttk.Entry(self.MyFrame1, width=60, textvariable=self.cutout)  
        self.cutoutEntered.grid(column=1, row=line, sticky='W')

        #行
        line = line + 1
        # Changing our Label
        ttk.Label(self.MyFrame1, text="输切入:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget
        self.cutinEntered = ttk.Entry(self.MyFrame1, width=60, textvariable=self.cutin)  
        self.cutinEntered.grid(column=1, row=line, sticky='W')           
        #行
        # Adding a Button
        line = line + 1
        self.btsave = ttk.Button(self.MyFrame1,text="保存",width=10,command=self.saveMe)
        self.btsave.grid(column=2,row=line,sticky='E')   
        #行
        line = line + 1
        ttk.Label(self.MyFrame1,text="日志信息:").grid(column=0,row=line,sticky='W')
        #行
        line = line + 1
        self.textlog = scrolledtext.ScrolledText(self.MyFrame1,width=self.scrolW,height=5,wrap=tk.WORD)
        self.textlog.grid(column=0,row=line,sticky='WE',columnspan=3)
        #行
        # Adding a Button
        line = line + 1
        self.btaction = ttk.Button(self.MyFrame1,text="开始",width=10,command=self.clickMe)
        self.btaction.grid(column=2,row=line,sticky='E')  
        
        # 一次性控制各控件之间的距离
        for child in self.MyFrame1.winfo_children(): 
            child.grid_configure(padx=3,pady=1)
        # 单独控制个别控件之间的距离
        #---------------Tab1控件介绍------------------#
        
        self.urlEntered.insert(END,self.url)
        self.buynoEntered.insert(END,self.buyno)
        self.textStrategy.insert(tk.INSERT,self.Strategy)

    def processCheckbutton(self):
        pass
    def processRaidobutton(self):
        pass

    def enterMe(self):
        self.url = self.urlEntered.get()
        if self.url != "":
            if test_flag == False:
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
        
        if self.Paser() == False:
            messagebox.showinfo("提示","方案配置有问题！")
            return  

        if self.reg == False and test_flag == False:
            messagebox.showinfo("提示","注册码已经过期!")
            return
            
        self.btaction.configure(text='关闭')
        self.thread = BettingThread(self)
        self.thread.start()

    def Paser(self):
        Jump_idx = 0
        self.Strategys = {}
        self.Strategy = self.textStrategy.get(1.0,END)
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
                    lines = inblock.split("\n")
                    if len(lines)==0:
                        return False
                    for line in lines:
                        rule = re.split('=', line)
                        rules.append(rule) 
                    Strategy["rules"] = rules
                elif "monerys" not in Strategy:
                    monerys = []
                    lines = inblock.split("\n")
                    if len(lines)==0:
                        return False
                    for line in lines:
                        monery = re.split('=',line)
                        monerys.append(monery) 
                    Strategy["monerys"] = monerys
                elif "jumps" not in Strategy:
                    Jumps = {}
                    #本方案累积赢[1000]元跳转到方案[1]
                    #本方案累积输[1000]元跳转到方案[1]
                    lines = inblock.split("\n")
                    if len(lines)==0:
                        return False
                    for line in lines:
                        searchObj  = re.search('^本方案累积赢\\[(\d+)\\]元跳转到方案\\[(\d+)\\]$',line)
                        if searchObj:
                            (a, b) = searchObj .groups()
                            Jumps["Win"] = [a, b]
                        searchObj  = re.search('^本方案累积输\\[(\d+)\\]元跳转到方案\\[(\d+)\\]$',line)
                        if searchObj:
                            (a, b) = searchObj .groups()
                            Jumps["Faild"] = [a, b]
                    Strategy["jumps"] = Jumps
            Jump_idx = Jump_idx + 1
            Strategy["Jump_idx"]     = Jump_idx
            self.Strategys[Jump_idx] = Strategy
        return True    
        
    def saveMe(self):
        #增加新的section
        self.Strategy = self.textStrategy.get(1.0,END)
        self.url      = self.urlEntered.get()
        self.buyno    = self.buynoEntered.get()
        self.conf.set("url","value",self.url)
        self.conf.set("buyno","value",self.buyno)
        self.conf.set("Strategy","value",self.Strategy)
            
        self.conf.set("pump","value",str(self.pump.get()))
        self.conf.set("backup","value",str(self.backup.get()))
        self.conf.set("cutin","value",str(self.cutin.get()))
        self.conf.set("cutout","value",str(self.cutout.get()))
        
        #写回配置文件
        self.conf.write(open("bbcp.txt","w"))
        if self.Paser() == False:
            messagebox.showinfo("提示","方案配置有问题！")
            return  
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
    app.title("BB彩票-双面玩法(开发者QQ：87954657)")
    app.resizable(0,0) #阻止Python GUI的大小调整
    # 主消息循环:
    app.mainloop()
    if test_flag == False:
        driver.close()
        driver.quit()
    else:
        pass;

if __name__ == "__main__":
    main()
