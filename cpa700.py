﻿## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
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
from selenium.common.exceptions import NoSuchElementException
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
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'  
headers = { 'User-Agent' : user_agent }  



class TestThread(threading.Thread):

    def __init__(self, target, thread_num=0, timeout=1.0):
        super(TestThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout

    def run(self):
        def target_func():
            #inp = raw_input("Thread %d: " % self.thread_num)
            #print('Thread %s input %s' % (self.thread_num, inp))
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute("select * from monery")
            monerys = cursor.fetchall()
            if len(monerys) == 0:
                return
            driver = webdriver.Chrome()
            while self.stopped != True:
                PostUrl = "http://bw1.cpa700.com/"

                #driver=webdriver.Firefox()
                driver.get(PostUrl)
                self.target.log.insert(tk.INSERT,'开始执行\n')


                driver.implicitly_wait(5)
                while self.stopped != True:
                    time.sleep(1)
                    try:
                        driver.find_element_by_id("menu_1")
                        driver.find_element_by_id("menu_1")
                        jump = False
                        handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
                        print(handles) # 输出句柄集合
                        for handle in handles:# 切换窗口
                            if handle != driver.current_window_handle:
                                print('switch to ',handle)
                                driver.switch_to_window(handle)
                                print(driver.current_window_handle)
                                jump = True
                                break
                        if jump:
                            break
                    except:
                        print("error lineno:" + str(sys._getframe().f_lineno))

                while self.stopped != True:
                    try:
                        time.sleep(5)
                        print("begin")
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

                        #<td id="BaLL_No7" width="26" class="No_3">&nbsp;</td>
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

                        ##指定数据不差1，跳过
                        if int(Cur_Award_Issue) + 1 != int(Cur_Issue):
                            continue
                        sql = "update data set data1 = ? , data2= ?, data3= ?, data4= ?, data5= ?, data6= ? ,data7= ?, data8= ?, data9= ?, data10= ? where issue = ?"
                        cursor.execute(sql, (BaLL_No1, BaLL_No2, BaLL_No3, BaLL_No4, BaLL_No5, BaLL_No6, BaLL_No7, BaLL_No8, BaLL_No9, 10, Cur_Award_Issue))
                        conn.commit()                                                                                        
                        print("update data Cur_Award_Issue:" + Cur_Award_Issue)
                        

                        BaLL_Idx = 1
                        Win = 0
                        Monery_Idx = monerys[0][0]
                        Have_Cur_Award_Issue = False
                        Deal_Cur_Award_Issue = False
                        cursor.execute("select * from data where issue = ?", (Cur_Award_Issue,))
                        datas = cursor.fetchall()
                        for data in datas:# 切换窗口
                            print("deal with Cur_Award_Issue: " + Cur_Award_Issue)
                            #处理未开奖数据
                            Have_Cur_Award_Issue = True
                            if data[11] != None and data[12] == None:
                                Deal_Cur_Award_Issue = True
                                print("deal win Cur_Award_Issue:" + Cur_Award_Issue)
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
                                ##########################
                                #('大', '小','单','双')
                                if items[1] == "大":
                                    if BaLL_No >= 5:
                                        Win = 1
                                elif items[1] == "小":
                                    if BaLL_No < 5:
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
                                    BaLL_Idx = 1
                                else:
                                    BaLL_Idx = BaLL_Idx + 1
                                if BaLL_Idx > 5:
                                    BaLL_Idx = 1
                            elif data[11] != None and data[12] != None:
                                Deal_Cur_Award_Issue = True
                                print("deal win Cur_Award_Issue:" + Cur_Award_Issue)
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
                                ##########################
                                #('大', '小','单','双')
                                if items[1] == "大":
                                    if BaLL_No >= 5:
                                        Win = 1
                                elif items[1] == "小":
                                    if BaLL_No < 5:
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
                                    BaLL_Idx = 1
                                else:
                                    BaLL_Idx = BaLL_Idx + 1
                                if BaLL_Idx > 5:
                                    BaLL_Idx = 1
                        #处理新订单，如果没有找到的话
                        if Have_Cur_Award_Issue == False or (Have_Cur_Award_Issue == True and Deal_Cur_Award_Issue == True): 
                            if Have_Cur_Award_Issue == False:
                                print("程序第一次开始执行")
                            else:
                                print("打到旧订单，并已经处理开奖结果")
                            cursor.execute("select * from data where issue = ?", (Cur_Issue,))
                            datas = cursor.fetchall()
                            if len(datas) == 0:
                                print("处理新订单 Cur_Issue:" + Cur_Issue)
                                ##################################################
                                Sel_Monery = None
                                if Have_Cur_Award_Issue:
                                    for monery in monerys:
                                        if  monery[0] == Monery_Idx:
                                            Sel_Monery = monery
                                            break
                                    for monery in monerys:
                                        if  Win == 1 and monery[0] == Sel_Monery[2]:
                                            Sel_Monery = monery
                                            break
                                        if  Win == 0 and monery[0] == Sel_Monery[3]:
                                            Sel_Monery = monery
                                            break
                                else:
                                     Sel_Monery = monerys[0]                                       
                                ##################################################
                                print("deal new BaLL_Idx:" + str(BaLL_Idx))
                                print("deal new Monery_Idx:" + str(Sel_Monery[0]))
                                if self.target.bookChosen.get() == "大":
                                    xpath = "//*[@id=\"B-DX-" + str(BaLL_Idx) + "1.money\"]"
                                    driver.find_element_by_xpath(xpath).clear()
                                    driver.find_element_by_xpath(xpath).send_keys(str(Sel_Monery[1]))
                                elif self.target.bookChosen.get() == "小":
                                    xpath = "//*[@id=\"B-DX-" + str(BaLL_Idx) + "0.money\"]"
                                    driver.find_element_by_xpath(xpath).clear()
                                    driver.find_element_by_xpath(xpath).send_keys(str(Sel_Monery[1]))
                                elif self.target.bookChosen.get() == "单":
                                    xpath = "//*[@id=\"B-DS-" + str(BaLL_Idx) + "1.money\"]"
                                    driver.find_element_by_xpath(xpath).clear()
                                    driver.find_element_by_xpath(xpath).send_keys(str(Sel_Monery[1]))
                                elif self.target.bookChosen.get() == "双":
                                    xpath = "//*[@id=\"B-DS-" + str(BaLL_Idx) + "2.money\"]"
                                    driver.find_element_by_xpath(xpath).clear()
                                    driver.find_element_by_xpath(xpath).send_keys(str(Sel_Monery[1]))

                                time.sleep(2)
                                driver.find_element_by_xpath("//*[@id=\"btn_order_2\"]").click()
                                time.sleep(2)
                                alert = driver.switch_to_alert()
                                time.sleep(2)
                                alert.accept()
                                tt = str(BaLL_Idx) + "=" + self.target.bookChosen.get() + "=" + str(Sel_Monery[0]) 
                                cursor.execute("insert into data(\"issue\", \"order\") VALUES (?, ?)", (Cur_Issue, tt))
                                conn.commit()
                            else:
                                print("新订单已经处理 Cur_Issue:" + Cur_Issue)
                        ############################################################3
                        driver.switch_to.parent_frame()
                        print("end")
                        print("**************************************************")
                    except:
                        print("error lineno:" + str(sys._getframe().f_lineno))
                        print("end")
                        print("**************************************************")
            driver.quit()
            cursor.close()
            conn.close()
                    
        subthread = threading.Thread(target=target_func, args=())
        subthread.setDaemon(True)
        subthread.start()

        while not self.stopped:
            subthread.join(self.timeout)

        self.target.log.insert(tk.INSERT,'Thread stopped')

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.thread = None
        try:
            self.conn = sqlite3.connect('test.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute('CREATE TABLE IF NOT EXISTS \"data\" (\"issue\"  varchar(20),\"data1\"  INTEGER,\"data2\"  INTEGER,\"data3\"  INTEGER,\"data4\"  INTEGER,\"data5\"  INTEGER,\"data6\"  INTEGER,\"data7\"  INTEGER,\"data8\"  INTEGER,\"data9\"  INTEGER,\"data10\"  INTEGER,\"order\"  TEXT,\"win\"  INTEGER, PRIMARY KEY (\"issue\" ASC));')
            self.cursor.execute("CREATE TABLE IF NOT EXISTS \"monery\" (\"id\"  INTEGER NOT NULL,\"monery\"  INTEGER,\"win\"  INTEGER,\"loss\"  INTEGER,PRIMARY KEY (\"id\" ASC));")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS \"users\" (\"username\"  TEXT(56)); ")
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
        def clickMe():
            self.cursor.execute("replace into \"users\" (username) values  ( ? )", (self.nameEntered.get(), ))
            self.conn.commit()

            url = "http://121.40.206.168/soft_net/SBDL_NSkt.php?NS=" + self.nameEntered.get()
            print('正在抓取首页 <---  ' + url)
            request = urllib.request.Request(url, headers = headers)
            try:
                #response = urllib.request.urlopen(request)
                response = opener.open(request, timeout = 5)
                html = response.read().decode()
            except urllib.error.HTTPError as e:
                print('The server couldn\'t fulfill the request.')
                print('Error code: ' + str(e.code))
                print('Error reason: ' + e.reason)
                messagebox.showerror("错误","网络连接错误！")
                return
            except urllib.error.URLError as e:
                print('We failed to reach a server.')
                print('Reason: ' + e.reason)
                messagebox.showerror("错误","网络连接错误！")
                return
            except:
                print("error lineno:" + str(sys._getframe().f_lineno))
                messagebox.showerror("错误","网络连接错误！")
                return
            if html != "1":
                messagebox.showerror("错误","账号未注册！")
                return

            text = self.btaction.config('text')
            if  text[4] == '关闭':
                self.btaction.configure(text='开始')
                self.thread.stop()
                #self.thread.join()
            else:
                self.btaction.configure(text='关闭')
                #btaction.configure(state='disabled') # Disable the Button
                #Widget
                self.thread = TestThread(self)
                self.thread.start()
        def save():#self.text.get(1.0, END)
            print(self.text.get(1.0, END))
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

            self.text.delete(0.0,len(self.text.get(0.0,END)) - 1.0)
            self.cursor.execute('select * from monery')
            datas = self.cursor.fetchall()
            for data in datas:# 切换窗口
                 self.text.insert(tk.INSERT, str(data[0]) + "=" + str(data[1]) + "=" + str(data[2]) + "=" + str(data[3]) + "\n")
            messagebox.showinfo("提示","配置成功！")
            
            
        def Chosen(*args):  
            print(self.bookChosen.get())  


        # We are creating a container tab3 to hold all other widgets
        self.monty = ttk.LabelFrame(self.tab1, text='操作区')
        self.monty.grid(column=0, row=0, padx=8, pady=4)

        # Changing our Label  
        ttk.Label(self.monty, text="账号:").grid(column=0, row=0, sticky='W')  
  
        # Adding a Textbox Entry widget  
        self.name = tk.StringVar()  
        self.nameEntered = ttk.Entry(self.monty, width=50, textvariable=self.name)  
        self.nameEntered.grid(column=1, row=0, sticky='W')  


        ttk.Label(self.monty, text="请选择:").grid(column=0, row=1,sticky='W')
        # Adding a Combobox
        self.book = tk.StringVar()
        self.bookChosen = ttk.Combobox(self.monty, width=50, textvariable=self.book)
        self.bookChosen['values'] = ('大', '小','单','双')
        self.bookChosen.grid(column=1, row=1, sticky='W')
        self.bookChosen.current(0)  #设置初始显示值，值为元组['values']的下标
        self.bookChosen.config(state='readonly')  #设为只读模式
        self.bookChosen.bind("<<ComboboxSelected>>", Chosen)  

        # Using a scrolled Text control
        self.scrolW = 80
        self.scrolH = 10
        ttk.Label(self.monty, text="策略配置:").grid(column=0, row=2,sticky='W')
        self.text = scrolledtext.ScrolledText(self.monty, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.text.grid(column=0, row=3, sticky='WE', columnspan=3)

        # Adding a Button
        self.btaction = ttk.Button(self.monty,text="保存",width=10,command=save)   
        self.btaction.grid(column=2,row=4)

        ttk.Label(self.monty, text="日志信息:").grid(column=0, row=5,sticky='W')
        self.log = scrolledtext.ScrolledText(self.monty, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.log.grid(column=0, row=6, sticky='WE', columnspan=3)

        # Adding a Button
        self.btaction = ttk.Button(self.monty,text="开始",width=10,command=clickMe)   
        self.btaction.grid(column=2,row=7)

        # 一次性控制各控件之间的距离
        for child in self.monty.winfo_children(): 
            child.grid_configure(padx=3,pady=1)
        # 单独控制个别控件之间的距离
        #self.btaction.grid(column=2,row=1,rowspan=2,padx=6)
        #---------------Tab1控件介绍------------------#

        self.cursor.execute('select * from monery')
        datas = self.cursor.fetchall()
        for data in datas:# 切换窗口
             self.text.insert(tk.INSERT, str(data[0]) + "=" + str(data[1]) + "=" + str(data[2]) + "=" + str(data[3]) + "\n")
        
        self.cursor.execute('select * from users')
        datas = self.cursor.fetchall()
        for data in datas:# 切换窗口
            self.nameEntered.insert(END, str(data[0]))

        
def main():
    app = Application()
    app.title("cpa700 自动打码神器")
    # 主消息循环:
    app.mainloop()

if __name__ == "__main__":
    main()

