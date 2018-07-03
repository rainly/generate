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
from PIL import Image
from aip import AipOcr
from PIL import *
ssl._create_default_https_context = ssl._create_unverified_context

#声明一个CookieJar对象实例来保存cookie
cookiejar = http.cookiejar.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib.request.HTTPCookieProcessor(cookiejar)
#通过handler来构建opener
opener = urllib.request.build_opener(handler)

#此处的open方法同urllib2的urlopen方法，也可以传入request
#response = opener.open('http://www.baidu.com')
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'  
headers = { 'User-Agent' : user_agent }  

gurls   = ["https://22gvb.net:502","https://www.77msc.net:502", "https://www.66msc.net:502", "https://www.22gvb.net:502"]


""" 你的 APPID AK SK """
#APP_ID = '11249600'
#API_KEY = 'oCy0me9K6h9D19PxDA5ESLj5'
#SECRET_KEY = '2aPGdXMfq63ypzrR0lPiKmG6dKD8UaKh '

APP_ID = '11283483'
API_KEY = 'K5PIp9qko5UFOZxOyvbV5EwK'
SECRET_KEY = 'LA5wxlyBW7rfuQxzHKAGICz2oFdjsQRC  '

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def secureImg(base_url):
    url = base_url + "/Keypad/secureImg.aspx"
    print(url)
    request = urllib.request.Request(url, headers = headers)
    try:
        response = opener.open(request, timeout = 5)
        _image_bytes = response.read()
        # internal data file
        _data_stream = io.BytesIO(_image_bytes)
        # open as a PIL image object
        _pil_image = Image.open(_data_stream)
        
        #验证码识别
        _pil_image.save("code.jpg") 
        code_image = get_file_content('code.jpg')
        """ 调用通用文字识别, 图片参数为本地图片 """
        #{'log_id': 7581455648920966971, 'words_result_num': 1, 'words_result': [{'words': '5002'}]}
        result = client.basicGeneral(code_image);
        print(result)
        
        if "words_result" in result and len(result["words_result"]):
            print(result["words_result"][0]["words"])
            return result["words_result"][0]["words"]       
        else:
            return ""
    except urllib.error.HTTPError as e:
        print("HTTPError :", e.reason)
    except urllib.error.URLError as e:
        print("URLError :", e.reason)
    except Exception as e:
        print("Exception:%s" % (e))
    except:
        print("错误 ==> 网络连接错误！")
    return ""
    
