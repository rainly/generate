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
import ssl
import configparser
import random
import hashlib
from bs4 import BeautifulSoup  # 引入beautifulsoup 解析html事半功倍
from collections import deque
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
from copy import deepcopy
from aip import AipOcr
from PIL import *
# allows for image formats other than gif
from PIL import Image, ImageTk
import logging
from logging import handlers


ssl._create_default_https_context = ssl._create_unverified_context




""" 你的 APPID AK SK """
#APP_ID = '11249600'
#API_KEY = 'oCy0me9K6h9D19PxDA5ESLj5'
#SECRET_KEY = '2aPGdXMfq63ypzrR0lPiKmG6dKD8UaKh '

APP_ID = '11283483'
API_KEY = 'K5PIp9qko5UFOZxOyvbV5EwK'
SECRET_KEY = 'LA5wxlyBW7rfuQxzHKAGICz2oFdjsQRC  '

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)





class Logger(object):
    #日志级别关系映射
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }

    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        sh.setLevel(logging.INFO)
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        th.setLevel(logging.INFO)
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)
    
log = Logger('all.log',level='debug')


def logdebug(msg, *args, **kwargs):
    log.logger.debug(msg, *args, **kwargs)
    
def loginfo(msg, *args, **kwargs):
    log.logger.info(msg, *args, **kwargs)
    
def logwarning(msg, *args, **kwargs):
    log.logger.warning(msg, *args, **kwargs)
    
def logerror(msg, *args, **kwargs):
    kwargs["exc_info"] = 1
    log.logger.error(msg, *args, **kwargs)

def logcrit(msg, *args, **kwargs):
    kwargs["exc_info"] = 1
    log.logger.crit(msg, *args, **kwargs)




""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()





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
    for key in all_the_oc["game_type"]:
        if all_the_oc["game_type"][key] == gname:
            return key
    return ""
    

#def application(environ, start_response):
#    start_response('200 OK', [('Content-Type', 'text/html')])
#    return [u"hello".encode('utf8')]
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
#httpd = make_Betting('', 8000, application)
#print ("Serving HTTP on port 8000...")


g_mutex = threading.Lock()
g_datas = []

    

#声明一个CookieJar对象实例来保存cookie
cookiejar = http.cookiejar.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookiejar)
#通过handler来构建opener
opener = urllib.request.build_opener(handler)

#此处的open方法同urllib2的urlopen方法，也可以传入request
#response = opener.open('http://www.baidu.com')
user_agent = 'Mozilla/5.0 (Windows NT 6.1 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'  
headers = { 'User-Agent' : user_agent }  

def GetHttp(url, data = None, headers = {}, method = 'GET'):    
    request = urllib.request.Request(url, headers = headers, data = data, method = method)
    try:
        response = opener.open(request, timeout = 5)
        html = response.read().decode()
    except urllib.error.HTTPError as e:
        logerror("HTTPError :", e.reason)
        return None
    except urllib.error.URLError as e:
        logerror("URLError :", e.reason)
        return None
    except Exception as e:
        logerror("Exception:%s" % (e))
        return None
    except:
        logerror("网络连接错误！")
        return None
    html = html.strip()
    logdebug(html)
    return html
    



timeSMS = []
def sendSMS(phone):
    global timeSMS
    now = time.time()
    now = int(round(now))
    timeSMS.append(now)
        
    expnum = 0
    for item in timeSMS:
        if item > now - 600:
            expnum = expnum + 1
    
    if expnum < 10:
        loginfo("发送太频繁，不发送:" + str(expnum))
        return False
        
    timeSMS = []
    
    signkey = '&key=0z#z#b#094kls#040jkas892#z#z#b#0' 
    data= {}
    data["phone"] = phone
    data["now"]   = now
    keys = sorted(data)
    src  = ""
    for key in keys:
        if len(src):
            src = src + "&"
        src = src + key
        src = src + "="
        src = src + str(data[key])
    tstr = src + signkey
    tstr = tstr.encode("utf8")
    
    tips = "网络连接错误！"
    m=hashlib.md5()
    m.update( tstr )
    result = m.hexdigest()
    data   = src.encode("utf8")
    data   = bytes.decode(data)
    data   = data + "&sign=" + result
    
    ##url = "http://duboren.com/api_sms/sms.php?%s"%(str(data))
    url = "http://duboren.com/api_sms/sms.php?%s"%(str(data))
    logdebug(url)
    html = GetHttp(url, headers = headers)
    if html == None:
        return False
    logdebug(html)
    return True

            
