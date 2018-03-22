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



#北京11选5
#http://kaijiang.500.com/static/info/kaijiang/xml/bjsyxw/20180322.xml?_A=LVJPOEQK1521729306270

#北京PK拾
#http://kaijiang.500.com/static/info/kaijiang/xml/bjpkshi/20180321.xml?_A=FGDQZMKT1521729519875

#江苏快3
#http://kaijiang.500.com/static/info/kaijiang/xml/jsk3/20180321.xml?_A=PUZYNSBT1521729576222

#重庆时时彩
#http://kaijiang.500.com/static/public/ssc/xml/qihaoxml/20180322.xml?_A=PEQZSKNM1521729618019

ssc_con = {
        "北京11选5":{ "type":1, "head":"http://kaijiang.500.com/static/info/kaijiang/xml/bjsyxw/", "end":".xml?_A=LVJPOEQK1521729306270"},
        "北京PK拾":{ "type":2, "head":"http://kaijiang.500.com/static/info/kaijiang/xml/bjpkshi/", "end":".xml?_A=FGDQZMKT1521729519875"},
        "江苏快3":{ "type":3, "head":"http://kaijiang.500.com/static/info/kaijiang/xml/jsk3/", "end":".xml?_A=PUZYNSBT1521729576222"},
        "重庆时时彩":{ "type":4, "head":"http://kaijiang.500.com/static/public/ssc/xml/qihaoxml/", "end":".xml?_A=PEQZSKNM1521729618019"},
    }
    
def main():

    #生成config对象
    conf = configparser.ConfigParser()
    #用config对象读取配置文件
    conf.read("77msc.cfg")



    # 连接数据库
    connect = pymysql.Connect(
        host='115.126.47.35',
        port=3306,
        user='root',
        passwd='zaq!@#$1234rfv',
        db='blog',
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
    cookiejar = http.cookiejar.CookieJar()
    #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler=urllib.request.HTTPCookieProcessor(cookiejar)
    #通过handler来构建opener
    opener = urllib.request.build_opener(handler)

    #此处的open方法同urllib2的urlopen方法，也可以传入request
    #response = opener.open('http://www.baidu.com')
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'  
    headers = { 'User-Agent' : user_agent }  
    
    #################################################
    day = 0
    while True:#无限循环
        #time.sleep(1)
        print('获取数据')
        print(get_days_before_today(day).strftime('%Y-%m-%d'))
    
        for key in ssc_con:
            print(key)
            url = ssc_con[key]["head"] + get_days_before_today(day).strftime('%Y%m%d') + ssc_con[key]["end"]   
            try:
                html = ""
                sql = ""
                num = 0 
                print('正在抓取数据 <---  ' + url)
                request = urllib.request.Request(url, headers = headers)
                response = opener.open(request, timeout = 15)
                html = response.read().decode()
                #print(html);
                soup = BeautifulSoup(html, "lxml")
                #<row  expect="18032184" opencode="10,02,07,11,06" opentime="2018-03-21 22:50:30" />
                sql     = "INSERT INTO ssc_data (`type`,`expect`,`opencode`,`opentime`) VALUES "
                for row in soup.find_all('row'):
                    if num != 0:
                        sql = sql + ","
                    num  = num + 1
                    
                    sql  = sql + "(%d, '%s', '%s', '%s')"
                    data = (ssc_con[key]["type"], row["expect"], row["opencode"], row["opentime"])
                    sql  = sql % data
                if num > 0:
                    sql = sql + "on duplicate key update ssc_data.opencode = values(ssc_data.opencode)"
                    sql = sql + ", ssc_data.opentime = values(ssc_data.opentime)"
                    cursor.execute(sql)
            except:
                connect.rollback()  # 事务回滚
                print(":error lineno:"+str(sys._getframe().f_lineno))
                print(html)
                print(sql)
                pass
            else:
                connect.commit()
                print('获取数据成功 更新', cursor.rowcount, '条数据')
        day = day + 1
    # 关闭连接
    cursor.close()
    connect.close()    
    print("----------------------end-------------------")
        
if __name__ == "__main__":
    main()

































