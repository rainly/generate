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



class BettingThread(threading.Thread):

    def __init__(self, target, thread_num=0, timeout=1.0):
        super(BettingThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout

    def run(self):
        self.target.textlog.insert(tk.INSERT,'Thread start'+ "\n")
        self.target_func()
        self.target.textlog.insert(tk.INSERT,'Thread stopped'+ "\n")

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped
    
    def target_func():
        self.target.textlog.insert(tk.INSERT,'线程执行目录函数\n')
        conn = sqlite3.connect('cpa700.db')
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

        driver = webdriver.Chrome()
        #driver = webdriver.Firefox()
        while self.stopped != True:
            PostUrl = "http://bw1.htd188.com/"

            driver.get(PostUrl)

            driver.implicitly_wait(5)
            while self.stopped != True:
                time.sleep(1)
                try:
                    driver.find_element_by_id("menu_1")
                    driver.find_element_by_id("menu_1")
                    jump = False
                    handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
                    #print(handles) # 输出句柄集合
                    for handle in handles:# 切换窗口
                        if handle != driver.current_window_handle:
                            #print('switch to ',handle)
                            driver.switch_to_window(handle)
                            #print(driver.current_window_handle)
                            jump = True
                            break
                    if jump:
                        break
                except Exception as msg:
                    #print("Exception:%s" % msg)
                    pass
                except:
                    #print("error lineno:" + str(sys._getframe().f_lineno))
                    pass

            FaildNum = 0 #统计在同一个坑中失败几镒
            while self.stopped != True:
                time.sleep(5)
                try:    
                    driver.switch_to.default_content()
                    #print("default current_url:" + driver.current_url)
                    #print("default title:" + driver.title)


                    frame2 = driver.find_element_by_xpath("//*[@id=\"fset1\"]/frame[2]")
                    driver.switch_to.frame(frame2)
                    #print("//*[@id=\"fset1\"]/frame[2] current_url:" +
                    #driver.current_url)
                    #print("//*[@id=\"fset1\"]/frame[2] title:" +
                    #driver.title)

                    mainFrame = driver.find_element_by_xpath("/html/frameset/frameset/frame[2]")
                    driver.switch_to.frame(mainFrame)
                    #print("/html/frameset/frameset/frame[2] current_url:"
                    #+ driver.current_url)
                    #print("/html/frameset/frameset/frame[2] title:" +
                    #driver.title)

                    #<td id="BaLL_No7" width="26" class="No_3">&nbsp</td>
                    Cur_Award_Issue = driver.find_element_by_xpath("//*[@id=\"Cur_Award_Issue\"]").text
                    BaLL_No1 = driver.find_element_by_xpath("//*[@id=\"BaLL_No1\"]").get_attribute("class").replace("No_", "")
                    BaLL_No2 = driver.find_element_by_xpath("//*[@id=\"BaLL_No2\"]").get_attribute("class").replace("No_", "")
                    BaLL_No3 = driver.find_element_by_xpath("//*[@id=\"BaLL_No3\"]").get_attribute("class").replace("No_", "")
                    BaLL_No4 = driver.find_element_by_xpath("//*[@id=\"BaLL_No4\"]").get_attribute("class").replace("No_", "")
                    BaLL_No5 = driver.find_element_by_xpath("//*[@id=\"BaLL_No5\"]").get_attribute("class").replace("No_", "")
                    BaLL_No6 = driver.find_element_by_xpath("//*[@id=\"BaLL_No6\"]").get_attribute("class").replace("No_", "")
                    BaLL_No7 = driver.find_element_by_xpath("//*[@id=\"BaLL_No7\"]").get_attribute("class").replace("No_", "")
                    BaLL_No8 = driver.find_element_by_xpath("//*[@id=\"BaLL_No8\"]").get_attribute("class").replace("No_", "")
                    BaLL_No9 = driver.find_element_by_xpath("//*[@id=\"BaLL_No9\"]").get_attribute("class").replace("No_", "")
                    BaLL_No10 = driver.find_element_by_xpath("//*[@id=\"BaLL_No10\"]").get_attribute("class").replace("No_", "")
                    Cur_Issue = driver.find_element_by_xpath("//*[@id=\"Cur_Issue\"]").text
                    
                    ##用于保证数据可以下注
                    for BaLL_Idx in range(0, 10):
                        xpath = "//*[@id=\"B-DX-" + str(BaLL_Idx) + "1.money\"]"
                        driver.find_element_by_xpath(xpath)
                        
                    ##指定数据不差1，跳过
                    if int(Cur_Award_Issue) + 1 != int(Cur_Issue):
                        continue

                    
                    sql = "update data set data1 = ? , data2= ?, data3= ?, data4= ?, data5= ?, data6= ? ,data7= ?, data8= ?, data9= ?, data10= ? where issue = ?"
                    cursor.execute(sql, (BaLL_No1, BaLL_No2, BaLL_No3, BaLL_No4, BaLL_No5, BaLL_No6, BaLL_No7, BaLL_No8, BaLL_No9, 10, Cur_Award_Issue))
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
                            ##########################
                            #('大', '小','单','双')
                            if items[1] == "大":
                                if BaLL_No > 5:
                                    Win = 1
                            elif items[1] == "小":
                                if BaLL_No <= 5:
                                    Win = 1
                            elif items[1] == "单":
                                if BaLL_No / 2 == 1:
                                    Win = 1
                            elif items[1] == "双":
                                if BaLL_No / 2 == 0:
                                    Win = 1
                            Monery_Idx = int(items[2])

                            cursor.execute("update data set win = ? where issue = ?", (Win, Cur_Award_Issue))
                            conn.commit()
                    
                            if Win == 1:
                                #检测赢是否回第一位置上
                                #BaLL_Idx = 1
                                #只要有赢，这个坑的失败次数就归0
                                FaildNum = 0;
                                self.target.textlog.insert(tk.INSERT,"开奖期号: " + Cur_Award_Issue+ "中奖\n")
                            else:
                                #累计失败次数
                                FaildNum = FaildNum + 1
                                #失败超过2次，跳转下一个，重置失败次数
                                if FaildNum >= 2:
                                    FaildNum = 0;
                                    BaLL_Idx = BaLL_Idx + 1
                                self.target.textlog.insert(tk.INSERT,"开奖期号: " + Cur_Award_Issue+ "未中奖\n")
                            if BaLL_Idx > 10:
                                BaLL_Idx = 1
                    #处理新订单，如果没有找到的话
                    if Have_Cur_Award_Issue == False or (Have_Cur_Award_Issue == True and Deal_Cur_Award_Issue == True): 
                        if Have_Cur_Award_Issue == False:
                            #print("程序第一次开始执行")
                            pass
                        else:
                            #print("打到旧订单，并已经处理开奖结果")
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
                                 
                            self.target.textlog.insert(tk.INSERT,"处理新订单期号:" + Cur_Issue + " BaLL_Idx:" + str(BaLL_Idx) + " Monery:" + str(Temp_Monery[1]) + "\n")                                     
                            ##################################################
                            #print("deal new BaLL_Idx:" + str(BaLL_Idx))
                            #print("deal new Monery_Idx:" + str(Temp_Monery[0]))
                            BaLL_Idx_Temp = BaLL_Idx
                            if BaLL_Idx_Temp == 10:
                                BaLL_Idx_Temp = 0
                            if self.target.bookChosen.get() == "大":
                                xpath = "//*[@id=\"B-DX-" + str(BaLL_Idx_Temp) + "1.money\"]"
                                driver.find_element_by_xpath(xpath).clear()
                                driver.find_element_by_xpath(xpath).send_keys(str(Temp_Monery[1]))
                            elif self.target.bookChosen.get() == "小":
                                xpath = "//*[@id=\"B-DX-" + str(BaLL_Idx_Temp) + "0.money\"]"
                                driver.find_element_by_xpath(xpath).clear()
                                driver.find_element_by_xpath(xpath).send_keys(str(Temp_Monery[1]))
                            elif self.target.bookChosen.get() == "单":
                                xpath = "//*[@id=\"B-DS-" + str(BaLL_Idx_Temp) + "1.money\"]"
                                driver.find_element_by_xpath(xpath).clear()
                                driver.find_element_by_xpath(xpath).send_keys(str(Temp_Monery[1]))
                            elif self.target.bookChosen.get() == "双":
                                xpath = "//*[@id=\"B-DS-" + str(BaLL_Idx_Temp) + "2.money\"]"
                                driver.find_element_by_xpath(xpath).clear()
                                driver.find_element_by_xpath(xpath).send_keys(str(Temp_Monery[1]))
        
                            time.sleep(1)
                            driver.find_element_by_xpath("//*[@id=\"btn_order_2\"]").click()
                            time.sleep(1)
                            alert = driver.switch_to_alert()
                            time.sleep(1)
                            alert.accept()
                            tt = str(BaLL_Idx) + "=" + self.target.bookChosen.get() + "=" + str(Temp_Monery[0]) 
                            cursor.execute("insert into data(\"issue\", \"order\") VALUES (?, ?)", (Cur_Issue, tt))
                            conn.commit()
                    ############################################################3
                    driver.switch_to.parent_frame()
                    #print("end")
                    #print("**************************************************")
                except Exception as msg:
                    #print("Exception:%s" % msg)
                    pass
                except:
                    #print("error lineno:" + str(sys._getframe().f_lineno))
                    #print("end")
                    #print("**************************************************")
                    pass
        driver.quit()
        cursor.close()
        conn.close()



    
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.thread = None
        try:
            self.conn = sqlite3.connect('cpa700.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute('CREATE TABLE IF NOT EXISTS \"data\" (\"issue\"  varchar(20),\"data1\"  INTEGER,\"data2\"  INTEGER,\"data3\"  INTEGER,\"data4\"  INTEGER,\"data5\"  INTEGER,\"data6\"  INTEGER,\"data7\"  INTEGER,\"data8\"  INTEGER,\"data9\"  INTEGER,\"data10\"  INTEGER,\"order\"  TEXT,\"win\"  INTEGER, PRIMARY KEY (\"issue\" ASC))')
            self.cursor.execute("CREATE TABLE IF NOT EXISTS \"monery\" (\"id\"  INTEGER NOT NULL,\"monery\"  INTEGER,\"win\"  INTEGER,\"loss\"  INTEGER,PRIMARY KEY (\"id\" ASC))")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS \"users\" (\"username\"  TEXT(56)) ")
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
        self.monty = ttk.LabelFrame(self.tab1, text='操作区')
        self.monty.grid(column=0, row=0, padx=8, pady=4)
        #第一行
        # Changing our Label  
        ttk.Label(self.monty, text="账号:").grid(column=0, row=0, sticky='W')  
  
        # Adding a Textbox Entry widget  
        self.name = tk.StringVar()  
        self.nameEntered = ttk.Entry(self.monty, width=60, textvariable=self.name)  
        self.nameEntered.grid(column=1, row=0, sticky='W')  

        #第二行
        ttk.Label(self.monty, text="请选择:").grid(column=0, row=1,sticky='W')
        # Adding a Combobox
        self.book = tk.StringVar()
        self.bookChosen = ttk.Combobox(self.monty, width=60, textvariable=self.book)
        self.bookChosen['values'] = ('大', '小','单','双')
        self.bookChosen.grid(column=1, row=1, sticky='W')
        self.bookChosen.current(0)  #设置初始显示值，值为元组['values']的下标
        self.bookChosen.config(state='readonly')  #设为只读模式
        self.bookChosen.bind("<<ComboboxSelected>>", self.Chosen)  

        # Using a scrolled Text control
        self.scrolW = 80
        self.scrolH = 10
        #第三行
        ttk.Label(self.monty, text="策略配置(序号=金额=赢跳转序号=输跳转序号)").grid(column=0, row=2,sticky='W')
        #第四行
        self.text = scrolledtext.ScrolledText(self.monty, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.text.grid(column=0, row=3, sticky='WE', columnspan=3)
        #第五行
        # Adding a Button
        self.btaction = ttk.Button(self.monty,text="保存",width=10,command=self.save).grid(column=1,row=4,sticky='E')   

        #第六行
        ttk.Label(self.monty, text="日志信息:").grid(column=0, row=5,sticky='W')
        #第七行
        self.textlog = scrolledtext.ScrolledText(self.monty, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.textlog.grid(column=0, row=6, sticky='WE', columnspan=3)
        #第八行
        # Adding a Button
        self.btaction = ttk.Button(self.monty,text="开始",width=10,command=self.clickMe)
        self.btaction.grid(column=1,row=7,sticky='E')   
        # 一次性控制各控件之间的距离
        for child in self.monty.winfo_children(): 
            child.grid_configure(padx=3,pady=1)
        # 单独控制个别控件之间的距离
        #self.btaction.grid(column=2,row=1,rowspan=2,padx=6)
        #---------------Tab1控件介绍------------------#
        self.FlushData()
        
        self.cursor.execute('select * from users')
        datas = self.cursor.fetchall()
        for data in datas:# 切换窗口
            self.nameEntered.insert(END, str(data[0]))
            
    def clickMe(self):
        if  self.thread != None:
            self.btaction.configure(text='开始')
            if self.thread.is_alive():
                self.thread.stop()
                self.thread.join()
            self.thread = None
            return
        self.cursor.execute('delete from users')
        self.cursor.execute("replace into \"users\" (username) values  ( ? )", (self.nameEntered.get(), ))
        self.conn.commit()

        self.cursor.execute("select * from monery")
        monerys = self.cursor.fetchall()
        if len(monerys) == 0:
            messagebox.showerror("错误","策略未配置")
            return        
            
        self.btaction.configure(text='关闭')
        self.thread = BettingThread(self)
        self.thread.start()

    def save(self):
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
    app.title("cpa700 自动打码神器(开发者QQ：87954657)")
    app.resizable(0,0) #阻止Python GUI的大小调整
    # 主消息循环:
    app.mainloop()

if __name__ == "__main__":
    main()
    
    
