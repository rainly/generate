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

ssl._create_default_https_context = ssl._create_unverified_context


driver = webdriver.Chrome()
driver.get("http://0190022.com")
#driver.get("http://baidu.com")



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
    
    def target_func(self):
    
        '''
        =================================

        庄庄=闲庄
        闲闲=庄闲

        1=10=1=1

        本方案累计赢[1000]元跳转到方案[1]
        本方案累计输[1000]元跳转到方案[1]

        ==============================
        '''
        
        print("**********target_func begin***********")
        
        buyno = int(self.target.buyno)
        self.logprint("位置:" + self.target.buyno)
        if buyno < 1 or buyno > 10:
            self.logprint("错误 ==> 购买位置配置出错")
            return            
        
        monery = self.target.monery
        self.logprint("金额:" + monery)
            
        monerys = []
        line = self.target.monery.split("\r\n")
        for item in line:
            monery = re.split('=',item)
            monerys.append(monery)  
            
        Jumps = []
        line = self.target.Jump.split("\r\n")
        for item in line:
            Jump = re.split('=',item)
            Jumps.append(Jump)  
        
        
        
        driver.implicitly_wait(5)           
        while self.stopped == False:
            print("**********find title***********")
            isJump = False
            try:
                handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
                #print(handles) # 输出句柄集合
                for handle in handles:# 切换窗口
                    if handle != driver.current_window_handle:
                        driver.switch_to_window(handle)
                        print(driver.title)
                        if driver.title == "彩票游戏官方版":
                            isJump = True
                            break
                if isJump:
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
        
        Last_Award_Issue = ""
        Last_Award_Issue_Have   = False

        roads       = {}
        SleepTime   = 10
        Temp_Monery = monerys[0]     
        Temp_Jump   = None
        Temp_Jump_Idx = 0
        while self.stopped == False:
            try:
                SleepTime = SleepTime + 1
                if SleepTime < 10:
                    time.sleep(1)
                    continue
                
                SleepTime = 0  
                self.logprint("***新的轮开始***")   
                Cur_Award_Issue1 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[2]/div[2]").text
                Cur_Award_Issue2 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[1]").text
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
                
                if Ball01 == "" or Ball02 == "" or Ball03 == "" or Ball04 == "" or Ball05 == "" or Ball06 == "" or Ball07 == "" or Ball08 == "" or Ball09 == "" or Ball10 == "":
                    self.logprint("***数据还在加载中***")   
                    continue
                    
                def GetType(BallNo):
                    if int(BallNo) > 5:
                        return '大'
                    else:
                        return '小'     
                road     = [GetType(Ball01), GetType(Ball02), GetType(Ball03), GetType(Ball04), GetType(Ball05), GetType(Ball06), GetType(Ball07), GetType(Ball08), GetType(Ball09), GetType(Ball10)]
                roads[Cur_Award_Issue2]     = road

                Last_Award_Issue = Cur_Award_Issue1

                #处理中奖结果
                Win = 0
                if Temp_Jump != None:
                    if road[buyno - 1] == Temp_Jump[1][Temp_Jump_Idx]:
                        Win = 1
                        print("***中奖***")
                    else:
                        Win = 0
                        print("***未中奖***")
                        
                    for monery in monerys:
                        if  Win == 1 and monery[0] == Temp_Monery[2]:
                            Temp_Monery = monery
                            break
                        if  Win == 0 and monery[0] == Temp_Monery[3]:
                            Temp_Monery = monery
                            break
                else:
                    print("***未下注***")

                for idx  in range(1,5):
                    Award_Issue = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) +"]/div[1]").text
                    Ball01 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) +"]/div[2]/span[1]").text
                    Ball02 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) +"]/div[2]/span[2]").text
                    Ball03 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) +"]/div[2]/span[3]").text
                    Ball04 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) +"]/div[2]/span[4]").text
                    Ball05 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) +"]/div[2]/span[5]").text
                    Ball06 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) +"]/div[2]/span[6]").text
                    Ball07 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) +"]/div[2]/span[7]").text
                    Ball08 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) +"]/div[2]/span[8]").text
                    Ball09 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) +"]/div[2]/span[9]").text
                    Ball10 = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[1]/div[4]/div[" + str(idx) +"]/div[2]/span[10]").text
                    road   = [GetType(Ball01), GetType(Ball02), GetType(Ball03), GetType(Ball04), GetType(Ball05), GetType(Ball06), GetType(Ball07), GetType(Ball08), GetType(Ball09), GetType(Ball10)]
                    roads[Award_Issue]     = road   
                        
                print(roads)
                    

                self.logprint("***检测规则是否下注***")
                if Temp_Jump != None and len(Temp_Jump[Temp_Jump_Idx]) >= Temp_Jump_Idx:
                    Temp_Jump = None
                    Temp_Jump_Idx = 0
                
                if Temp_Jump == None:
                    for Jump in Jumps:
                        tmp1 = Jump[0]
                        tmp2 = ""
                        keys = roads.keys() 
                        keys = keys.sort()
                        for key in keys:
                            tmp2 = tmp2 + roads[key][0]
                        if tmp1==tmp2[:-len(tmp1)]:
                            Temp_Jump = Jump
                            self.logprint("***规则符合条件***" + str(Jump[0]) + "= " + str(Jump[1]))
                            break
                        else:
                            self.logprint("***规则不符合条件***" + str(Jump[0]) + "= " + str(Jump[1]))    
                            
                    
                #双面玩法
                if Temp_Jump != None:
                    if Temp_Jump[1][Temp_Jump_Idx] == "大":
                        driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div[1]/div[2]/button[1]")
                    if Temp_Jump[1][Temp_Jump_Idx] == "小":
                        driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div[1]/div[2]/button[2]")
                    if Temp_Jump[1][Temp_Jump_Idx] == "单":
                        driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div[1]/div[2]/button[3]")
                    if Temp_Jump[1][Temp_Jump_Idx] == "双":
                        driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[3]/div[" + str(buyno) + "]/div[1]/div[2]/button[3]")
                    Temp_Jump_Idx = Temp_Jump_Idx + 1
                    time.sleep(1)
                    driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[4]/div[1]/div[1]/input").clear()
                    driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[4]/div[1]/div[1]/input").send_keys(Temp_Monery[1])
                    time.sleep(1)
                    driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[4]/div[1]/div[1]/button").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[2]/div[2]/div[4]/div[2]/button[3]").click()

                
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
            

        if self.conf.has_section("Jump") == True:
            self.Jump = self.conf.get("Jump", "value")
        else:
            self.Jump = ""
            self.conf.add_section("Jump")
            self.conf.set("Jump", "value", "")
        
        if self.conf.has_section("monery") == True:
            self.monery = self.conf.get("monery", "value")
        else:
            self.monery = ""
            self.conf.add_section("monery")
            self.conf.set("monery", "value", "")
            
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
        self.scrolH = 5
        
    
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
        
        #行
        line = line + 1
        ttk.Label(self.MyFrame, text="大大=小小##小小=大大").grid(column=0, row=line,sticky='W',columnspan=3)
        #行
        line = line + 1
        self.textJump = scrolledtext.ScrolledText(self.MyFrame, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.textJump.grid(column=0, row=line, sticky='WE', columnspan=3)
        #行
        line = line + 1
        ttk.Label(self.MyFrame, text="序号=金额=赢跳转=输跳转").grid(column=0, row=line,sticky='W', columnspan=3)
        #行
        line = line + 1
        self.textMonery = scrolledtext.ScrolledText(self.MyFrame, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.textMonery.grid(column=0, row=line, sticky='WE', columnspan=3)        
        #行
        # Adding a Button
        line = line + 1
        self.btaction = ttk.Button(self.MyFrame,text="保存",width=10,command=self.save).grid(column=2,row=line,sticky='E')   
        #行
        line = line + 1
        ttk.Label(self.MyFrame, text="日志信息:").grid(column=0, row=line,sticky='W')
        #行
        line = line + 1
        self.textlog = scrolledtext.ScrolledText(self.MyFrame, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.textlog.grid(column=0, row=line, sticky='WE', columnspan=3)
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
        
        self.urlEntered.insert(END, self.url)
        self.buynoEntered.insert(END, self.buyno)
        self.textJump.insert(tk.INSERT, self.Jump)
        self.textMonery.insert(tk.INSERT, self.monery)

    def enterMe(self):
        self.url  = self.urlEntered.get()
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
        self.buyno  = self.buynoEntered.get()
        self.Jump   = self.textJump.get(1.0, END)
        self.monery = self.textMonery.get(1.0, END)
        if self.url == "":
            messagebox.showinfo("提示","地址不能为空")
            return
            
        if self.buyno == "":
            messagebox.showinfo("提示","地址不能为空")
            return
            
        if self.monery == "":
            messagebox.showinfo("提示","金额不能为空！")
            return
            
        if self.Jump == "":
            messagebox.showinfo("提示","停次数不能为空！")
            return
            
        self.btaction.configure(text='关闭')
        self.thread = BettingThread(self)
        self.thread.start()
            
    def save(self):
        #增加新的section
        #
        self.url  = self.urlEntered.get()
        self.buyno  = self.buynoEntered.get()
        self.Jump  = self.textJump.get(1.0, END)
        self.monery = self.textMonery.get(1.0, END)
        
        self.conf.set("url", "value", self.url)
        self.conf.set("buyno", "value", self.buyno)
        self.conf.set("Jump", "value", self.Jump)
        self.conf.set("monery", "value", self.monery)
        #写回配置文件
        self.conf.write(open("bjpk.txt", "w"))
        messagebox.showinfo("提示","配置成功！")
        
    def Chosen(self, *args):
        messagebox.showinfo("提示", self.bookChosen.get())
        
    def Close(self):
        if self.thread != None:
            messagebox.showinfo("提示","请先关闭自动打码！")
            return
        self.destroy()    
    
    
def main():
    app = Application()
    app.title("北京赛车 自动打码神器(开发者QQ：87954657)")
    app.resizable(0,0) #阻止Python GUI的大小调整
    # 主消息循环:
    app.mainloop()
    driver.close()
    driver.quit()

if __name__ == "__main__":
    main()
