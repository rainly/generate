﻿## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
#北京赛车 自动打码神器
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
import sqlite3
import threading  
import time

import urllib
import urllib.request
import urllib.response
import urllib.error
import http.cookiejar

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

driver = webdriver.Chrome()
PostUrl = "http://a3688.net"
driver.get(PostUrl)
driver.implicitly_wait(5)    


class BettingThread(threading.Thread):

    def __init__(self, target, thread_num=0, timeout=1.0):
        super(BettingThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout

    def run(self):
        self.target.textlog.insert(tk.INSERT,'线程开始执行\n')
        conn = sqlite3.connect('a3688.db')
        cursor = conn.cursor()
        cursor.execute("delete from data")
        conn.commit() 
        cursor.execute("select * from monery")
        monerys = cursor.fetchall()
        if len(monerys) == 0:
            cursor.close()
            conn.close()
            self.target.textlog.insert(tk.INSERT,'策略未配置\n')
            return
       
        while self.stopped == False:
            print("**********find title***********")
            isJump = False
            try:
                handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
                #print(handles) # 输出句柄集合
                for handle in handles:# 切换窗口
                    print(driver.title)
                    print(driver.current_url)
                    #http://pxiagme1.lot5562.net/member/m5ngj8qrmj99ji203gpbraupnp/Home/Index.action
                    if handle != driver.current_window_handle:
                        driver.switch_to_window(handle)
                        print(driver.title)
                        if driver.title == "688":
                            isJump = True
                            break
                if isJump:
                    break
                time.sleep(5)
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

        
        FaildNum = 0 #统计在同一个坑中失败几镒
        while self.stopped != True:
                time.sleep(5)
                try:    
                    driver.switch_to.default_content()
                    #print("default current_url:" + driver.current_url)
                    #print("default title:" + driver.title)

                    #/html/frameset
                    #    //*[@id="topFrame"]
                    #    //*[@id="frameset1"]
                    #        //*[@id="leftFrame"]
                    #        //*[@id="mainFrame"]
                    mainFrame = driver.find_element_by_xpath("//*[@id=\"mainFrame\"]")
                    driver.switch_to.frame(mainFrame)
                    #print("//*[@id=\"mainFrame\"] current_url:" +driver.current_url)
                    #print("//*[@id=\"mainFrame\"] title:" +driver.title)

                    Cur_Award_Issue = driver.find_element_by_xpath("//*[@id=\"memberMainContent\"]/div[1]/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td[1]").text
                    #674039期结果
                    Cur_Award_Issue = Cur_Award_Issue.replace("期结果", "");
                    Cur_Award_Issue = Cur_Award_Issue.strip()
                    print(Cur_Award_Issue)
                    
                    #<div class="bjpks no_04"></div>
                    BaLL_No1  = driver.find_element_by_xpath("//*[@id=\"memberMainContent\"]/div[1]/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td[2]/div").get_attribute("class").replace("bjpks no_", "")
                    BaLL_No2  = driver.find_element_by_xpath("//*[@id=\"memberMainContent\"]/div[1]/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td[3]/div").get_attribute("class").replace("bjpks no_", "")
                    BaLL_No3  = driver.find_element_by_xpath("//*[@id=\"memberMainContent\"]/div[1]/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td[4]/div").get_attribute("class").replace("bjpks no_", "")
                    BaLL_No4  = driver.find_element_by_xpath("//*[@id=\"memberMainContent\"]/div[1]/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td[5]/div").get_attribute("class").replace("bjpks no_", "")
                    BaLL_No5  = driver.find_element_by_xpath("//*[@id=\"memberMainContent\"]/div[1]/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td[6]/div").get_attribute("class").replace("bjpks no_", "")
                    BaLL_No6  = driver.find_element_by_xpath("//*[@id=\"memberMainContent\"]/div[1]/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td[7]/div").get_attribute("class").replace("bjpks no_", "")
                    BaLL_No7  = driver.find_element_by_xpath("//*[@id=\"memberMainContent\"]/div[1]/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td[8]/div").get_attribute("class").replace("bjpks no_", "")
                    BaLL_No8  = driver.find_element_by_xpath("//*[@id=\"memberMainContent\"]/div[1]/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td[9]/div").get_attribute("class").replace("bjpks no_", "")
                    BaLL_No9  = driver.find_element_by_xpath("//*[@id=\"memberMainContent\"]/div[1]/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td[10]/div").get_attribute("class").replace("bjpks no_", "")
                    BaLL_No10 = driver.find_element_by_xpath("//*[@id=\"memberMainContent\"]/div[1]/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td[11]/div").get_attribute("class").replace("bjpks no_", "")
                        
                    print(BaLL_No1)
                    print(BaLL_No2)
                    print(BaLL_No3)
                    print(BaLL_No4)
                    print(BaLL_No5)
                    print(BaLL_No6)
                    print(BaLL_No7)
                    print(BaLL_No8)
                    print(BaLL_No9)
                    print(BaLL_No10)
                    #<span class="eventInfoDiv">674031</span>
                    Cur_Issue = driver.find_element_by_xpath("//*[@id=\"memberMainContent\"]/div[1]/table/tbody/tr[2]/td[1]/span").text
                    #674040
                    Cur_Issue = Cur_Issue.strip()

                    
                    print(Cur_Issue)

                    if Cur_Award_Issue == "" or Cur_Issue == "":
                        driver.switch_to.parent_frame()
                        continue;

                    
                    def GetXpath(BaLL_No, BallType):
                    
                        BaLL_No = str(BaLL_No)
                        BaLL_No = BaLL_No.zfill(2)
                        if BallType == "大":
                            return "//*[@id=\"2" + BaLL_No + "201\"]/div[2]"
                        elif BallType == "小":
                            return "//*[@id=\"2" + BaLL_No + "202\"]/div[2]"
                        elif BallType == "单":
                            return "//*[@id=\"2" + BaLL_No + "301\"]/div[2]"
                        elif BallType == "双":
                            return "//*[@id=\"2" + BaLL_No + "302\"]/div[2]"
                            
                    #//*[@id="201201"]/div[2]
                    #//*[@id="201202"]/div[2]
                    #//*[@id="201301"]/div[2]
                    #//*[@id="201302"]/div[2]

                    #//*[@id="201301"]/div[2]
                    
                    ##指定数据不差1，跳过
                    if int(Cur_Award_Issue) + 1 != int(Cur_Issue):
                        driver.switch_to.parent_frame()
                        continue
    
                    
                    sql = "update data set data1 = ? , data2= ?, data3= ?, data4= ?, data5= ?, data6= ? ,data7= ?, data8= ?, data9= ?, data10= ? where issue = ?"
                    cursor.execute(sql, (BaLL_No1, BaLL_No2, BaLL_No3, BaLL_No4, BaLL_No5, BaLL_No6, BaLL_No7, BaLL_No8, BaLL_No9, BaLL_No10, Cur_Award_Issue))
                    conn.commit()                                                                                        
                    #self.target.textlog.insert(tk.INSERT,"获取期号:" + Cur_Award_Issue + "数据\n")
                    

                    BaLL_Idx = 1
                    Win = 0
                    Monery_Idx = monerys[0][0]
                    Have_Cur_Award_Issue = False
                    Deal_Cur_Award_Issue = False
                    cursor.execute("select * from data where issue = ? and win is NULL", (Cur_Award_Issue,))
                    datas = cursor.fetchall()
                    for data in datas:# 切换窗口
                        self.target.textlog.insert(tk.INSERT,"处理期号: " + Cur_Award_Issue+ "开奖数据\n")
                        #处理未开奖数据
                        Have_Cur_Award_Issue = True
                        if data[11] != None:
                            Deal_Cur_Award_Issue = True
                            items = data[11].split("=")
                            if len(items) != 3:
                                break
                            BaLL_No = 1
                            BaLL_Idx = int(items[0])
                            if BaLL_Idx == 1:
                                BaLL_No = int(BaLL_No1)
                            elif BaLL_Idx == 2:
                                BaLL_No = int(BaLL_No2)
                            elif BaLL_Idx == 3:
                                BaLL_No = int(BaLL_No3)
                            elif BaLL_Idx == 4:
                                BaLL_No = int(BaLL_No4)
                            elif BaLL_Idx == 5:
                                BaLL_No = int(BaLL_No5)
                            elif BaLL_Idx == 6:
                                BaLL_No = int(BaLL_No6)
                            elif BaLL_Idx == 7:
                                BaLL_No = int(BaLL_No7)
                            elif BaLL_Idx == 8:
                                BaLL_No = int(BaLL_No8)
                            elif BaLL_Idx == 9:
                                BaLL_No = int(BaLL_No9)
                            elif BaLL_Idx == 10:
                                BaLL_No = int(BaLL_No10)     
    
                            print("##############" + str(BaLL_No))
                            ##########################
                            #('大', '小','单','双')
                            if items[1] == "大":
                                if BaLL_No > 5:
                                    Win = 1
                            elif items[1] == "小":
                                if BaLL_No <= 5:
                                    Win = 1
                            elif items[1] == "单":
                                if BaLL_No % 2 == 1:
                                    Win = 1
                            elif items[1] == "双":
                                if BaLL_No % 2 == 0:
                                    Win = 1
                                    
                            print("##############" + str(Win))
                            
                            Monery_Idx = int(items[2])

                            cursor.execute("update data set win = ? where issue = ?", (Win, Cur_Award_Issue))
                            conn.commit()
                        
                            if Win == 1:
                                #检测赢是否回第一位置上
                                BaLL_Idx = 1
                                #只要有赢，这个坑的失败次数就归0
                                FaildNum = 0;
                                self.target.textlog.insert(tk.INSERT,"开奖期号: " + Cur_Award_Issue+ "中奖 返回第一球开始\n")
                            else:
                                #累计失败次数
                                FaildNum = FaildNum + 1
                                self.target.textlog.insert(tk.INSERT,"开奖期号: " + Cur_Award_Issue+ "未中奖 当前未中奖次数：" + str(FaildNum) + "\n")
                                #失败超过2次，跳转下一个，重置失败次数
                                if FaildNum >= self.target.faildnum.get():
                                    FaildNum = 0;
                                    BaLL_Idx = BaLL_Idx + 1
                                    self.target.textlog.insert(tk.INSERT,"未中奖次数超出设置的值，递增一个球：" + str(BaLL_Idx) + "\n")
                            if BaLL_Idx > 10:
                                BaLL_Idx = 1
                                self.target.textlog.insert(tk.INSERT,"所有球全部打完，回归到第一球" + "\n")
                    #处理新订单，如果没有找到的话
                    if Have_Cur_Award_Issue == False or (Have_Cur_Award_Issue == True and Deal_Cur_Award_Issue == True): 
                        if Have_Cur_Award_Issue == False:
                            #print("程序第一次开始执行")
                            pass
                        else:
                            print("打到旧订单，并已经处理开奖结果")
                            pass
                        cursor.execute("select * from data where issue = ?", (Cur_Issue,))
                        datas = cursor.fetchall()
                        if len(datas) == 0:
                            ##################################################
                            Temp_Monery = None
                            if Have_Cur_Award_Issue:
                                for monery in monerys:
                                    if  monery[0] == Monery_Idx:
                                        Temp_Monery = monery
                                        break
                                for monery in monerys:
                                    if  Win == 1 and monery[0] == Temp_Monery[2]:
                                        Temp_Monery = monery
                                        break
                                    if  Win == 0 and monery[0] == Temp_Monery[3]:
                                        Temp_Monery = monery
                                        break
                            else:
                                 Temp_Monery = monerys[0] 
                                 
                            self.target.textlog.insert(tk.INSERT,"处理新订单期号:" + Cur_Issue + " 位置:" + str(BaLL_Idx) + " 金额:" + str(Temp_Monery[1]) + "\n")                                     
                            ##################################################
                            print("deal new BaLL_Idx:" + str(BaLL_Idx))
                            print("deal new Monery_Idx:" + str(Temp_Monery[0]))
                            BaLL_Idx_Temp = BaLL_Idx
                            #if BaLL_Idx_Temp == 10:
                            #    BaLL_Idx_Temp = 0
                            if self.target.bookChosen.get() == "大":
                                xpath = GetXpath(BaLL_Idx_Temp, "大")
                                driver.find_element_by_xpath(xpath).click()
                            elif self.target.bookChosen.get() == "小":
                                xpath = GetXpath(BaLL_Idx_Temp, "小")
                                driver.find_element_by_xpath(xpath).click()
                            elif self.target.bookChosen.get() == "单":
                                xpath = GetXpath(BaLL_Idx_Temp, "单")
                                driver.find_element_by_xpath(xpath).click()
                            elif self.target.bookChosen.get() == "双":
                                xpath = GetXpath(BaLL_Idx_Temp, "双")
                                driver.find_element_by_xpath(xpath).click()
                                
                            time.sleep(1)
                            driver.find_element_by_xpath("//*[@id=\"itmStakeInputBulk\"]").clear()
                            driver.find_element_by_xpath("//*[@id=\"itmStakeInputBulk\"]").send_keys(str(Temp_Monery[1]))
                            time.sleep(1)
                            driver.find_element_by_xpath("//*[@id=\"confirmStakeBtn\"]").click()
                            time.sleep(1)
                            driver.find_element_by_xpath("//*[@id=\"betSlipDivContent\"]/table/tbody/tr[2]/td/a[1]").click()
                            
                            tt = str(BaLL_Idx) + "=" + self.target.bookChosen.get() + "=" + str(Temp_Monery[0]) 
                            cursor.execute("insert into data(\"issue\", \"order\") VALUES (?, ?)", (Cur_Issue, tt))
                            conn.commit()
                    ############################################################3
                    driver.switch_to.parent_frame()
                    print("end")
                    print("**************************************************")
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
                
        cursor.close()
        conn.close()
        self.target.textlog.insert(tk.INSERT,'线程结束执行'+ "\n")

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped

    
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.thread = None
        try:
            self.conn = sqlite3.connect('a3688.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute('CREATE TABLE IF NOT EXISTS \"data\" (\"issue\"  varchar(20),\"data1\"  INTEGER,\"data2\"  INTEGER,\"data3\"  INTEGER,\"data4\"  INTEGER,\"data5\"  INTEGER,\"data6\"  INTEGER,\"data7\"  INTEGER,\"data8\"  INTEGER,\"data9\"  INTEGER,\"data10\"  INTEGER,\"order\"  TEXT,\"win\"  INTEGER, PRIMARY KEY (\"issue\" ASC))')
            self.cursor.execute("CREATE TABLE IF NOT EXISTS \"monery\" (\"id\"  INTEGER NOT NULL,\"monery\"  INTEGER,\"win\"  INTEGER,\"loss\"  INTEGER,PRIMARY KEY (\"id\" ASC))")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS \"global\" (\"faildnum\"  TEXT(56)) ")
        except Exception as msg:
            print("Exception:%s" % msg)
            pass
        except:
            pass
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
        ttk.Label(self.MyFrame, text="失败次数跳转:").grid(column=0, row=0, sticky='W')  
  
        # Adding a Textbox Entry widget  
        self.faildnum = tk.IntVar()  
        self.faildnumEntered = ttk.Entry(self.MyFrame, width=60, textvariable=self.faildnum)  
        self.faildnumEntered.grid(column=1, row=0, sticky='W')  

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
        ttk.Label(self.MyFrame, text="策略配置(序号=金额=赢跳转序号=输跳转序号)").grid(column=0, row=2,sticky='W')
        #第四行
        self.text = scrolledtext.ScrolledText(self.MyFrame, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.text.grid(column=0, row=3, sticky='WE', columnspan=3)
        #第五行
        # Adding a Button
        self.btaction = ttk.Button(self.MyFrame,text="保存",width=10,command=self.save).grid(column=1,row=4,sticky='E')   

        #第六行
        ttk.Label(self.MyFrame, text="日志信息:").grid(column=0, row=5,sticky='W')
        #第七行
        self.textlog = scrolledtext.ScrolledText(self.MyFrame, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.textlog.grid(column=0, row=6, sticky='WE', columnspan=3)
        #第八行
        # Adding a Button
        self.btaction = ttk.Button(self.MyFrame,text="开始",width=10,command=self.clickMe)
        self.btaction.grid(column=1,row=7,sticky='E')   
        # 一次性控制各控件之间的距离
        for child in self.MyFrame.winfo_children(): 
            child.grid_configure(padx=3,pady=1)
        # 单独控制个别控件之间的距离
        #self.btaction.grid(column=2,row=1,rowspan=2,padx=6)
        #---------------Tab1控件介绍------------------#
        self.FlushData()
        
        self.cursor.execute('select * from global')
        datas = self.cursor.fetchall()
        for data in datas:# 切换窗口
            print(str(data[0]))
            #self.faildnumEntered.insert(END, str(data[0]))
            self.faildnum.set(data[0])
            
    def clickMe(self):
        self.cursor.execute('delete from global')
        self.cursor.execute("replace into \"global\" (faildnum) values  ( ? )", (self.faildnumEntered.get(), ))
        self.conn.commit()

        self.cursor.execute("select * from monery")
        monerys = self.cursor.fetchall()
        if len(monerys) == 0:
            messagebox.showerror("错误","策略未配置")
            return
        
        text = self.btaction.config('text')
        if  text[4] == '关闭':
            self.btaction.configure(text='开始')
            self.thread.stop()
            #self.thread.join()
        else:
            self.btaction.configure(text='关闭')
            #btaction.configure(state='disabled') # Disable the Button
            self.thread = BettingThread(self)
            self.thread.start()

    def save(self):
        self.cursor.execute('delete from global')
        self.cursor.execute("replace into \"global\" (faildnum) values  ( ? )", (self.faildnumEntered.get(), ))
        self.conn.commit()
        
        text = self.text.get(1.0, END)
        lines = text.split("\n") 
        for line1 in lines:
            if line1 == "":
                continue
            item1s = line1.split("=") 
            if len(item1s) != 4:
                messagebox.showerror("错误","配置出错，请重新配置！")
                return
            win = False
            lose = False
            for line2 in lines:
                if line2 == "":
                    continue
                item2s = line2.split("=")
                if len(item2s) != 4:
                    messagebox.showerror("错误","配置出错，请重新配置！")
                    return
                #成功
                if item1s[2] == item2s[0]:
                    win = True
                #失败
                if item1s[3] == item2s[0]:
                    lose = True

            if win == False or lose == False:
                messagebox.showerror("错误","配置出错，请重新配置！")
                return
            
        self.cursor.execute('delete from monery') 
        for line in lines:
            items = line.split("=") 
            if len(items) != 4:
                continue
            sql = "insert into monery values(" + str(items[0]) + "," + str(items[1]) + "," + str(items[2]) + "," + str(items[3]) + ")"
            self.cursor.execute(sql)
        self.conn.commit()
        self.FlushData()
        messagebox.showinfo("提示","配置成功！")
        
        
    def Chosen(self, *args):  
        print(self.bookChosen.get())  
    
    def FlushData(self):
        self.text.delete(0.0,len(self.text.get(0.0,END)) - 1.0)
        self.cursor.execute('select * from monery')
        datas = self.cursor.fetchall()
        for data in datas:# 切换窗口
            self.text.insert(tk.INSERT, str(data[0]) + "=" + str(data[1]) + "=" + str(data[2]) + "=" + str(data[3]) + "\n")
            

            
def main():
    app = Application()
    app.title("a3688 自动打码神器(开发者QQ：87954657)")
    app.resizable(0,0) #阻止Python GUI的大小调整
    # 主消息循环:
    app.mainloop()
    driver.quit()

if __name__ == "__main__":
    main()
    
    
