## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
#跟投抓包数据
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
import configparser
ssl._create_default_https_context = ssl._create_unverified_context
    
def main():

    #生成config对象
    conf = configparser.ConfigParser()
    #用config对象读取配置文件
    conf.read("77msc.cfg")



    # 连接数据库
    connect = pymysql.Connect(
        host='duboren123.mysql.rds.aliyuncs.com',
        port=3306,
        user='root',
        passwd='DBRaly123',
        db='duboren',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor()


    def get_days_before_today(n=0):
        '''
        date format = "YYYY-MM-DD HH:MM:SS"
        '''
        now = datetime.datetime.now()  
        if(n<0):  
            return datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)  
        else:  
            n_days_before = now - datetime.timedelta(days=n)  
        return datetime.datetime(n_days_before.year, n_days_before.month, n_days_before.day, n_days_before.hour, n_days_before.minute, n_days_before.second)
    #print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
    #print(get_days_before_today(2).strftime('%Y-%m-%d'))

        
    #声明一个CookieJar对象实例来保存cookie
    cookiejar = cookiejar = http.cookiejar.CookieJar()
    #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler=urllib.request.HTTPCookieProcessor(cookiejar)
    #通过handler来构建opener
    opener = urllib.request.build_opener(handler)

    #此处的open方法同urllib2的urlopen方法，也可以传入request
    #response = opener.open('http://www.baidu.com')
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'  
    headers = { 'User-Agent' : user_agent }  
        
    gurlidx = 0
    gurls = ["https://www.77msc.net:502", "https://www.66msc.net:502", "https://www.22gvb.net:502"]
    ##########################################################
    ##########################################################
    while True:#无限循环
        if gurlidx >= len(gurls):
            gurlidx = 0
        print(gurls[gurlidx])

        if conf.has_section("agent") == False:
            #增加新的section
            conf.add_section("agent")
            conf.set("agent", "Value", "xmiao89")
            #写回配置文件
            conf.write(open("77msc.cfg", "w"))
            print('配置出错，请正确配置代码名称1')
            time.sleep(1)
            continue
        agent = conf.get("agent", "Value")
        
        url = "http://121.40.206.168/SOFT_net/SBDL_data.php?name=" + agent
        #print(agent + ':正在获取代理数据 <---  ' + url)
        print(agent + ":正在登录 1")
        request = urllib.request.Request(url, headers = headers)
        try:
            #response = urllib.request.urlopen(request)
            response = opener.open(request, timeout = 15)
        except:
            print('配置出错，请正确配置代码名称3')
            time.sleep(1)
            gurlidx = gurlidx + 1
            continue  

        html = None
        try:
            html = response.read().decode()
        except:
            
            print('配置出错，请正确配置代码名称3')
            time.sleep(1)
            gurlidx = gurlidx + 1
            continue  
            
        if html == None:
            
            print('配置出错，请正确配置代码名称3')
            time.sleep(1)
            gurlidx = gurlidx + 1
            continue  
        
        #print(agent + ':获取代理数据 <---  ' + html)
        html = html.replace("\r\n", "")
        #print(agent + ':获取代理数据 <---  ' + html)
        urls = html.split("wocaonima")
        if len(urls) != 3:
            print('配置出错，请正确配置代码名称3')
            time.sleep(1)
            gurlidx = gurlidx + 1
            continue    

        #print(agent + ":分割数据1-->" + urls[0])
        #print(agent + ":分割数据2-->" + urls[1])
        #print(agent + ":分割数据3-->" + urls[2])
        #######################################################
        url = gurls[gurlidx] + "/Login.aspx"
        #print(agent + ':正在抓取首页 <---  ' + url)
        print(agent + ":正在登录 2")
        request = urllib.request.Request(url, headers = headers)
        try:
            #response = urllib.request.urlopen(request)
            response = opener.open(request, timeout = 15)
        except:
            print(agent + ":error lineno:"+str(sys._getframe().f_lineno))
            pass

        try:
            html = response.read().decode()
        except:
            print(agent + ":error lineno:"+str(sys._getframe().f_lineno))
            pass



        
        url = gurls[gurlidx] + "/Login.aspx"
        data = bytes(urls[0], encoding = "utf8")
        print(agent + ":正在登录 3")
        request = urllib.request.Request(url, data, headers)
        try:
            #response = urllib.request.urlopen(request)
            response = opener.open(request, timeout = 15)
        except:
            print(agent + ":error lineno:"+str(sys._getframe().f_lineno))
            pass
        
        try:
            html = response.read().decode()
        except:
            print(agent + ":error lineno:"+str(sys._getframe().f_lineno))
            pass
        

        url = gurls[gurlidx] + "/Login.aspx"
        print(agent + ":正在登录 4")
        data = bytes(urls[1], encoding = "utf8")
        request = urllib.request.Request(url, data, headers)
        try:
            #response = urllib.request.urlopen(request)
            response = opener.open(request, timeout = 15)
        except:
            print(agent + ":error lineno:"+str(sys._getframe().f_lineno))
            pass
        
        try:
            html = response.read().decode()
        except:
            print(agent + ":error lineno:"+str(sys._getframe().f_lineno))
            pass
        
        
        url = gurls[gurlidx] + "/Login.aspx"
        print(agent + '正在登录 5')
        data = bytes(urls[2], encoding = "utf8")
        request = urllib.request.Request(url, data, headers)
        try:
            #response = urllib.request.urlopen(request)
            response = opener.open(request, timeout = 15)
        except:
            print(agent + ":error lineno:"+str(sys._getframe().f_lineno))
            pass
        
        try:
            html = response.read().decode()
        except:
            print(agent + ":error lineno:"+str(sys._getframe().f_lineno))
            pass
        
        print(agent + ':登录成功')

        ready = True
        #################################################
        while ready:#无限循环
            time.sleep(1)
            print(agent + '获取数据')
            url = gurls[gurlidx] + "/Reports/BetMonitor.aspx"
                
            try:
                #print(agent + ':正在抓取数据 <---  ' + url)
                request = urllib.request.Request(url, headers = headers)
                response = opener.open(request, timeout = 15)
                html = response.read().decode()
                #print(agent + ':删除数据')
                sql = "delete from soft_77msc where agent = '" + agent + "'"
                cursor.execute(sql)
                sql = "delete from soft_77msc_user where agent = '" + agent + "'"
                cursor.execute(sql)
                #print(agent + ':BeautifulSoup解析')
                dealcount = 0
                soup = BeautifulSoup(html, "lxml")
                for table in soup.find_all('table'):
                    if table.get("id") == "gridSummary":
                        dealcount = dealcount + 1
                        #print(agent + ":gridSummary")
                        row     = 0 
                        sql     = "INSERT INTO soft_77msc (`agent`, `tableNo`, `type`, `date`, `state`, `number`, `bootsnumber`, `downlinebets`, `downlinemonery`, `result1`, `result2`, `result3`, `lastresult`) VALUES "
                    
                        for tr in table.find_all('tr'):
                            tds = tr.find_all('td')
                            if len(tds) == 0:
                                continue
                            if len(tds) != 12:
                                continue
                            if tds[0].get_text() == "":
                                continue
                            if tds[0].get_text() == " ":
                                continue
                            if row != 0:
                                sql = sql + ","
                            row  = row + 1
                            sql  = sql + "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                            data = (agent, tds[0].get_text(), tds[1].get_text(), tds[2].get_text(), tds[3].get_text(), tds[4].get_text(), tds[5].get_text(), tds[6].get_text(), tds[7].get_text(), tds[8].get_text(), tds[9].get_text(), tds[10].get_text(), tds[11].get_text())
                            sql  = sql % data

                        if row > 0:
                            #print(agent + ":######################执行SQL语句################################")
                            sql = sql + "on duplicate key update soft_77msc.tableNo = values(soft_77msc.tableNo)"
                            sql = sql + ", soft_77msc.agent = values(soft_77msc.agent)"
                            sql = sql + ", soft_77msc.type = values(soft_77msc.type)"
                            sql = sql + ", soft_77msc.date = values(soft_77msc.date)"
                            sql = sql + ", soft_77msc.state = values(soft_77msc.state)"
                            sql = sql + ", soft_77msc.number = values(soft_77msc.number)"
                            sql = sql + ", soft_77msc.bootsnumber = values(soft_77msc.bootsnumber)"
                            sql = sql + ", soft_77msc.downlinebets = values(soft_77msc.downlinebets)"
                            sql = sql + ", soft_77msc.downlinemonery = values(soft_77msc.downlinemonery)"
                            sql = sql + ", soft_77msc.result1 = values(soft_77msc.result1)"
                            sql = sql + ", soft_77msc.result2 = values(soft_77msc.result2)"
                            sql = sql + ", soft_77msc.result3 = values(soft_77msc.result3)"
                            sql = sql + ", soft_77msc.lastresult = values(soft_77msc.lastresult)"
                            #print(sql)
                            cursor.execute(sql)
                    if table.get("id") == "gridDetail":
                        #print(agent + ":gridDetail")
                        dealcount = dealcount + 1
                        row     = 0
                        sql     = "INSERT INTO soft_77msc_user (`agent`, `agentid`, `membername`, `bettingdate`, `tableno`, `type`, `member`, `bootsnumber`, `betting`, `bettingmonery`) VALUES "
                        for tr in table.find_all('tr'):
                            tds = tr.find_all('td')
                            if len(tds) == 0:
                                continue
                            if len(tds) != 9:
                                continue
                            if tds[0].get_text() == "":
                                continue
                            if tds[0].get_text() == " ":
                                continue
                            if row != 0:
                                sql = sql + ","
                            row  = row + 1
                            sql  = sql + "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                            data = (agent, tds[0].get_text(), tds[1].get_text(), tds[2].get_text(), tds[3].get_text(), tds[4].get_text(), tds[5].get_text(), tds[6].get_text(), tds[7].get_text(), tds[8].get_text())
                            sql  = sql % data

                        if row > 0:
                            #print(agent + ":######################执行SQL语句################################")
                            sql = sql + "on duplicate key update soft_77msc_user.agent = values(soft_77msc_user.agent)"
                            sql = sql + ", soft_77msc_user.agentid = values(soft_77msc_user.agentid)"
                            sql = sql + ", soft_77msc_user.membername = values(soft_77msc_user.membername)"
                            sql = sql + ", soft_77msc_user.bettingdate = values(soft_77msc_user.bettingdate)"
                            sql = sql + ", soft_77msc_user.tableno = values(soft_77msc_user.tableno)"
                            sql = sql + ", soft_77msc_user.type = values(soft_77msc_user.type)"
                            sql = sql + ", soft_77msc_user.member = values(soft_77msc_user.member)"
                            sql = sql + ", soft_77msc_user.bootsnumber = values(soft_77msc_user.bootsnumber)"
                            sql = sql + ", soft_77msc_user.betting = values(soft_77msc_user.betting)"
                            sql = sql + ", soft_77msc_user.bettingmonery = values(soft_77msc_user.bettingmonery)"
                            cursor.execute(sql)                
                if dealcount == 0:
                    ready = False
            except:
                ready = False
                connect.rollback()  # 事务回滚
                print(agent + ":error lineno:"+str(sys._getframe().f_lineno))
                #print(msg)
                pass
            else:
                connect.commit()
                print(agent + '获取数据成功 更新', cursor.rowcount, '条数据')   

    # 关闭连接
    cursor.close()
    connect.close()    
    print(agent + ":----------------------end-------------------")
        
if __name__ == "__main__":
    main()

































