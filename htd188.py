## -*- coding: utf-8 -*-
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
from selenium.common.exceptions import *
import sqlite3
import threading  
import time

import urllib
import urllib.request
import urllib.response
import urllib.error
import http.cookiejar
import re
import random

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



class TestThread(threading.Thread):

    def __init__(self, target, thread_num=0, timeout=1.0):
        super(TestThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout
        


    def run(self):
        def toStr(BaLL_No):
            if BaLL_No > 5:
                return '大'
            else:
                return '小'

        def foundload(BaLL_Idx, loads, datas):
            load_found = None
            for load in loads:
                #路单要减一
                if len(load) - 1 > len(datas):
                    continue
                isFound = True
                for idx in  range(1, len(load)):
                    if toStr(datas[idx - 1][BaLL_Idx]) != load[idx]:
                        isFound = False
                        break
                if isFound:
                    load_found = load
                    break

            strLog = ""
            for idx in  range(0, len(datas)):
                strLog += toStr(datas[idx][BaLL_Idx])
            #print("BaLL_Idx:" + str(BaLL_Idx) + " data:" + strLog + "\n")
            if load_found != None:
                #print(load_found)
                pass
            else:
                #print("Not Found Loads\n")
                pass
            return load_found
            
            
        def delorder(driver, conn, cursor, Cur_Issue, BaLL_Idx, order, BaLL_No, monerys, loads, datas):
            Win = 0
            BaLL_No = int(BaLL_No)
            Sel_Monery = monerys[0]
            if order != None:
                Monery_Idx = monerys[0][0]
                items = order.split("=")
                if len(items) != 2:
                    return False
                #('大', '小','单','双')
                if toStr(BaLL_No) == items[0]:
                    Win = 1
                else:
                    Win = 0
                #########################
                Monery_Idx = int(items[1])
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

            load_found = foundload(BaLL_Idx, loads, datas)
            if load_found == None:
                return False

            _BaLL_Idx = BaLL_Idx
            if BaLL_Idx == 10:
                _BaLL_Idx = 0

            try:            
                if load_found[0] == "大":
                    xpath = "//*[@id=\"B-DX-" + str(_BaLL_Idx) + "1.money\"]"
                    driver.find_element_by_xpath(xpath).clear()
                    driver.find_element_by_xpath(xpath).send_keys(str(Sel_Monery[1]))
                elif load_found[0] == "小":
                    xpath = "//*[@id=\"B-DX-" + str(_BaLL_Idx) + "0.money\"]"
                    driver.find_element_by_xpath(xpath).clear()
                    driver.find_element_by_xpath(xpath).send_keys(str(Sel_Monery[1]))
                elif load_found[0] == "单":
                    xpath = "//*[@id=\"B-DS-" + str(_BaLL_Idx) + "1.money\"]"
                    driver.find_element_by_xpath(xpath).clear()
                    driver.find_element_by_xpath(xpath).send_keys(str(Sel_Monery[1]))
                elif load_found[0] == "双":
                    xpath = "//*[@id=\"B-DS-" + str(_BaLL_Idx) + "2.money\"]"
                    driver.find_element_by_xpath(xpath).clear()
                    driver.find_element_by_xpath(xpath).send_keys(str(Sel_Monery[1]))
            
                tt = load_found[0] + "=" + str(Sel_Monery[0])
                sql = "update data set order" + str(BaLL_Idx) + " = ? where issue = ?"
                cursor.execute(sql, (tt, Cur_Issue))
                conn.commit()
            except Exception as msg:
                print("Exception:%s" % msg)
                pass
            except:
                #print("error lineno:" + str(sys._getframe().f_lineno))
                #self.target.textlog.insert(tk.INSERT,"error lineno:" +
                #str(sys._getframe().f_lineno))
                pass
            return True            
            
        def target_func():
            if self.target.urlEntered.get() == "":
                self.target.textlog.insert(tk.INSERT,'网址出错\n')
                return
                
            conn = sqlite3.connect('htd188.db')
            cursor = conn.cursor()
            cursor.execute("delete from data")
            conn.commit() 
            ########################################
            cursor.execute("select * from monery")
            monerys = cursor.fetchall()
            if len(monerys) == 0:
                cursor.close()
                conn.close()
                self.target.textlog.insert(tk.INSERT,'金额策略未配置\n')
                return

            ########################################
            cursor.execute("select * from load")
            loads = []
            dbloads = cursor.fetchall()
            if len(dbloads) == 0:
                cursor.close()
                conn.close()
                self.target.textlog.insert(tk.INSERT,'路单策略未配置\n')
                return
            
            lines = dbloads[0][0].split("\n") 
            for line in lines:
                if line == "":
                    continue
                line = line.strip()
                items = re.split('[+＝=]',line)
                loads.append(items)

            #对路单反序
            loads.reverse()
            for load in loads:
                load = load.reverse()
                
            driver = webdriver.Chrome()
            #driver = webdriver.Firefox()
            while self.stopped != True:
                PostUrl = self.target.urlEntered.get()
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
                    except NoSuchElementException as msg:
                        #print("NoSuchElementException:%s" % msg)
                        pass
                    except WebDriverException as msg:
                        #print("WebDriverException:%s" % msg)
                        pass
                    except NoSuchWindowException as msg:
                        #print("NoSuchWindowException:%s" % msg)
                        pass
                    except NoSuchAttributeException as msg:
                        #print("NoSuchAttributeException:%s" % msg)
                        pass
                    except NoAlertPresentException as msg:
                        #print("NoAlertPresentException:%s" % msg)
                        pass
                    except ElementNotVisibleException as msg:
                        #print("ElementNotVisibleException:%s" % msg)
                        pass
                    except ElementNotSelectableException as msg:
                        #print("ElementNotSelectableException:%s" % msg)
                        pass
                    except TimeoutException as msg:
                        #print("TimeoutException:%s" % msg)
                        pass
                    except Exception as msg:
                        print("Exception:%s" % msg)
                        pass
                    except:
                        #print("error lineno:" + str(sys._getframe().f_lineno))
                        #self.target.textlog.insert(tk.INSERT,"error lineno:" +
                        #str(sys._getframe().f_lineno))
                        pass

                run_idx = 0
                while self.stopped != True:
                    time.sleep(1)
                    try:
                        driver.switch_to.default_content()
                        
                        frame2 = driver.find_element_by_xpath("//*[@id=\"fset1\"]/frame[2]")
                        driver.switch_to.frame(frame2)
                        
                        mainFrame = driver.find_element_by_xpath("/html/frameset/frameset/frame[2]")
                        driver.switch_to.frame(mainFrame)

                        Cur_Award_Issue = driver.find_element_by_xpath("//*[@id=\"Cur_Award_Issue\"]")
                        Cur_Award_Issue = Cur_Award_Issue.text
                        Cur_Issue = driver.find_element_by_xpath("//*[@id=\"Cur_Issue\"]")
                        Cur_Issue = Cur_Issue.text
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


                        ##用于保证数据可以下注
                        for BaLL_Idx in range(0, 10):
                            xpath = "//*[@id=\"B-DX-" + str(BaLL_Idx) + "1.money\"]"
                            driver.find_element_by_xpath(xpath)
                      
                        ##指定数据不差1，跳过
                        if int(Cur_Award_Issue) + 1 != int(Cur_Issue):
                            continue

                        #print("插入路单数据" + Cur_Award_Issue + "\n")
                        cursor.execute("select * from data where issue = ? ", (Cur_Award_Issue,))
                        Cur_Award_Issue_datas = cursor.fetchall()
                        if len(Cur_Award_Issue_datas) > 0:
                            sql = "update data set data1 = ?  , data2= ?, data3=?, data4= ?, data5= ?, data6= ?  ,data7= ?, data8= ?,data9= ?, data10= ?  where issue = ?"
                            cursor.execute(sql, (BaLL_No1, BaLL_No2, BaLL_No3,BaLL_No4, BaLL_No5, BaLL_No6, BaLL_No7, BaLL_No8,BaLL_No9, BaLL_No10, Cur_Award_Issue))
                            conn.commit()
                        else:
                            sql = "insert into data (issue, data1 , data2, data3, data4, data5, data6,data7, data8,data9, data10) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                            cursor.execute(sql, (Cur_Award_Issue, BaLL_No1, BaLL_No2, BaLL_No3,BaLL_No4, BaLL_No5, BaLL_No6, BaLL_No7, BaLL_No8,BaLL_No9, BaLL_No10))
                            conn.commit()                           
                        self.target.textlog.insert(tk.INSERT,"更新期号:" + Cur_Award_Issue + "\n")

                        #print("检测新订单是否已经存在" + Cur_Issue + "\n")
                        cursor.execute("select * from data where issue = ?", (Cur_Issue,))
                        Cur_Issue_datas = cursor.fetchall()
                        if len(Cur_Issue_datas) != 0:
                            continue

                        #print("获取所有路单数据\n")
                        cursor.execute("select * from data order by issue desc limit 10")
                        datas = cursor.fetchall()
                        if len(datas) == 0:
                            continue

                        #print("插入新路单" + Cur_Issue + "\n")
                        cursor.execute("insert into data(\"issue\") VALUES (?)", (Cur_Issue,))
                        conn.commit()   
                        
                        isdelorder = False
                        #print("检测上期的路单位数据" + Cur_Award_Issue + "\n")
                        cursor.execute("select * from data where issue = ? ", (Cur_Award_Issue,))
                        Cur_Award_Issue_datas = cursor.fetchall()
                        for Cur_Award_Issue_data in Cur_Award_Issue_datas:# 切换窗口
                            for BaLL_Idx in range(1, 11):
                                if Cur_Award_Issue_data[BaLL_Idx] != None:
                                    #print("位置 BaLL_Idx:" + str(BaLL_Idx))
                                    isdelorder |= delorder(driver, conn, cursor, Cur_Issue, BaLL_Idx, Cur_Award_Issue_data[BaLL_Idx + 10], Cur_Award_Issue_data[BaLL_Idx], monerys, loads, datas)   
                        
                        if isdelorder:
                            time.sleep(2)
                            #print("获取确定订单位置\n")            
                            driver.find_element_by_xpath("//*[@id=\"btn_order_2\"]").click()

                            time.sleep(2)
                            #print("获取确定alert位置\n")    
                            alert = driver.switch_to_alert()

                            time.sleep(2)  
                            #print("确认alert\n")
                            alert.accept()                           
                        ############################################################
                        driver.switch_to.parent_frame()
                    except NoSuchElementException as msg:
                        #print("NoSuchElementException:%s" % msg)
                        pass
                    except WebDriverException as msg:
                        #print("WebDriverException:%s" % msg)
                        pass
                    except NoSuchWindowException as msg:
                        #print("NoSuchWindowException:%s" % msg)
                        pass
                    except NoSuchAttributeException as msg:
                        #print("NoSuchAttributeException:%s" % msg)
                        pass
                    except NoAlertPresentException as msg:
                        #print("NoAlertPresentException:%s" % msg)
                        pass
                    except ElementNotVisibleException as msg:
                        #print("ElementNotVisibleException:%s" % msg)
                        pass
                    except ElementNotSelectableException as msg:
                        #print("ElementNotSelectableException:%s" % msg)
                        pass
                    except TimeoutException as msg:
                        #print("TimeoutException:%s" % msg)
                        pass
                    except Exception as msg:
                        #print("Exception:%s" % msg)
                        pass
                    except:
                        #print("error lineno:" + str(sys._getframe().f_lineno))
                        #self.target.textlog.insert(tk.INSERT,"error lineno:" +
                        #str(sys._getframe().f_lineno))
                        pass

            driver.quit()
            cursor.close()
            conn.close()
 
        self.target.textlog.insert(tk.INSERT,'Thread start\n')                   
        subthread = threading.Thread(target=target_func, args=())
        subthread.setDaemon(True)
        subthread.start()
    
        while not self.stopped:
            subthread.join(self.timeout)

        self.target.textlog.insert(tk.INSERT,'Thread stopped' + "\n")

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped

    
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.thread = None
        try:
            self.conn = sqlite3.connect('htd188.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS \"data\" (     \
            \"issue\"  varchar(20),   \
            \"data1\"  INTEGER,      \
            \"data2\"  INTEGER,     \
            \"data3\"  INTEGER,     \
            \"data4\"  INTEGER,     \
            \"data5\"  INTEGER,     \
            \"data6\"  INTEGER,     \
            \"data7\"  INTEGER,     \
            \"data8\"  INTEGER,     \
            \"data9\"  INTEGER,     \
            \"data10\"  INTEGER,    \
            \"order1\"  TEXT,       \
            \"order2\"  TEXT,       \
            \"order3\"  TEXT,       \
            \"order4\"  TEXT,       \
            \"order5\"  TEXT,       \
            \"order6\"  TEXT,       \
            \"order7\"  TEXT,       \
            \"order8\"  TEXT,       \
            \"order9\"  TEXT,       \
            \"order10\"  TEXT,      \
            PRIMARY KEY (\"issue\" ASC)      \
            );")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS \"monery\" (\"id\"  INTEGER NOT NULL,\"monery\"  INTEGER,\"win\"  INTEGER,\"loss\"  INTEGER,PRIMARY KEY (\"id\" ASC))")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS \"global\" (        \
            \"type\"  INTEGER,          \
            \"value\"  TEXT(56),        \
            PRIMARY KEY (\"type\" ASC)  \
            );                          \
            ")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS \"load\" (\"data\"  TEXT(1024)) ")
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
        ttk.Label(self.monty, text="网址:").grid(column=0, row=0, sticky='W')  
        # Adding a Textbox Entry widget
        self.url = tk.StringVar()  
        self.urlEntered = ttk.Entry(self.monty, width=60, textvariable=self.url)  
        self.urlEntered.grid(column=1, row=0, sticky='W')  


        # Changing our Label
        ttk.Label(self.monty, text="账号:").grid(column=0, row=1, sticky='W')  
        # Adding a Textbox Entry widget
        self.name = tk.StringVar()  
        self.nameEntered = ttk.Entry(self.monty, width=60, textvariable=self.name)  
        self.nameEntered.grid(column=1, row=1, sticky='W')  

        #第二行
        #ttk.Label(self.monty, text="请选择:").grid(column=0, row=1,sticky='W')
        #Adding a Combobox
        #self.book = tk.StringVar()
        #self.bookChosen = ttk.Combobox(self.monty, width=60, textvariable=self.book)
        #self.bookChosen['values'] = ('大', '小','单','双')
        #self.bookChosen.grid(column=1, row=1, sticky='W')
        #self.bookChosen.current(0)  #设置初始显示值，值为元组['values']的下标
        #self.bookChosen.config(state='readonly')  #设为只读模式
        #self.bookChosen.bind("<<ComboboxSelected>>", Chosen)  

        # Using a scrolled Text control
        self.scrolW = 80
        self.scrolH = 5

        #第三行
        ttk.Label(self.monty, text="金额策略(序号=金额=赢跳转序号=输跳转序号)").grid(column=0, row=2,sticky='W')
        #第四行
        self.monerytext = scrolledtext.ScrolledText(self.monty, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.monerytext.grid(column=0, row=3, sticky='WE', columnspan=3)
        #第五行
        # Adding a Button
        self.btaction = ttk.Button(self.monty,text="保存",width=10,command=self.savemonery).grid(column=1,row=4,sticky='E')   
        
        #第六行
        ttk.Label(self.monty, text="路单策略(大+大＝小)").grid(column=0, row=5,sticky='W')
        #第七行
        self.roadtext = scrolledtext.ScrolledText(self.monty, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.roadtext.grid(column=0, row=6, sticky='WE', columnspan=3)
        #第八行
        # Adding a Button
        self.btroadaction = ttk.Button(self.monty,text="保存",width=10,command=self.saveload).grid(column=1,row=7,sticky='E')   

        #第行
        ttk.Label(self.monty, text="日志信息:").grid(column=0, row=8, sticky='W')
        #第七行
        self.textlog = scrolledtext.ScrolledText(self.monty, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.textlog.grid(column=0, row=9, sticky='WE', columnspan=3)
        #第八行
        # Adding a Button
        self.btaction = ttk.Button(self.monty,text="开始",width=10,command=self.clickMe)
        self.btaction.grid(column=1,row=10,sticky='E')   
        # 一次性控制各控件之间的距离
        for child in self.monty.winfo_children(): 
            child.grid_configure(padx=3,pady=1)
        # 单独控制个别控件之间的距离
        #self.btaction.grid(column=2,row=1,rowspan=2,padx=6)
        #---------------Tab1控件介绍------------------#
        self.FlushData()
        
        self.cursor.execute('select * from global')
        datas = self.cursor.fetchall()
        for data in datas:# 切换窗口
            if data[0] == 1:
                self.nameEntered.insert(END, str(data[1]))
            if data[0] == 2:
                self.urlEntered.insert(END, str(data[1]))
        if self.nameEntered.get() == "":
            self.urlEntered.insert(END, "http://bw1.htd188.com/")
            
            
    def clickMe(self):
        if self.urlEntered.get() == "":
            messagebox.showerror("错误","请输入网址")
            return
        
        if self.nameEntered.get() == "":
            messagebox.showerror("错误","请输入账号")
            return 
        
        self.cursor.execute('delete from global')
        self.cursor.execute("replace into \"global\" (type, value) values  (?, ?)", (1, self.nameEntered.get()))
        self.cursor.execute("replace into \"global\" (type, value) values  (?, ?)", (2, self.urlEntered.get()))
        self.conn.commit()

        self.cursor.execute("select * from monery")
        monerys = self.cursor.fetchall()
        if len(monerys) == 0:
            messagebox.showerror("错误","金额策略未配置")
            return        
        

        url = "http://121.40.206.168/soft_net/SBDL_NSkt.php?NS=" + self.nameEntered.get()
        #print(url)
        request = urllib.request.Request(url, headers = headers)
        try:
            #response = urllib.request.urlopen(request)
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
        except urllib.error.HTTPError as e:
            #print('The server couldn\'t fulfill the request.')
            #print('Error code: ' + str(e.code))
            #print('Error reason: ' + e.reason)
            messagebox.showerror("错误","网络连接错误！")
            return
        except urllib.error.URLError as e:
            #print('We failed to reach a server.')
            #print('Reason: ' + e.reason)
            messagebox.showerror("错误","网络连接错误！")
            return
        except Exception as msg:
            print("Exception:%s" % msg)
            return
        except:
            #print("error lineno:" + str(sys._getframe().f_lineno))
            messagebox.showerror("错误","网络连接错误！")
            return
        html = html.strip()
        #print(html)
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
            self.thread = TestThread(self)
            self.thread.start()

    def savemonery(self):
        monerytext = self.monerytext.get(1.0, END)
        lines = monerytext.split("\n") 
        for line in lines:
            if line == "":
                continue
            items = line.split("=") 
            if len(items) != 4:
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
                if items[2] == item2s[0]:
                    win = True
                #失败
                if items[3] == item2s[0]:
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


    def saveload(self):
        roadtext = self.roadtext.get(1.0, END)
        lines = roadtext.split("\n") 
        for line in lines:
            if line == "":
                continue
            items = re.split('[＝=]',line)
            if len(items) != 2:
                messagebox.showerror("错误1","配置出错，请重新配置！")
                return
            print(items);
            tt = items[0].split("+") 
            if len(tt) == 0:
                messagebox.showerror("错误2","配置出错，请重新配置！")
                return
            
        self.cursor.execute('delete from load') 
        sql = "insert into load values('" + roadtext + "')"
        self.cursor.execute(sql)
        self.conn.commit()
        self.FlushData()
        messagebox.showinfo("提示","配置成功！")

    def Chosen(self, *args):  
        #print(self.bookChosen.get())
        pass
    
    def FlushData(self):
        self.monerytext.delete(0.0,len(self.monerytext.get(0.0,END)) - 1.0)
        self.cursor.execute('select * from monery')
        datas = self.cursor.fetchall()
        for data in datas:# 切换窗口
            self.monerytext.insert(tk.INSERT, str(data[0]) + "=" + str(data[1]) + "=" + str(data[2]) + "=" + str(data[3]) + "\n")

        self.roadtext.delete(0.0,len(self.roadtext.get(0.0,END)) - 1.0)
        self.cursor.execute('select * from load')
        datas = self.cursor.fetchall()
        for data in datas:# 切换窗口
            self.roadtext.insert(tk.INSERT, data[0] + "\n")
 
def main():
    app = Application()
    app.title("北京赛车 自动打码神器")
    app.resizable(0,0) #阻止Python GUI的大小调整
    # 主消息循环:
    app.mainloop()

if __name__ == "__main__":
    main()