class ServerThread(threading.Thread):
    def __init__(self, target, thread_num=0, timeout=5.0):
        super(ServerThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout
    def run(self):
        logdebug('Thread start\n')   
        while self.stopped == False:    
            try:        
                self.target_func()
                sleeptime   = 0
                sleepdelay  = 30
                trynum      = 0
                while self.stopped == False:
                    loginfo('代理尝试登录中(%d/%d)\n'%(sleeptime, sleepdelay))
                    time.sleep(1)
                    sleeptime = sleeptime + 1
                    if sleeptime < sleepdelay:
                        continue
                    sleepdelay = sleepdelay + 30
                    if sleepdelay > 300:
                        sleepdelay = 300
                    trynum = trynum + 1
                    self.target.ser_interMe()
                    if self.target.ser_loginMe(False) != True:
                        sleeptime = 0;
                        #登录失败发送短信通知
                        if trynum % 10 == 0:
                            sendSMS(self.target.conf_phone.get())
                    else:
                        break;
            except:
                logerror("error lineno:" + str(sys._getframe().f_lineno))
        logdebug('Thread stopped'+ "\n")

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped
    

        
    def target_func(self):
        logdebug("target_func begin")
        sleeptime = 5
        syncUserNum   = 3600
        while self.stopped == False:
            sleeptime = sleeptime + 1
            syncUserNum = syncUserNum + 1
            if sleeptime < 5:
                time.sleep(1)
                continue
            sleeptime = 0
            logdebug(syncUserNum)
            if self.target.conf_ck.get() == 1 and syncUserNum >= 3600:
                syncUserNum = 0;
                self.target.syncUser();
                
            g_mutex.acquire()    
            t_users = deepcopy(self.target.users)
            g_mutex.release()
            
            t_datas = []
            for user in t_users:
                if self.stopped:
                    break
                loginfo("############################查询详细##############################" + user) 
                #https://00271596-xsj.cp168.ws/agent/report/bets?username=zhw999&lottery=BJPK10%2CCQSSC%2CPK10JSC%2CLUCKYSB%2CSSCJSC%2CGDKLSF%2CGXK3%2CXYNC%2CKL8%2CXJSSC%2CTJSSC%2CBJPK10BJL%2CGXKLSF%2CGD11X5%2CPCEGG%2CAULUCKY20%2CAULUCKY10%2CAULUCKY5%2CAULUCKY8%2CHK6&begin=2018-03-25&end=2018-03-25&settle=false
                t = time.time()
                url = self.target.ser_url.get() + "agent/report/bets?username=" + user + "&lottery=BJPK10%2CCQSSC%2CPK10JSC%2CLUCKYSB%2CSSCJSC%2CGDKLSF%2CGXK3%2CXYNC%2CKL8%2CXJSSC%2CTJSSC%2CBJPK10BJL%2CGXKLSF%2CGD11X5%2CPCEGG%2CAULUCKY20%2CAULUCKY10%2CAULUCKY5%2CAULUCKY8%2CHK6&begin=" + datetime.datetime.now().strftime('%Y-%m-%d') + "&end=" + datetime.datetime.now().strftime('%Y-%m-%d') + "&settle=false"
                #url = self.target.ser_url.get() + "agent/report/bets?username=zhw999&lottery=BJPK10%2CCQSSC%2CPK10JSC%2CLUCKYSB%2CSSCJSC%2CGDKLSF%2CGXK3%2CXYNC%2CKL8%2CXJSSC%2CTJSSC%2CBJPK10BJL%2CGXKLSF%2CGD11X5%2CPCEGG%2CAULUCKY20%2CAULUCKY10%2CAULUCKY5%2CAULUCKY8%2CHK6&begin=2018-03-25&end=2018-03-25&settle=true"
                logdebug(url)
                html = GetHttp(url = url, headers = headers, method = 'GET')

                if html == None:
                    loginfo("网络异常，需要重新登录")
                    return
                logdebug(html)
                
                if html == "<script type=\"text/javascript\">top.location.href='/'</script>" or html.find("内部错误") > 0:
                    loginfo("服务器内部错误")
                    return
                            
                soup = BeautifulSoup(html, "lxml")
                for tbody in soup.find_all('tbody'):
                    for tr in tbody.find_all('tr'):
                        data = []
                        for td in tr.find_all('td'):
                            data.append(td.get_text())
                        loginfo(data)
                        t_datas.append(data)
                
                

            g_mutex.acquire() 
            global g_datas
            g_datas = t_datas            
            g_mutex.release()
                
            loginfo("注单号    投注时间    投注种类    账号    投注内容    下注金额    退水(%)    下注结果    本级占成    本级结果    占成明细")
            for item in g_datas:
                loginfo(item[0].strip() + " " + item[1].strip() + " " + item[2].strip() + " " + item[3].strip() + " " + item[4].strip() + " " +  item[5].strip() + " " + item[6].strip() + " " + item[7].strip() + " " + item[8].strip() + " " + item[9].strip() + " " + item[10].strip())
            
        logdebug("target_func end")
                
                
       
class ClientThread(threading.Thread):
    def __init__(self, target, thread_num=0, timeout=5.0):
        super(ClientThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout
    def run(self):
        logdebug('Thread start\n')  
        while self.stopped == False:   
            try:        
                self.target_func()
                sleeptime   = 0
                sleepdelay  = 30
                trynum      = 0
                while self.stopped == False: 
                    loginfo('会员尝试登录中(%d/%d)\n'%(sleeptime, sleepdelay))
                    time.sleep(1)
                    sleeptime = sleeptime + 1
                    if sleeptime < sleepdelay:
                        continue;
                    sleepdelay = sleepdelay + 30
                    if sleepdelay > 300:
                        sleepdelay = 300
                    
                    trynum = trynum + 1
                    self.target.cli_interMe()
                    if self.target.cli_loginMe(False) != True:
                        sleeptime = 0
                        #登录失败发送短信通知
                        if trynum % 10 == 0:
                            sendSMS(self.target.conf_phone.get())
                    else:
                        break;
            except:
                logdebug("error lineno:" + str(sys._getframe().f_lineno))
        logdebug('Thread stopped'+ "\n")

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped




    def target_func(self):
        g_order_dict = {}
        sleeptime = 5
        while self.stopped == False:
            sleeptime = sleeptime + 1
            if sleeptime < 5:
                time.sleep(1)
                continue
            sleeptime = 0     

            loginfo("############################查询倍率##############################")
            t = time.time()
            #https://3661032706-xsj.cp168.ws/member/odds?lottery=BJPK10BJL&_=1522070776784
            #{"DX_D":1.5,"DX_X":2.5,"LB_X_4":7,"LB_X_6":31,"LB_X":2,"LB_Z_3":5,"LB_X_3":5,"LB_Z_2":3,"LB_Z_4":7,"LB_Z_5":11,"LB_Z_6":31,"LB_Z_1":2,"LB_X_1":2,"LB_Z":2,"LB_X_5":11,"LB_X_2":3,"T_T":8,"XD_XD":12,"ZD_ZD":12,"ZX_Z":1.95,"ZX_X":2,"ZX1_Z":2,"ZX1_X":2}
           
            url = self.target.cli_url.get() + "member/odds?lottery=BJPK10BJL&_=" + str(int(round(t * 1000)))
            logdebug(url)    
            html = GetHttp(url = url, headers = headers, method = 'GET')
            if html == None:
                loginfo("错误 ==> 网络连接错误！")
                return
            
            logdebug(html)    
            
            try:
                game_lv = json.loads(html)  
                all_the_oc["game_lv"] = game_lv                
            except:
                pass
                
            loginfo("############################查询倍率成功##############################")
            g_mutex.acquire()
                
            global g_datas                 
            t_datas = deepcopy(g_datas)
            t_users = deepcopy(self.target.users)
            g_mutex.release()            
            
            for item in t_datas:
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

                #['4399421039# ', '2018-03-26 21:28:06 星期一', '彩票百家乐673156-1期', 'qqww110A盘', '小 @ 2.5\n', '2200', '0.5%', '-2189.0', '0%', '11.0', '明细']
                loginfo("############################下注订单##############################")
                logdebug(item)
                
                username = item[3]
                username = username.replace("A盘", "")
                username = username.replace("B盘", "")
                username = username.replace("C盘", "")
                username = username.replace("D盘", "")
                username = username.replace("E盘", "")
                username = username.replace("F盘", "")
                username = username.replace("G盘", "")
                
                bUser = False
                for key in t_users:
                    if username == key:
                        bUser = True
                    
                if bUser == False:
                    loginfo("****账号没有找到****" + username)
                    continue
    
                if item[0] in g_order_dict:
                    loginfo("****订单已经处理*****" + item[0])
                    continue
                
                loginfo(item)
    
                amount = round(float(item[5]) * float(t_users[username]))
                #amount =10
                
                drawNumber = item[2]
                if drawNumber.find("彩票百家乐") == -1:
                    loginfo("****不是彩票百家乐订单*****")
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
                logdebug(_split)
                if len(_split) < 2:
                    loginfo("****数据有出错*****", item[4])
                    continue
                _odds           = _split[1]
                _odds           = _odds.replace("\n", "")
                _odds           = _odds.strip()
                _odds            = float(_odds)
                #小
                _type = gettype(_split[0].strip(), _odds)
                logdebug(_type)
                #DX_D
                _split2 = _type.split("_")
                if len(_split2) < 2:
                    loginfo("****数据有出错*****", _type)
                    continue
                
                bet = {}
                bet["game"]     = _split2[0]
                bet["contents"] = _split2[1]
                bet["amount"]   = amount
                #bet["odds"]    = _odds
                bet["odds"]     = all_the_oc["game_lv"][_type]
                order_dict["bets"].append(bet)
                
                
                data = json.dumps(order_dict).encode(encoding='UTF8')  
                url = self.target.cli_url.get() + "member/bet"
                
                headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
                headers["Content-Type"] = "application/json; charset=UTF-8"
                loginfo(url)
                loginfo(data)
                html = GetHttp(url = url, data = data, headers = headers, method = 'POST')
                if html == None:
                    loginfo("错误 ==> 网络连接错误！")
                    return
                loginfo(html)
                #{"account":{"balance":20.706,"betting":10,"maxLimit":80.3,"result":-49.594,"type":0,"userid":"xsj88-cs0990"},"ids":["4401781315"],"odds":["2,2,3,5,7,11,31"],"status":0}
                try:
                    result = json.loads(html)  
                    if result["status"] == 0:
                        loginfo("****跟单成功****")
                    elif result["status"] == 1:
                        loginfo("****跟单失败 赔率变更，重新显示投注确认框****")
                    elif result["status"] == 2:
                        loginfo("****跟单失败 后台未开盘，请等待开盘再试****")                        
                    else:
                        loginfo("****跟单失败****")
                except:
                    logerror("****跟单失败****")
                g_order_dict[item[0]] = 1            
            ###############################

 
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.Close)
        
        #生成config对象
        self.conf = configparser.ConfigParser()
        #用config对象读取配置文件
        self.conf.read("Betting2.txt")    
            
        self.conf_pl = tk.StringVar()    
        if self.conf.has_section("pl") == True:
            self.conf_pl.set(self.conf.get("pl", "value"))
        else:
            self.conf_pl.set("")
            self.conf.add_section("pl")
            self.conf.set("pl", "value", "")
                
        self.conf_phone = tk.StringVar()    
        if self.conf.has_section("phone") == True:
            self.conf_phone.set(self.conf.get("phone", "value"))
        else:
            self.conf_phone.set("")
            self.conf.add_section("phone")
            self.conf.set("phone", "value", "")
            
        # 复选框
        self.conf_ck = tk.IntVar()   # 用来获取复选框是否被勾选，通过chVarDis.get()来获取其的状态,其状态值为int类型 勾选为1  未勾选为0 
        if self.conf.has_section("ck") == True:
            self.conf_ck.set(int(self.conf.get("ck", "value")))
        else:
            self.conf_ck.set(0)
            self.conf.add_section("ck")
            self.conf.set("ck", "value", "")
            
        self.searchText = ""   
        if self.conf.has_section("searchText") == True:
            self.searchText = self.conf.get("searchText", "value")
        else:
            self.searchText = ""
            self.conf.add_section("searchText")
            self.conf.set("searchText", "value", "")
        
        self.ser_initdata()
        self.cli_initdata()
        self.createWidgets()
        self.parseUser()
        self.packUser();
        
    def parseUser(self):
        g_mutex.acquire()
        self.users = {}
        self.searchText = self.searchScrolledText.get(1.0, END)
        searchTexts = self.searchText.split("\n")
        for item in searchTexts:
            if item  == "":
                continue
            item  = item.replace("\n", "")
            user  = item.split("*")
            if len(user) < 2:
                continue                
            self.users[user[0]] = user[1]
        logdebug(self.users)
        g_mutex.release()
        
    def packUser(self):
        searchText = ""
        g_mutex.acquire()
        for user in self.users:
            searchText = searchText + user;
            searchText = searchText + "*";
            searchText = searchText + self.users[user];
            searchText = searchText + "\n";
        g_mutex.release()
        logdebug(searchText)
        self.searchText = searchText
        self.searchScrolledText.delete(1.0, END)
        self.searchScrolledText.insert(tk.INSERT, self.searchText)
        
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
        self.searchScrolledText = scrolledtext.ScrolledText(self.conf_MyFrame, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.searchScrolledText.grid(column=0, row=line, sticky='WE', columnspan=2)    
        
        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.conf_MyFrame, text="默认赔率:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        self.conf_plEntered = ttk.Entry(self.conf_MyFrame, width=60, textvariable=self.conf_pl)  
        self.conf_plEntered.grid(column=1, row=line, sticky='W')   
        
        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.conf_MyFrame, text="通知手机号:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        self.conf_phoneEntered = ttk.Entry(self.conf_MyFrame, width=60, textvariable=self.conf_phone)  
        self.conf_phoneEntered.grid(column=1, row=line, sticky='W')   

    
        line = line + 1
        self.conf_check = tk.Checkbutton(self.conf_MyFrame, text="自动获取账号", variable=self.conf_ck)        # text为该复选框后面显示的名称, variable将该复选框的状态赋值给一个变量，当state='disabled'时，该复选框为灰色，不能点的状态
        #check1.select()                                                                             # 该复选框是否勾选,select为勾选, deselect为不勾选
        self.conf_check.grid(column=0, row=line, sticky=tk.W)                                                   # sticky=tk.W  当该列中其他行或该行中的其他列的某一个功能拉长这列的宽度或高度时，设定该值可以保证本行保持左对齐，N：北/上对齐  S：南/下对齐  W：西/左对齐  E：东/右对齐

        # Adding a Button
        #line = line + 1
        self.conf_sms_btaction = ttk.Button(self.conf_MyFrame,text="短信发送",width=10,command=self.conf_sms)
        self.conf_sms_btaction.grid(column=1,row=line,sticky='E')    

        # Adding a Button
        line = line + 1
        self.conf_save_btaction = ttk.Button(self.conf_MyFrame,text="保存",width=10,command=self.conf_save)
        self.conf_save_btaction.grid(column=0,row=line,sticky='E')
        
        # Adding a Button
        # line = line + 1
        self.conf_account_btaction = ttk.Button(self.conf_MyFrame,text="获取账号数据",width=10,command=self.conf_account)
        self.conf_account_btaction.grid(column=1,row=line,sticky='E')
        ####
        self.searchScrolledText.insert(tk.INSERT, self.searchText)
        
    def conf_sms(self):
        sendSMS(self.conf_phone.get())
        
    def conf_save(self):
        self.searchText = self.searchScrolledText.get(1.0, END)
        #增加新的section
        self.conf.set("searchText", "value", self.searchText) 
        self.conf.set("pl", "value", self.conf_pl.get())   
        self.conf.set("ck", "value", str(self.conf_ck.get()))   
        self.conf.set("phone", "value", self.conf_phone.get())  
        
        #写回配置文件
        self.conf.write(open("Betting2.txt", "w"))
        self.parseUser()
        
    def conf_account(self):
        self.syncUser()
        
    def syncUser(self):
        page_count = 1
        current    = 0
        g_mutex.acquire()
        while current < page_count:
            #https://00271596-xsj.cp168.ws/agent/user/list?parent=cb9999&type=1&lv=&page=2
            url = self.ser_url.get() + "agent/user/list?parent=" + self.ser_nick.get() + "&type=1&lv=&page=" + str(current + 1)
            logdebug(url)
            html = GetHttp(url = url, headers = headers, method = 'GET')
            
            if html == None:
                g_mutex.release()
                loginfo("错误 ==> 网络连接错误！")
                return
            logdebug(html)
            soup = BeautifulSoup(html, "lxml")
            for tbody in soup.find_all('tbody'):
                for tr in tbody.find_all('tr'):
                    username = tr.find_all('td')[3].get_text()
                    #logdebug(username)
                    _split      = username.split(" ")
                    _split[0]   = _split[0].replace("\n", "")
                    _split[0]   = _split[0].strip()
                    if _split[0] == "":
                        continue
                    #logdebug(_split)
                    if _split[0] in self.users:
                        continue
                    self.users[_split[0]] = self.conf_pl.get()
                        
            html_page_count = soup.find_all("span", class_="page_count") #共 2 页
            if len(html_page_count) > 0:
                html_page_count = html_page_count[0].get_text()
                logdebug(html_page_count)
                html_page_count = html_page_count.replace("共 ", "")
                html_page_count = html_page_count.replace(" 页", "")
                page_count = int(html_page_count)
            else:
                break
            
            
            html_current = soup.find_all("span", class_="current") #1
            if len(html_current) > 0:
                html_current = html_current[0].get_text()
                logdebug(html_page_count)
                current = int(html_current)
            else:
                break
        g_mutex.release()        
        self.packUser()
        self.parseUser()
        self.conf_save()
            
    def ser_initdata(self):
        self.ser_thread = None
        self.ser_name = tk.StringVar()    
        if self.conf.has_section("ser_name") == True:
            self.ser_name.set(self.conf.get("ser_name", "value"))
        else:
            self.ser_name.set("")
            self.conf.add_section("ser_name")
            self.conf.set("ser_name", "value", "")

        self.ser_nick = tk.StringVar()    
        if self.conf.has_section("ser_nick") == True:
            self.ser_nick.set(self.conf.get("ser_nick", "value"))
        else:
            self.ser_nick.set("")
            self.conf.add_section("ser_nick")
            self.conf.set("ser_nick", "value", "")
            
        self.ser_pwd = tk.StringVar()    
        if self.conf.has_section("ser_pwd") == True:
            self.ser_pwd.set(self.conf.get("ser_pwd", "value"))
        else:
            self.ser_pwd.set("")
            self.conf.add_section("ser_pwd")
            self.conf.set("ser_pwd", "value", "")
        
        self.ser_url = tk.StringVar()           
        if self.conf.has_section("ser_url") == True:
            self.ser_url.set(self.conf.get("ser_url", "value"))
        else:
            self.ser_url.set("")
            self.conf.add_section("ser_url")
            self.conf.set("ser_url", "value", "")

        self.ser_wd = tk.StringVar()
        if self.conf.has_section("ser_wd") == True:
            self.ser_wd.set(self.conf.get("ser_wd", "value"))
        else:
            self.ser_wd.set("")
            self.conf.add_section("ser_wd")
            self.conf.set("ser_wd", "value", "")  
            
        self.ser_check = tk.StringVar()   
    
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
        self.ser_urlEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable=self.ser_url)  
        self.ser_urlEntered.grid(column=1, row=line, sticky='W')    



         # Adding a Button
        line = line + 1
        self.ser_btaction = ttk.Button(self.ser_MyFrame,text="进入",width=10,command=self.ser_interMe)
        self.ser_btaction.grid(column=1,row=line,sticky='E')   
    
        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.ser_MyFrame, text="账号:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        self.ser_nameEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable=self.ser_name)  
        self.ser_nameEntered.grid(column=1, row=line, sticky='W')
         
        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.ser_MyFrame, text="昵称:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        self.ser_nickEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable=self.ser_nick)  
        self.ser_nickEntered.grid(column=1, row=line, sticky='W')
        
        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.ser_MyFrame, text="密码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        
        self.ser_pwdEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable=self.ser_pwd)  
        self.ser_pwdEntered.grid(column=1, row=line, sticky='W')  

        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.ser_MyFrame, text="验证码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
        
        self.ser_checkEntered = ttk.Entry(self.ser_MyFrame, width=60, textvariable=self.ser_check)  
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
   
    def ser_interMe(self):
        loginfo("################进入代理网站#######################")
        url = self.ser_url.get()
        loginfo("################进入登陆页面#######################")
        #http://54jndgw.ttx158.com/cp5-5-ag/?pagegroup=CP5_5_AG&idcode=64801&rnd=38744&key=E6C257CF128CFFF9ED4A93F61F1312&ts=636574765790000000
        logdebug(url)
        html = GetHttp(url, headers = headers)
        if html == None:
            loginfo("错误 ==> 网络连接错误！")
            return
        logdebug(html)
        loginfo("################进入代理网站成功#######################")

        self.ser_flushMe()
        
    def ser_flushMe(self):
        url = self.ser_url.get() + "code"
        logdebug(url)
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
            
            #验证码识别
            self.ser_pil_image.save("code.jpg") 
            code_image = get_file_content('code.jpg')
            """ 调用通用文字识别, 图片参数为本地图片 """
            #{'log_id': 7581455648920966971, 'words_result_num': 1, 'words_result': [{'words': '5002'}]}
            result = client.basicGeneral(code_image);
            logdebug(result)
            
            if "words_result" in result and len(result["words_result"]):
                logdebug(result["words_result"][0]["words"])
                self.ser_check.set(result["words_result"][0]["words"])            
            
        except urllib.error.HTTPError as e:
            logerror("HTTPError :", e.reason)
        except urllib.error.URLError as e:
            logerror("URLError :", e.reason)
        except Exception as e:
            loginfo("Exception:%s" % (e))
        except:
            loginfo("错误 ==> 网络连接错误！")
            
    def ser_clickMe(self):
        if  self.ser_thread != None:
            if self.ser_thread.is_alive():
                self.ser_thread.stop()
                self.ser_thread.join()
            self.ser_thread = None
            self.ser_btaction.configure(text='开始')
            return
            
        if self.ser_loginMe(True) != True:
            return
            
        self.ser_btaction.configure(text='关闭')
        self.ser_thread = ServerThread(self)
        self.ser_thread.start()
            
    def ser_loginMe(self, tips):    
        self.searchText = self.searchScrolledText.get(1.0, END)
        if self.ser_name.get() == "":
            if tips:
                messagebox.showinfo("提示","账号不能为空！")
            return False
        if self.ser_nick.get() == "":
            if tips:
                messagebox.showinfo("提示","昵称不能为空！")
            return False
        if self.ser_pwd.get() == "":
            if tips:
                messagebox.showinfo("提示","密码不能为空！")
            return False

        if self.ser_check.get() == "":
            if tips:
                messagebox.showinfo("提示","验证码不能为空！")
            return False
            
        if self.searchText == "":
            if tips:
                messagebox.showinfo("提示","账号查询不能为空！")
            return False
            
        self.parseUser()
        self.ser_save()  
        loginfo("############################账号登陆##############################")
        logindict = {}
        logindict["type"]     = 2
        logindict["account"]  = self.ser_name.get()
        logindict["password"] = self.ser_pwd.get() 
        logindict["code"]     = self.ser_check.get()
        
        data = urllib.parse.urlencode(logindict).encode('utf-8')

        url = self.ser_url.get() + "login"
        logdebug(url)       
        html = GetHttp(url = url, data = data, headers = headers, method = 'POST')
        if html == None:
            loginfo("错误 ==> 网络连接错误！")
            return False
        logdebug(html)      
        
        if html.find("新世纪") == -1:
            logdebug(html)
            if tips:
                messagebox.showinfo("提示","登陆失败！")
            return False
               
        #login = False
        #soup = BeautifulSoup(html, "lxml")
        #for row in soup.find_all('title'):
        #    if row.get_text().find("") >= 0:
        #        login = True
        #if login == False:
        #    logerror("错误 ==> 登陆错误！")
        #    return
        if tips:  
            messagebox.showinfo("提示","登陆成功！") 
        return True
                
    def ser_save(self):
        #增加新的section   
        self.conf.set("ser_url", "value", self.ser_url.get())
        self.conf.set("ser_wd", "value", self.ser_wd.get())
        self.conf.set("ser_name", "value", self.ser_name.get())
        self.conf.set("ser_nick", "value", self.ser_nick.get())        
        self.conf.set("ser_pwd", "value", self.ser_pwd.get())
        #写回配置文件
        self.conf.write(open("Betting2.txt", "w"))
    
    ############################
    def cli_initdata(self):   
        self.cli_thread = None
        self.cli_name = tk.StringVar()
        if self.conf.has_section("cli_name") == True:
            self.cli_name.set(self.conf.get("cli_name", "value"))
        else:
            self.cli_name.set("")
            self.conf.add_section("cli_name")
            self.conf.set("cli_name", "value", "")

        self.cli_pwd = tk.StringVar()
        if self.conf.has_section("cli_pwd") == True:
            self.cli_pwd.set(self.conf.get("cli_pwd", "value"))
        else:
            self.cli_pwd.set("")
            self.conf.add_section("cli_pwd")
            self.conf.set("cli_pwd", "value", "")
        
        self.cli_url = tk.StringVar()
        if self.conf.has_section("cli_url") == True:
            self.cli_url.set(self.conf.get("cli_url", "value"))
        else:
            self.cli_url.set("")
            self.conf.add_section("cli_url")
            self.conf.set("cli_url", "value", "")
        
        self.cli_wd = tk.StringVar()
        if self.conf.has_section("cli_wd") == True:
            self.cli_wd.set(self.conf.get("cli_wd", "value"))
        else:
            self.cli_wd.set("")
            self.conf.add_section("cli_wd")
            self.conf.set("cli_wd", "value", "")  
        self.cli_check = tk.StringVar()   
            
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
          
        self.cli_urlEntered = ttk.Entry(self.cli_MyFrame, width=60, textvariable=self.cli_url)  
        self.cli_urlEntered.grid(column=1, row=line, sticky='W')    

        #行
        #line = line + 1
        # Changing our Label  
        #ttk.Label(self.cli_MyFrame, text="登录码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
          
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
          
        self.cli_nameEntered = ttk.Entry(self.cli_MyFrame, width=60, textvariable=self.cli_name)  
        self.cli_nameEntered.grid(column=1, row=line, sticky='W')
        
        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.cli_MyFrame, text="密码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
          
        self.cli_pwdEntered = ttk.Entry(self.cli_MyFrame, width=60, textvariable=self.cli_pwd)  
        self.cli_pwdEntered.grid(column=1, row=line, sticky='W')  

        #行
        line = line + 1
        # Changing our Label  
        ttk.Label(self.cli_MyFrame, text="验证码:").grid(column=0, row=line, sticky='W')  
        # Adding a Textbox Entry widget  
          
        self.cli_checkEntered = ttk.Entry(self.cli_MyFrame, width=60, textvariable=self.cli_check)  
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
            
    def cli_interMe(self):
        loginfo("################进入会员网站#######################")
        url = self.cli_url.get()
        loginfo("################进入会员登陆页面#######################")
        logdebug(url)
        html = GetHttp(url, headers = headers)
        if html == None:
            loginfo("错误 ==> 网络连接错误！")
            return
        logdebug(html)
        
        loginfo("################进入会员网站成功#######################")

        self.cli_flushMe()
        
    def cli_flushMe(self):
        url = self.cli_url.get() + "code"
        logdebug(url)
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

            #验证码识别
            self.cli_pil_image.save("code.jpg") 
            code_image = get_file_content('code.jpg')
            """ 调用通用文字识别, 图片参数为本地图片 """
            #{'log_id': 7581455648920966971, 'words_result_num': 1, 'words_result': [{'words': '5002'}]}
            result = client.basicGeneral(code_image);
            logdebug(result)
            #result = json.loads(byarray.decode('utf-8'))
            if "words_result" in result and len(result["words_result"]):
                logdebug(result["words_result"][0]["words"])
                self.cli_check.set(result["words_result"][0]["words"])                
                
        except urllib.error.HTTPError as e:
            logerror("HTTPError:" , e.reason)
        except urllib.error.URLError as e:
            logerror("URLError:" , e.reason)
        except Exception as e:
            logerror("Exception:%s" % (e))
        except:
            logerror("错误 ==> 网络连接错误！")
   
    def cli_clickMe(self):
        if  self.cli_thread != None:
            if self.cli_thread.is_alive():
                self.cli_thread.stop()
                self.cli_thread.join()
            self.cli_thread = None
            self.cli_btaction.configure(text='开始')
            return
            
        if self.cli_loginMe(True) != True:
            return

        self.cli_btaction.configure(text='关闭')
        self.cli_thread = ClientThread(self)
        self.cli_thread.start()
        
            
    def cli_loginMe(self, tips):    
        if self.cli_name.get() == "":
            if tips:
                messagebox.showinfo("提示","账号不能为空！")
            return

        if self.cli_pwd.get() == "":
            if tips:
                messagebox.showinfo("提示","密码不能为空！")
            return

        if self.cli_check.get() == "":
            if tips:
                messagebox.showinfo("提示","验证码不能为空！")
            return
        self.cli_save()  
        loginfo("############################账号登陆##############################")
        logindict = {}
        logindict["type"]       = 2
        logindict["account"]    = self.cli_name.get()
        logindict["password"]   = self.cli_pwd.get() 
        logindict["code"]       = self.cli_check.get()
        
        data = urllib.parse.urlencode(logindict).encode('utf-8')
        logdebug(data)

        url = self.cli_url.get() + "login"
        logdebug(url)        
        html = GetHttp(url = url, data = data, headers = headers, method = 'POST')
        if html == None:
            loginfo("错误 ==> 网络连接错误！")
            return
        logdebug(html)

        login = False
        soup = BeautifulSoup(html, "lxml")
        for row in soup.find_all('li'):
            if row.get_text().find("用户协议") >= 0:
                login = True
        if login == False:
            logerror("错误 ==> 登陆错误！")
            return
        loginfo("登录 ==> 登陆成功！")
        
        loginfo("############################同意登录##############################")
        #https://3661032706-xsj.cp168.ws/member/index
        url = self.cli_url.get() + "member/index"
        logdebug(url)   
        html = GetHttp(url = url, headers = headers, method = 'GET')
        if html == None:
            loginfo("错误 ==> 网络连接错误！")
            return
        logdebug(html)
        if tips:
            messagebox.showinfo("提示","登陆成功！")
        return True
        
    def cli_save(self):
        #增加新的section
        self.conf.set("cli_url", "value", self.cli_url.get())
        self.conf.set("cli_wd", "value", self.cli_wd.get())
        self.conf.set("cli_name", "value", self.cli_name.get())
        self.conf.set("cli_pwd", "value", self.cli_pwd.get())
        #写回配置文件
        self.conf.write(open("Betting2.txt", "w"))
            
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
    app.title("彩票百家乐 自动跟单系统(开发者QQ：87954657)")
    app.resizable(0,0) #阻止Python GUI的大小调整
    # 主消息循环:
    app.mainloop()

if __name__ == "__main__":
    main()
