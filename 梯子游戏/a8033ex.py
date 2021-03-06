## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
#梯子游戏

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
#driver.get("http://a8033.com/")
driver.get("http://baidu.com")



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


class BettingThread(threading.Thread):
    def __init__(self, target, thread_num=0, timeout=5.0):
        super(BettingThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout
    def run(self):
        self.target.textlog.insert(tk.INSERT,'Thread start\n')                   
        self.target_func()
        self.target.textlog.insert(tk.INSERT,'Thread stopped'+ "\n")

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped

    def logprint(self, log):
        print(log)
        self.target.textlog.insert(tk.INSERT, log + "\n")
    
    def target_func(self):

        #url = self.target.url
        #self.logprint("地址:" + url)

        #jump = self.target.jump
        #self.logprint("输停:" + jump)

        monery = self.target.monery
        self.logprint("下注金额:" + monery)
        
        agent = self.target.agent
        self.logprint("代理:" + agent)    
       
       
        monerys = monery.split("+")
        if len(monerys) == 0:
            self.logprint("错误 ==> 金额配置出错")
            return
            

        jumps = []
        line = self.target.jump.split("\r\n")
        for item in line:
            jump = re.split('[+=]',item)
            jumps.append(jump)            
            
        
        #driver.get(url)
        driver.implicitly_wait(5)
        
        try:
            while self.stopped == False:
                self.logprint("***检测是否打开梯子游戏***")  
                isJump = False
                handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
                for handle in handles:# 切换窗口
                    if handle != driver.current_window_handle:
                        driver.switch_to_window(handle)
                        #self.logprint(driver.title)
                        if driver.title == "梯子游戏":
                            isJump = True
                            break
                if isJump:
                    break
                time.sleep(self.timeout)
                
            self.logprint("***打开梯子游戏正常***")   
            Last_Award_Issue = ""
            Last_Award_Issue_Buy = ""
            Jump_Idx   = 0
            
            #<span class="LD-resultItem LD--s LD--l4o">4单</span>
            #<span class="LD-resultItem LD--s LD--r4e">4双</span>
            #<span class="LD-resultItem LD--s LD--r3o">3单</span>
            #<span class="LD-resultItem LD--s LD--l3e">3双</span>            
            
            MyKey={}
            MyKey["LD-resultItem LD--s LD--r3o"] = "3单"
            MyKey["LD-resultItem LD--s LD--l3e"] = "3双"
            MyKey["LD-resultItem LD--s LD--l4o"] = "4单"
            MyKey["LD-resultItem LD--s LD--r4e"] = "4双"

            while self.stopped == False:
                try:
                    time.sleep(self.timeout)
                    
                    Cur_Award_Issue1_1 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[1]/td[1]").text
                    Cur_Award_Issue1_2 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[2]/td[1]").text
                    Cur_Award_Issue1_3 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[3]/td[1]").text
                    
                    if int(Cur_Award_Issue1_1) != (int(Cur_Award_Issue1_2) + 1):
                        self.logprint("***期号不相差1*** " + Cur_Award_Issue1_1 + "~=" + Cur_Award_Issue1_2)
                        continue                    
    
                    if int(Cur_Award_Issue1_1) != (int(Cur_Award_Issue1_3) + 2):
                        self.logprint("***期号不相差2*** " + Cur_Award_Issue1_1 + "~=" + Cur_Award_Issue1_3)
                        continue    
                    
                    if Cur_Award_Issue1_1 == Last_Award_Issue:
                        self.logprint("***等待开奖*** ==>" + Cur_Award_Issue1_1)
                        continue
                    
                    self.logprint("********************************************************")
                    Last_Award_Issue = Cur_Award_Issue1_1
                    self.logprint("***处理中奖结果*** ==>" + Cur_Award_Issue1_1)
                    #tclass1 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[1]/td[2]/span").get_attribute("class")
                    tclass2 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[2]/td[2]/span").get_attribute("class")
                    tclass3 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[3]/td[2]/span").get_attribute("class")
                    tclass4 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[4]/td[2]/span").get_attribute("class")
                    tclass5 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[5]/td[2]/span").get_attribute("class")
                    tclass6 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[6]/td[2]/span").get_attribute("class")
                    tclass7 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[7]/td[2]/span").get_attribute("class")
                    tclass8 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[8]/td[2]/span").get_attribute("class")
                    tclass9 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[9]/td[2]/span").get_attribute("class")
                    
                    self.logprint("***开奖***" + MyKey[tclass2])                      
                    
                    roal = [MyKey[tclass9], MyKey[tclass8], MyKey[tclass7], MyKey[tclass6], MyKey[tclass5], MyKey[tclass4], MyKey[tclass3], MyKey[tclass2]]
                    print(roal)                    

                    #处理中奖结果
                    Last_Award_Issue_Win = False
                    if Last_Award_Issue_Buy != "":                       
                        Last_Award_Issue_Win = False
                        if MyKey[tclass2] == Last_Award_Issue_Buy:
                            Last_Award_Issue_Win = True
                        else:
                            Last_Award_Issue_Win = False
                        #######################################
                        if Last_Award_Issue_Win == True:
                            #中奖，金额回归
                            Jump_Idx    = 0
                            self.logprint("***中奖*** 金额回归***" + monerys[Jump_Idx])
                        else:
                            Jump_Idx    = Jump_Idx + 1
                            #######################################
                            if Jump_Idx >= len(monerys):
                                #Jump_Idx = 0;
                                self.logprint("***未中奖*** 金额达到最大,停止")
                                return
                            else:
                                self.logprint("***未中奖*** 金额下移一个：" + monerys[Jump_Idx])
                                
                    else:
                        self.logprint("***未下注***")
                                                 
                    self.logprint("********************************************************") 
                    
                    self.logprint("***检测规则是否下注***")
                    for jump in jumps:
                        tmp1 = jump[0:len(jump) - 1]
                        tmp2 = roal[len(roal) - len(jump) + 1:len(roal)]
                        if tmp1==tmp2:
                            Last_Award_Issue_Buy = jump[len(jump) - 1]
                            self.logprint("***规则符合条件***" + str(jump))
                            break
                        else:
                            self.logprint("***规则不符合条件***" + str(jump))
                            
                    #if MyKey[tclass2] == "4单": #4单
                    #    self.logprint("***检测是否下注***4单 ==>不购买")
                    #    Last_Award_Issue_Buy = ""
                    #ielif  MyKey[tclass2] == "4双":#4双
                    #i    ##############################################
                    #i    if MyKey[tclass3] == "3单":
                    #i        self.logprint("***检测是否下注*** 上轮：3单 ==> 本轮：4双 ==>不购买")
                    #i        Last_Award_Issue_Buy = ""                        
                    #i    elif MyKey[tclass3] == "4双":
                    #i        self.logprint("***检测是否下注*** 上轮：4双 ==> 本轮：4双 ==>不购买")
                    #i        Last_Award_Issue_Buy = ""                        
                    #i    else:
                    #i        self.logprint("***检测是否下注*** 4双 ==>购买3单")
                    #i        Last_Award_Issue_Buy = "3单"    
                    #i    ##############################################    
                    #ielif  MyKey[tclass2] == "3双":#3双
                    #i    self.logprint("***检测是否下注***3双 ==>不购买") 
                    #i    Last_Award_Issue_Buy = ""
                    #ielif  MyKey[tclass2] == "3单":#3单
                    #i    ##############################################
                    #i    if MyKey[tclass3] == "3单":
                    #i        self.logprint("***检测是否下注*** 上轮：3单 ==> 本轮：3单 ==>不购买")
                    #i        Last_Award_Issue_Buy = ""                        
                    #i   elif MyKey[tclass3] == "4双":
                    #i        self.logprint("***检测是否下注*** 上轮：4双 ==> 本轮：3单 ==>不购买")
                    #i        Last_Award_Issue_Buy = ""                        
                    #i    else:
                    #i        self.logprint("***检测是否下注*** 4双 ==>购买4双")
                    #i        Last_Award_Issue_Buy = "4双"    
                    #i    ##############################################
                    #ielse:
                    #i    self.logprint("***检测是否下注***未知类型")
                    #i    Last_Award_Issue_Buy = ""
                    #i    
                    #i
                    ##############################################
                    if Last_Award_Issue_Buy == "" or Last_Award_Issue_Buy == "停":
                        self.logprint("***本轮不下注:***" + Cur_Award_Issue1_1)
                        continue
                    else:
                        self.logprint("***开始下注:***" + Cur_Award_Issue1_1 + " 金额：" + monerys[Jump_Idx])

                    input1 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/table/tbody/tr[2]/td[4]/div[1]/input")
                    input2 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/table/tbody/tr[2]/td[4]/div[2]/input")
                    input3 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/table/tbody/tr[2]/td[4]/div[3]/input")
                    input4 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/table/tbody/tr[2]/td[4]/div[4]/input")
                    
                    if Last_Award_Issue_Buy == "3单":#3单
                        input1.clear()
                        input1.send_keys(monerys[Jump_Idx])
                    elif Last_Award_Issue_Buy == "3双":#3双
                        input2.clear()
                        input2.send_keys(monerys[Jump_Idx])                           
                    elif Last_Award_Issue_Buy == "4单":#4单
                        input2.clear()
                        input2.send_keys(monerys[Jump_Idx])                          
                    elif Last_Award_Issue_Buy == "4双":#4双
                        input4.clear()
                        input4.send_keys(monerys[Jump_Idx])
                    else:
                        Last_Award_Issue_Buy = "";
                        continue;
                        
                        
                    time.sleep(1)          
                    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/div[2]/button[2]").click()  
                    time.sleep(1)
                    driver.find_element_by_xpath("//*[@id=\"alertify\"]/div/div/div[2]/div[2]/button[2]").click()
                    
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
                    self.logprint("Exception:%s" % msg)
                    pass
                except:
                    #self.logprint("error lineno:" + str(sys._getframe().f_lineno))
                    #self.target.textlog.insert(tk.INSERT,"error lineno:" +
                    #str(sys._getframe().f_lineno))
                    pass
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
            self.logprint("Exception:%s" % msg)
            pass
        except:
            #self.logprint("error lineno:" + str(sys._getframe().f_lineno))
            #self.target.textlog.insert(tk.INSERT,"error lineno:" +
            #str(sys._getframe().f_lineno))
            pass    
        
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.Close)
        self.thread = None
        #生成config对象
        self.conf = configparser.ConfigParser()
        #用config对象读取配置文件
        self.conf.read("a8033ex.txt")

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
        
        self.jump = "3单+3单=停\r\n3单+4双=停\r\n4双+3单=停\r\n4双+4双=停\r\n3单=4双\r\n4双=3单\r\n"
        
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
        self.scrolW = 80
        self.scrolH = 10
        
    
        #行
        line = 0
        #行
        ttk.Label(self.MyFrame, text="金额配置(10+20+40+80+...)").grid(column=0, row=line,sticky='W')
        #行
        line = line + 1
        self.textMonery = scrolledtext.ScrolledText(self.MyFrame, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.textMonery.grid(column=0, row=line, sticky='WE', columnspan=3)        
        #行
        # Adding a Button
        line = line + 1
        self.btaction = ttk.Button(self.MyFrame,text="保存",width=10,command=self.save).grid(column=1,row=line,sticky='E')   
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
        self.btaction.grid(column=1,row=line,sticky='E')  
        
        # 一次性控制各控件之间的距离
        for child in self.MyFrame.winfo_children(): 
            child.grid_configure(padx=3,pady=1)
        # 单独控制个别控件之间的距离
        #self.btaction.grid(column=2,row=1,rowspan=2,padx=6)
        #---------------Tab1控件介绍------------------#
        #self.textJump.insert(tk.INSERT, self.jump)
        self.textMonery.insert(tk.INSERT, self.monery)
            
    def clickMe(self):
        if  self.thread != None:
            self.btaction.configure(text='开始')
            if self.thread.is_alive():
                self.thread.stop()
                self.thread.join()
            self.thread = None
            return
    
        #self.jump  = self.textJump.get(1.0, END)
        self.monery = self.textMonery.get(1.0, END)

        if self.monery == "":
            messagebox.showinfo("提示","金额不能为空！")
            return
            
        self.btaction.configure(text='关闭')
        self.thread = BettingThread(self)
        self.thread.start()
            
    def save(self):
        #增加新的section
        #
        #self.jump  = self.textJump.get(1.0, END)
        self.monery = self.textMonery.get(1.0, END)
        self.conf.set("jump", "value", self.jump)
        self.conf.set("monery", "value", self.monery)
        #写回配置文件
        self.conf.write(open("a8033ex.txt", "w"))
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
    app.title("梯子游戏 自动打码神器(开发者QQ：87954657)")
    app.resizable(0,0) #阻止Python GUI的大小调整
    # 主消息循环:
    app.mainloop()
    driver.close()
    driver.quit()

if __name__ == "__main__":
    main()
