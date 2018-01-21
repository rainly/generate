## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
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
ssl._create_default_https_context = ssl._create_unverified_context



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
def main():
    #生成config对象
    conf = configparser.ConfigParser()
    #用config对象读取配置文件
    conf.read("a8033.txt")

    if conf.has_section("url") == False:
        printf("配置出错")
        time.sleep(3600)
        return
    url = conf.get("url", "value")
    print("地址:" + url)

    if conf.has_section("url") == False:
        printf("配置出错")
        time.sleep(3600)
        return
    jump = conf.get("jump", "value")
    print("输停:" + jump)

    if conf.has_section("monery") == False:
        printf("配置出错")
        time.sleep(3600)
        return
    monery = conf.get("monery", "value")
    print("下注金额:" + monery)
    
    if conf.has_section("agent") == False:
        printf("配置出错")
        time.sleep(3600)
        return
    agent = conf.get("agent", "value")
    print("代理:" + agent)    
    
    url_agent = "http://121.40.206.168/soft_net/SBDL_NSkt.php?NS=" + agent
    print(url_agent)
    request = urllib.request.Request(url_agent, headers = headers)
    try:
        #response = urllib.request.urlopen(request)
        response = opener.open(request, timeout = 5)
        html = response.read().decode()
    except urllib.error.HTTPError as e:
        #print('The server couldn\'t fulfill the request.')
        #print('Error code: ' + str(e.code))
        #print('Error reason: ' + e.reason)
        print("错误","网络连接错误！")
        time.sleep(3600)
        return
    except urllib.error.URLError as e:
        #print('We failed to reach a server.')
        #print('Reason: ' + e.reason)
        print("错误","网络连接错误！")
        time.sleep(3600)
        return
    except Exception as msg:
        print("Exception:%s" % msg)
        return
    except:
        #print("error lineno:" + str(sys._getframe().f_lineno))
        print("错误","网络连接错误！")
        time.sleep(3600)
        return
    html = html.strip()
    #print(html)
    if html != "1":
        print("错误","账号未注册！")
        return    
    
    jumps   = jump.split("+")
    monerys = monery.split("+")
    if len(jumps) + 1 != len(monerys):
        printf("输停长度 ！= 下注金额长度")
        time.sleep(3600)
        return
    jumps.append("0")    
        
    
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(5)
    
        
    try:
        
        while True:
            isJump = False
            handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
            #print(handles) # 输出句柄集合
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
        Last_Award_Issue_Have = False
        Jump_Idx   = 0
        Stop_num   = 0

        while True:
            try:
                time.sleep(5)
                if  Jump_Idx >= len(jumps):
                    print("***自动停止***")
                    time.sleep(1000)
                    continue

                print("********************************************************")
                Cur_Award_Issue1_1 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[1]/td[1]").text
                #Cur_Award_Issue1_2 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[1]/td[2]").text
                print(Cur_Award_Issue1_1)

                Cur_Award_Issue2_1 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[2]/td[1]").text
                #Cur_Award_Issue2_2 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[2]/td[2]").text
                print(Cur_Award_Issue2_1)
                
                if Cur_Award_Issue1_1 == Last_Award_Issue:
                    print("***等待开奖***")
                    continue

                Last_Award_Issue = Cur_Award_Issue1_1
                #处理中奖结果
                if Last_Award_Issue_Have:
                    print("***处理中奖结果***")
                    tclass = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div/table/tbody/tr[2]/td[2]/span").get_attribute("class")
                    print(tclass)
                    #<span class="LD-resultItem LD--s LD--l4o">单4</span>
                    #<span class="LD-resultItem LD--s LD--r4e">双4</span>
                    #<span class="LD-resultItem LD--s LD--r3o">单3</span>
                    #<span class="LD-resultItem LD--s LD--l3e">双3</span>
                    
                    Last_Award_Issue_Win = False
                    if tclass == "LD-resultItem LD--s LD--l4o":
                        print("***开奖***单4")
                        Last_Award_Issue_Win = True
                        pass
                    elif  tclass == "LD-resultItem LD--s LD--r4e":
                        Last_Award_Issue_Win = True
                        print("***开奖***双4")
                        pass
                    elif  tclass == "LD-resultItem LD--s LD--l3e":
                        Last_Award_Issue_Win = True
                        print("***开奖***双3")
                        pass
                    elif  tclass == "LD-resultItem LD--s LD--r3o":
                        Last_Award_Issue_Win = False
                        print("***开奖***单3")
                        pass
                    else:
                        Last_Award_Issue_Win = False
                        print("***等待开奖***单3")
                        pass                     
                    
                    if Last_Award_Issue_Win == True:
                        Jump_Idx    = 0
                        Stop_num    = 0
                        print("***中奖***")
                    else:
                        Stop_num    = 1
                        print("***未中奖***")
                        
                #print("***Stop_num:" + str(Stop_num))
                #print("***Jump_Idx:" + str(Jump_Idx))
                #print("***jumps[Jump_Idx]:" + jumps[Jump_Idx])
                if Stop_num != 0  and Stop_num <= int(jumps[Jump_Idx]) :
                    Last_Award_Issue_Have = False
                    Stop_num = Stop_num + 1
                    print("***不下注***")
                    continue
                elif Stop_num != 0 and Stop_num > int(jumps[Jump_Idx]):
                    Jump_Idx   = Jump_Idx + 1
                    
                if  Jump_Idx >= len(jumps):
                    print("***自动停止***")
                    continue
                Last_Award_Issue_Have = True                               
                Stop_num    = 0   
                print("***开始下注***" + Cur_Award_Issue1_1)
                #print("***Stop_num:" + str(Stop_num))
                #print("***Jump_Idx:" + str(Jump_Idx))
                #print("***jumps[Jump_Idx]:" + jumps[Jump_Idx])
                #print("***monerys[Jump_Idx]:" + monerys[Jump_Idx])

                input1 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/table/tbody/tr[2]/td[4]/div[1]/input")
                input2 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/table/tbody/tr[2]/td[4]/div[2]/input")
                input3 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/table/tbody/tr[2]/td[4]/div[3]/input")
                input4 = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/main/div/div/div[3]/table/tbody/tr[2]/td[4]/div[4]/input")
                
                input2.clear()
                input2.send_keys(monerys[Jump_Idx])
                time.sleep(1)
                input3.clear()
                input3.send_keys(monerys[Jump_Idx])
                time.sleep(1)
                input4.clear()
                input4.send_keys(monerys[Jump_Idx])
                time.sleep(1)
                #print("获取确定订单位置\n")            
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
if __name__ == "__main__":
    main()