def GetHttp(url, data = None, headers = {}, method = 'GET'):    
    request = urllib.request.Request(url, headers = headers, data = data, method = method)
    try:
        response = opener.open(request, timeout = 5)
        html = response.read().decode()
    except urllib.error.HTTPError as e:
        print("HTTPError :", e.reason)
        return None
    except urllib.error.URLError as e:
        print("URLError :", e.reason)
        return None
    except Exception as e:
        print("Exception:%s" % (e))
        return None
    except:
        print("错误 ==> 网络连接错误！")
        return None
    html = html.strip()
    print(html)
    return html    

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

    
def main():
    
    #生成config对象
    conf = configparser.ConfigParser()
    #用config对象读取配置文件
    conf.read("77msc.cfg")
    
    if conf.has_section("agent") == False:
        #增加新的section
        conf.add_section("agent")
        conf.set("agent", "Value", "xmiao89")
        #写回配置文件
        conf.write(open("77msc.cfg", "w"))
        print('配置出错，请正确配置代码名称1')
        time.sleep(10)
        return
    agent = conf.get("agent", "Value")

    print(agent)
    
    if conf.has_section("pwd") == False:
        #增加新的section
        conf.add_section("pwd")
        conf.set("pwd", "Value", "xmiao89")
        #写回配置文件
        conf.write(open("77msc.cfg", "w"))
        print('配置出错，请正确配置代码名称1')
        time.sleep(10)
        return
    pwd = conf.get("pwd", "Value")
    print(pwd)
    
    if conf.has_section("DoubleVerifyTextInput1") == False:
        #增加新的section
        conf.add_section("DoubleVerifyTextInput1")
        conf.set("DoubleVerifyTextInput1", "Value", "xmiao89")
        #写回配置文件
        conf.write(open("77msc.cfg", "w"))
        print('配置出错，请正确配置代码名称1')
        time.sleep(10)
        return
    DoubleVerifyTextInput1 = conf.get("DoubleVerifyTextInput1", "Value")       
    
    if conf.has_section("DoubleVerifyTextInput2") == False:
        #增加新的section
        conf.add_section("DoubleVerifyTextInput2")
        conf.set("DoubleVerifyTextInput2", "Value", "xmiao89")
        #写回配置文件
        conf.write(open("77msc.cfg", "w"))
        print('配置出错，请正确配置代码名称1')
        time.sleep(10)
        return
    DoubleVerifyTextInput2 = conf.get("DoubleVerifyTextInput2", "Value")     

    if conf.has_section("DoubleVerifyTextInput3") == False:
        #增加新的section
        conf.add_section("DoubleVerifyTextInput3")
        conf.set("DoubleVerifyTextInput3", "Value", "xmiao89")
        #写回配置文件
        conf.write(open("77msc.cfg", "w"))
        print('配置出错，请正确配置代码名称1')
        time.sleep(10)
        return
    DoubleVerifyTextInput3 = conf.get("DoubleVerifyTextInput3", "Value")      
    
    if conf.has_section("DoubleVerifyTextInput4") == False:
        #增加新的section
        conf.add_section("DoubleVerifyTextInput4")
        conf.set("DoubleVerifyTextInput4", "Value", "xmiao89")
        #写回配置文件
        conf.write(open("77msc.cfg", "w"))
        print('配置出错，请正确配置代码名称1')
        time.sleep(10)
        return
    DoubleVerifyTextInput4 = conf.get("DoubleVerifyTextInput4", "Value") 
    
    
    
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
    
    gurlidx = 0
    ##########################################################
    ##########################################################
    while True:#无限循环
        if gurlidx >= len(gurls):
            gurlidx = 0
        
        print(gurls[gurlidx])
        #######################################################
        
        print("################进入登陆页面#######################")
        html = GetHttp(gurls[gurlidx], headers = headers)
        if html == None:
            print("错误 ==> 获取网页数据为空")
            continue
        print("################进入登陆页面成功#######################")
        
        #######################################################
        
        print("################获取验证码#######################")
        while 1:
            code = secureImg(gurls[gurlidx])        
            if code == None or len(code) != 6:
                print("错误 ==> 获取网页数据为空")
                continue
            break
        print("################获取验证码成功#######################")
        #######################################################
        
        soup = BeautifulSoup(html, "lxml")
        
        #######################################################
        
        print("################开始登录认证 1#######################")
        url = gurls[gurlidx] + "/Login.aspx"
        logindict = {}
        logindict["__EVENTTARGET"]           = soup.find("input", {'id':"__EVENTTARGET"})["value"]
        logindict["__EVENTARGUMENT"]         = soup.find("input", {'id':"__EVENTARGUMENT"})["value"]  
        logindict["__LASTFOCUS"]             = soup.find("input", {'id':"__LASTFOCUS"})["value"]        
        logindict["__VIEWSTATE"]             = soup.find("input", {'id':"__VIEWSTATE"})["value"]
        logindict["wUserId"]                 = agent
        logindict["wSecureCd"]               = code
        logindict["btnSubmit"]               = "提 交"
        logindict["langMenuContainer"]       = 0
        logindict["wLangCode"]               = "简体中文"
        logindict["wloginStep"]              = 1
        logindict["wloginMethod"]            = ""
        logindict["wScore"]                  = 0
        #print(logindict)
        data = urllib.parse.urlencode(logindict).encode('utf-8')
        html = GetHttp(url = url, data = data, headers = headers, method = 'POST')
        if html == None:
            print("错误 ==> 获取网页数据为空")
            continue        
        print("################登录成功 1#######################")  
        #######################################################

        soup = BeautifulSoup(html, "lxml")

        #######################################################
        print("################开始登录认证 2#######################")
        url = gurls[gurlidx] + "/Login.aspx"
        logindict = {}
        logindict["__EVENTTARGET"]           = soup.find("input", {'id':"__EVENTTARGET"})["value"]
        logindict["__EVENTARGUMENT"]         = soup.find("input", {'id':"__EVENTARGUMENT"})["value"]  
        logindict["__LASTFOCUS"]             = soup.find("input", {'id':"__LASTFOCUS"})["value"]        
        logindict["__VIEWSTATE"]             = soup.find("input", {'id':"__VIEWSTATE"})["value"]
        logindict["wPwd"]                    = pwd
        logindict["btnSubmit"]               = "提 交"
        logindict["langMenuContainer"]       = 0
        logindict["wLangCode"]               = "简体中文"
        logindict["wloginStep"]              = 2
        logindict["wloginMethod"]            = 1
        logindict["wScore"]                  = 0
        #print(logindict)
        data = urllib.parse.urlencode(logindict).encode('utf-8')
        html = GetHttp(url = url, data = data, headers = headers, method = 'POST')
        if html == None:
            print("错误 ==> 获取网页数据为空")
            continue        
        print("################登录成功 2#######################")   
        
        #######################################################
        
        soup = BeautifulSoup(html, "lxml")
        
        #######################################################
        print("################开始登录认证 3#######################")
        url = gurls[gurlidx] + "/Login.aspx"
        logindict = {}
        logindict["__EVENTTARGET"]           = soup.find("input", {'id':"__EVENTTARGET"})["value"]
        logindict["__EVENTARGUMENT"]         = soup.find("input", {'id':"__EVENTARGUMENT"})["value"]  
        logindict["__LASTFOCUS"]             = soup.find("input", {'id':"__LASTFOCUS"})["value"]        
        logindict["__VIEWSTATE"]             = soup.find("input", {'id':"__VIEWSTATE"})["value"]
        logindict["wDoubleVerifyTextInput1"]                    = DoubleVerifyTextInput1
        logindict["wDoubleVerifyTextInput2"]                    = DoubleVerifyTextInput2
        logindict["wDoubleVerifyTextInput3"]                    = DoubleVerifyTextInput3
        logindict["wDoubleVerifyTextInput4"]                    = DoubleVerifyTextInput4
        logindict["btnSubmit"]               = "提 交"
        logindict["langMenuContainer"]       = 0
        logindict["wLangCode"]               = "简体中文"
        logindict["wloginStep"]              = 4
        logindict["wloginMethod"]            = 1
        logindict["wScore"]                  = 0
        #print(logindict)
        data = urllib.parse.urlencode(logindict).encode('utf-8')
        html = GetHttp(url = url, data = data, headers = headers, method = 'POST')
        if html == None:
            print("错误 ==> 获取网页数据为空")
            continue        
        print("################登录成功 3#######################")   
            
        #######################################################

        
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

































