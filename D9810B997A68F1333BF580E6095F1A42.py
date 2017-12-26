# coding='UTF-8'
from bs4 import BeautifulSoup  # 引入beautifulsoup 解析html事半功倍
import re
import urllib
import urllib.request
import urllib.response
import urllib.error
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


ssl._create_default_https_context = ssl._create_unverified_context

agent = "D9810B997A68F1333BF580E6095F1A42"

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

##########################################################
##########################################################
while True:#无限循环
    url = "http://121.40.206.168/SOFT_net/SBDL_data.php?name=" + agent
    print('正在抓取首页 <---  ' + url)
    request = urllib.request.Request(url, headers = headers)
    try:
        #response = urllib.request.urlopen(request)
        response = opener.open(request, timeout = 5)
        html = response.read().decode()
    except urllib.error.HTTPError as e:
        print ( 'The server couldn\'t fulfill the request.')
        print ('Error code: ' +str( e.code))
        print ('Error reason: ' + e.reason)
    except urllib.error.URLError as e:
        print ('We failed to reach a server.')
        print ('Reason: ' + e.reason)
    except:
        print("error lineno:"+str(sys._getframe().f_lineno))
        continue;

    print('获取登录数据 <---  ' + html)
    html = html.replace("\r\n", "")
    print('获取登录数据 <---  ' + html)
    urls = html.split("wocaonima")
    if len(urls) != 3:
        continue;    

    print("分割数据1-->" + urls[0])
    print("分割数据2-->" + urls[1])
    print("分割数据3-->" + urls[2])
    #######################################################
    url = "https://www.77msc.net:502/Login.aspx"
    print('正在抓取首页 <---  ' + url)
    request = urllib.request.Request(url, headers = headers)
    try:
        #response = urllib.request.urlopen(request)
        response = opener.open(request, timeout = 5)
        html = response.read().decode()
    except urllib.error.HTTPError as e:
        print ( 'The server couldn\'t fulfill the request.')
        print ('Error code: ' +str( e.code))
        print ('Error reason: ' + e.reason)
        print("error lineno:"+str(sys._getframe().f_lineno))
    except urllib.error.URLError as e:
        print ('We failed to reach a server.')
        print ('Reason: ' + e.reason)
        print("error lineno:"+str(sys._getframe().f_lineno))
    except:
        print("error lineno:"+str(sys._getframe().f_lineno))
        print("error lineno:"+str(sys._getframe().f_lineno))
        continue;

    url = "https://www.77msc.net:502/Login.aspx"
    print('正在登录1 <---  ' + url);
    data = bytes(urls[0], encoding = "utf8")
    request = urllib.request.Request(url, data, headers)
    try:
        #response = urllib.request.urlopen(request)
        response = opener.open(request, timeout = 5)
        html = response.read().decode()
    except urllib.error.HTTPError as e:
        print ( 'The server couldn\'t fulfill the request.')
        print ('Error code: ' +str( e.code))
        print ('Error reason: ' + e.reason)
        print("error lineno:"+str(sys._getframe().f_lineno))
    except urllib.error.URLError as e:
        print ('We failed to reach a server.')
        print ('Reason: ' + e.reason)
        print("error lineno:"+str(sys._getframe().f_lineno))
    #except:
    #    print("error lineno:"+str(sys._getframe().f_lineno))
    #    continue;
	
    #print(html)
    
    url = "https://www.77msc.net:502/Login.aspx"
    print('正在登录2 <---  ' + url);
    data = bytes(urls[1], encoding = "utf8")
    request = urllib.request.Request(url, data, headers)
    try:
        #response = urllib.request.urlopen(request)
        response = opener.open(request, timeout = 5)
        html = response.read().decode()
    except urllib.error.HTTPError as e:
        print ( 'The server couldn\'t fulfill the request.')
        print ('Error code: ' +str( e.code))
        print ('Error reason: ' + e.reason)
        print("error lineno:"+str(sys._getframe().f_lineno))
    except urllib.error.URLError as e:
        print ('We failed to reach a server.')
        print ('Reason: ' + e.reason)
        print("error lineno:"+str(sys._getframe().f_lineno))
    #except:
    #    print("error lineno:"+str(sys._getframe().f_lineno))
    #    continue;
        
    #print(html)
    
    url = "https://www.77msc.net:502/Login.aspx"
    print('正在登录3 <---  ' + url);
    data = bytes(urls[2], encoding = "utf8")
    request = urllib.request.Request(url, data, headers)
    try:
        #response = urllib.request.urlopen(request)
        response = opener.open(request, timeout = 5)
        html = response.read().decode()
    except urllib.error.HTTPError as e:
        print ( 'The server couldn\'t fulfill the request.')
        print ('Error code: ' +str( e.code))
        print ('Error reason: ' + e.reason)
        print("error lineno:"+str(sys._getframe().f_lineno))
    except urllib.error.URLError as e:
        print ('We failed to reach a server.')
        print ('Reason: ' + e.reason)
        print("error lineno:"+str(sys._getframe().f_lineno))
    #except:
    #    print("error lineno:"+str(sys._getframe().f_lineno))
    #    continue;

    #print(html)
    ready = True
    #################################################
    while ready:#无限循环
        #time.sleep(1)
        url = "https://www.77msc.net:502/Reports/BetMonitor.aspx"
            
        try:
            print('正在抓取数据 <---  ' + url)
            request = urllib.request.Request(url, headers = headers)
            response = opener.open(request, timeout = 5)
            html = response.read().decode()
            print('抓取数据 <---  ' + html)
            print('删除数据 soft_77msc')
            sql = "delete from soft_77msc where agent = '" + agent + "'";
            cursor.execute(sql)
            print('删除数据 soft_77msc_user')
            sql = "delete from soft_77msc_user where agent = '" + agent + "'";
            cursor.execute(sql)
            print('BeautifulSoup解析')
            dealcount = 0
            soup = BeautifulSoup(html, "lxml")
            for table in soup.find_all('table'):
                if table.get("id") == "gridSummary":
                    dealcount = dealcount + 1;
                    print("gridSummary")
                    row     = 0 
                    sql     = "INSERT INTO soft_77msc (`agent`, `tableNo`, `type`, `date`, `state`, `number`, `bootsnumber`, `downlinebets`, `downlinemonery`, `result1`, `result2`, `result3`, `lastresult`) VALUES "
                
                    for tr in table.find_all('tr'):
                        tds = tr.find_all('td')
                        if len(tds) == 0:
                            continue;
                        if len(tds) != 12:
                            continue;
                        if tds[0].get_text() == "":
                            continue;
                        if tds[0].get_text() == " ":
                            continue;
                        if row != 0:
                            sql = sql + ","
                        row  = row + 1
                        sql  = sql + "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                        data = (agent, tds[0].get_text(), tds[1].get_text(), tds[2].get_text(), tds[3].get_text(), tds[4].get_text(), tds[5].get_text(), tds[6].get_text(), tds[7].get_text(), tds[8].get_text(), tds[9].get_text(), tds[10].get_text(), tds[11].get_text())
                        sql  = sql % data

                    if row > 0:
                        print("######################执行SQL语句################################")
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
                    print("gridDetail")
                    dealcount = dealcount + 1;
                    row     = 0
                    sql     = "INSERT INTO soft_77msc_user (`agent`, `agentid`, `membername`, `bettingdate`, `tableno`, `type`, `member`, `bootsnumber`, `betting`, `bettingmonery`) VALUES "
                    for tr in table.find_all('tr'):
                        tds = tr.find_all('td')
                        if len(tds) == 0:
                            continue;
                        if len(tds) != 9:
                            continue;
                        if tds[0].get_text() == "":
                            continue;
                        if tds[0].get_text() == " ":
                            continue;
                        if row != 0:
                            sql = sql + ","
                        row  = row + 1
                        sql  = sql + "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                        data = (agent, tds[0].get_text(), tds[1].get_text(), tds[2].get_text(), tds[3].get_text(), tds[4].get_text(), tds[5].get_text(), tds[6].get_text(), tds[7].get_text(), tds[8].get_text())
                        sql  = sql % data

                    if row > 0:
                        print("######################执行SQL语句################################")
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
                print("error dealcount:"+str(sys._getframe().f_lineno))
                ready = False
        except urllib.error.HTTPError as e:
            ready = False
            connect.rollback()  # 事务回滚
            print ('The server couldn\'t fulfill the request.')
            print ('Error code: ' +str( e.code))
            print ('Error reason: ' + e.reason)
            print("error lineno:"+str(sys._getframe().f_lineno))
        except urllib.error.URLError as e:
            ready = False
            connect.rollback()  # 事务回滚
            print ('We failed to reach a server.')
            print ('Reason: ', e.reason)
            print("error lineno:"+str(sys._getframe().f_lineno))
        #except:
        #    ready = False
        #    connect.rollback()  # 事务回滚
        #    print("error lineno:"+str(sys._getframe().f_lineno))
        #    print("error lineno:"+str(sys._getframe().f_lineno))
        else:
            connect.commit()
            print('提交事物成功', cursor.rowcount, '条数据')   
        
# 关闭连接
cursor.close()
connect.close()    
print("----------------------end-------------------")



































