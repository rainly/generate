## -*- coding: utf-8 -*-
##Author：哈士奇说喵
#pyinstaller
#BB彩票-双面玩法
    
import threading  
import time
import configparser
import random
import copy
import re  #python的正则表达式模块
import os
import sys
import zlib
import hashlib
import json
import datetime
import pymysql.cursors
from LightMysql import LightMysql
import codecs

config_cptypes = {}
config_cptypes["北京11选5"]   = {"BallNum":5,  "type":1} 
config_cptypes["北京PK拾"]    = {"BallNum":10, "type":2} 
config_cptypes["江苏快3"]     = {"BallNum":3,  "type":3} 
config_cptypes["重庆时时彩"]  = {"BallNum":5,  "type":4} 


class CPAnalyze:
    def __init__(self):
        self.cutin  = 10
        self.cutout = 10
        self.backup = 0
        self.Strategys = {}
        self.db = LightMysql()

    def get_days_before_today(self, n=0):
        '''
        date format = "YYYY-MM-DD HH:MM:SS"
        '''
        now = datetime.datetime.now()  
        if(n<0):  
            return datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)  
        else:  
            n_days_before = now - datetime.timedelta(days=n)  
        return datetime.datetime(n_days_before.year, n_days_before.month, n_days_before.day, n_days_before.hour, n_days_before.minute, n_days_before.second)
    

    def GetType(self, BallNo):
        type1 = "大"
        if int(BallNo) > 5:
            type1 = '大'
        else:
            type1 = '小'
        
        type2 = "单"        
        if int(BallNo) % 2 == 1:
            type2 = '单'
        else:
            type2 = '双'
        return [type1, type2]

    def log(self, type, issue, ballno, logtxt):
        for key in config_cptypes:
            if config_cptypes[key]["type"] == type:
                break;
        logformat = "%s  %s:%d %s"%(key, issue, ballno, logtxt)
        print(logformat)

    def delBallNo(self, road, ballno, config_cptype):
        Win = 0
        roads        = config_cptype["roads"]
        BALL_NO_DATA = config_cptype["BALL_NO_DATAS"][ballno]
        #处理中奖结果
        if BALL_NO_DATA["Temp_Rule"] != None:
            if  BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] in road[ballno - 1]:
                Win = 1
                BALL_NO_DATA["Temp_Win"]              = BALL_NO_DATA["Temp_Win"] + int(BALL_NO_DATA["Temp_Monery"][1])
                BALL_NO_DATA["Temp_Strategy_Win"]     = BALL_NO_DATA["Temp_Strategy_Win"] + int(BALL_NO_DATA["Temp_Monery"][1])
                BALL_NO_DATA["Temp_Cut"]              = BALL_NO_DATA["Temp_Cut"] + int(BALL_NO_DATA["Temp_Monery"][1])

                if BALL_NO_DATA["Temp_Cut_Flag"] == 1:
                    BALL_NO_DATA["Temp_CutIn"]              = BALL_NO_DATA["Temp_CutIn"] + int(BALL_NO_DATA["Temp_Monery"][1])
                    sql     = "update ssc_data_analyze set result = '中奖' where type = %d and expect='%s' and ballno = %d"%(config_cptype["type"], config_cptype["last_expect_issue"], ballno)
                    self.db.query(sql)

                self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***中奖***金额:" + BALL_NO_DATA["Temp_Monery"][1])

            else:
                Win = 0
                BALL_NO_DATA["Temp_Win"]              = BALL_NO_DATA["Temp_Win"] - int(BALL_NO_DATA["Temp_Monery"][1])
                BALL_NO_DATA["Temp_Strategy_Win"]     = BALL_NO_DATA["Temp_Strategy_Win"] - int(BALL_NO_DATA["Temp_Monery"][1])
                BALL_NO_DATA["Temp_Cut"]              = BALL_NO_DATA["Temp_Cut"] - int(BALL_NO_DATA["Temp_Monery"][1])
            
                if BALL_NO_DATA["Temp_Cut_Flag"] == 1:
                    BALL_NO_DATA["Temp_CutIn"]              = BALL_NO_DATA["Temp_CutIn"] - int(BALL_NO_DATA["Temp_Monery"][1])
                    sql     = "update ssc_data_analyze set result = '未中奖' where type = %d and expect='%s' and ballno = %d"%(config_cptype["type"], config_cptype["last_expect_issue"], ballno)
                    self.db.query(sql)

                self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***未中奖***")

            self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***当前输赢:" + str(BALL_NO_DATA["Temp_Win"]))
            self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***当前方案输赢:" + str(BALL_NO_DATA["Temp_Strategy_Win"]))
            self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***当前切入切出输赢:" + str(BALL_NO_DATA["Temp_Cut"]))
            self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***当前切入输赢:" + str(BALL_NO_DATA["Temp_CutIn"]))
        
            ##[1, 10, 2, 2]    
            for monery in BALL_NO_DATA["Temp_Strategy"]["monerys"]:
                if  Win == 1 and monery[0] == BALL_NO_DATA["Temp_Monery"][2]:
                    BALL_NO_DATA["Temp_Monery"] = monery
                    break
                elif  Win == 0 and monery[0] == BALL_NO_DATA["Temp_Monery"][3]:
                    BALL_NO_DATA["Temp_Monery"] = monery
                    break
            self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***当前方案输赢:" + str(BALL_NO_DATA["Temp_Strategy_Win"]))
            #Win = [1000, 1]    
            if BALL_NO_DATA["Temp_Strategy_Win"] > int(BALL_NO_DATA["Temp_Strategy"]["jumps"]["Win"][0]):
                BALL_NO_DATA["Temp_Strategy_Win"] = 0
                BALL_NO_DATA["Temp_Strategy"] = self.Strategys[int(BALL_NO_DATA["Temp_Strategy"]["jumps"]["Win"][1])]
                BALL_NO_DATA["Temp_Rule"]     = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0
                BALL_NO_DATA["Temp_Monery"]   = BALL_NO_DATA["Temp_Strategy"]["monerys"][0]

                self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***本方案累积赢跳转***" + str(BALL_NO_DATA["Temp_Strategy"]["Jump_idx"]))
                    
            #Faild = [1000, 1]    
            elif BALL_NO_DATA["Temp_Strategy_Win"] < -int(BALL_NO_DATA["Temp_Strategy"]["jumps"]["Faild"][0]):
                BALL_NO_DATA["Temp_Strategy_Win"] = 0
                BALL_NO_DATA["Temp_Strategy"] = self.Strategys[int(BALL_NO_DATA["Temp_Strategy"]["jumps"]["Faild"][1])]
                BALL_NO_DATA["Temp_Rule"]     = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0
                BALL_NO_DATA["Temp_Monery"]   = BALL_NO_DATA["Temp_Strategy"]["monerys"][0]
            
                self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***本方案累积输跳转***" + str(BALL_NO_DATA["Temp_Strategy"]["Jump_idx"]))

            #切入切出
            if BALL_NO_DATA["Temp_Cut"] > 0 and BALL_NO_DATA["Temp_Cut"] > self.cutout:
                self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***切出***" + str(BALL_NO_DATA["Temp_Cut"]))
                BALL_NO_DATA["Temp_Cut"] = 0
                BALL_NO_DATA["Temp_Cut_Flag"] = 0
            elif  BALL_NO_DATA["Temp_Cut"] < 0 and BALL_NO_DATA["Temp_Cut"] < -self.cutin:
                self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***切入***" + str(BALL_NO_DATA["Temp_Cut"]))
                BALL_NO_DATA["Temp_Cut"] = 0
                BALL_NO_DATA["Temp_Cut_Flag"] = 1

        else:
            self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***未下注***")

        #处理中奖结果

        if BALL_NO_DATA["Temp_Rule"] != None:
            BALL_NO_DATA["Temp_Rule_Idx"] = BALL_NO_DATA["Temp_Rule_Idx"] + 1
            if len(BALL_NO_DATA["Temp_Rule"][1]) <= BALL_NO_DATA["Temp_Rule_Idx"]:
                BALL_NO_DATA["Temp_Rule"] = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0

            #不回揽
            if self.backup == 0:
                self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***不回揽***")
                pass
            #中回揽
            elif self.backup == 1 and Win == 1:
                BALL_NO_DATA["Temp_Rule"] = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0
                self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***中回揽***")
            #错回揽
            elif self.backup == 2 and Win == 1:
                BALL_NO_DATA["Temp_Rule"] = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0
                self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***错回揽***")
       
        #处理路单规则
                         
        if BALL_NO_DATA["Temp_Rule"] == None:
            keys = sorted(roads)
            tmp  = ""
            for key in keys:
                tmp = tmp + str(roads[key][ballno - 1])

            self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***当前路单***" + tmp)

            for rule in BALL_NO_DATA["Temp_Strategy"]["rules"]:
                #[大大， 小小]
                rule0 = rule[0]
                self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***查找规则***" + rule0)
                len_keys  = len(keys)
                len_rule0 = len(rule0)
                isEqual   = False
                if len_keys >= len_rule0:
                    isEqual = True
                    start   = len_keys - len_rule0
                    for idx in range(0, len_rule0):
                        #[大， 双]
                        _isEqual = False
                        roadKey  = keys[start + idx]
                        for item in roads[roadKey][ballno - 1]:
                            if item == rule0[idx]:
                                _isEqual = True
                        if _isEqual == False:
                            isEqual = False
                            break
                if isEqual:
                    BALL_NO_DATA["Temp_Rule"]     = rule
                    BALL_NO_DATA["Temp_Rule_Idx"] = 0
                    self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***规则符合条件***" + str(rule[0]) + "=" + str(rule[1]))
                    break
                else:
                    self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***规则不符合条件***" + str(rule[0]) + "=" + str(rule[1]))  
                    pass 
        else: 
            self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***回揽未结束***")
            pass

        next_expect_issue = str(int(config_cptype["last_expect_issue"]) + 1)
        if BALL_NO_DATA["Temp_Rule"] != None:
            if BALL_NO_DATA["Temp_Cut_Flag"] == 1:
                self.log(config_cptype["type"], config_cptype["last_expect_issue"], ballno, "***购买:" + BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] + "金额：" + str(BALL_NO_DATA["Temp_Monery"][1]))

                sql     = "insert into ssc_data_analyze(type, expect, ballno, buy, monery, opentime) values(%d, '%s', %d, '%s', %s, now())"%(config_cptype["type"], next_expect_issue, ballno, BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]], str(BALL_NO_DATA["Temp_Monery"][1]))
                row_all = self.db.query(sql)
                return
        sql     = "insert into ssc_data_analyze(type, expect, ballno, buy, monery, opentime) values(%d, '%s', %d, '%s', 0, now())"%(config_cptype["type"], next_expect_issue, ballno, "不购买")
        row_all = self.db.query(sql)

    def autorun(self):
        print(self.Strategys) 
        last_run_date = ""
        while True:#无限循环
            time.sleep(1)
            run_date = datetime.datetime.now().strftime('%Y-%m-%d');
            if run_date != last_run_date:
                for config_cptype in config_cptypes.values():
                    config_cptype["last_expect_issue"] = ""
                    config_cptype["roads"] = {}
                    BALL_NO_DATAS = {}
                    for ballno in range(1, config_cptype["BallNum"] + 1):
                        BALL_NO_DATA = {}
                        BALL_NO_DATA["Temp_Strategy"]        =  self.Strategys[1]
                        BALL_NO_DATA["Temp_Monery"]          =  self.Strategys[1]["monerys"][0]
                        BALL_NO_DATA["Temp_Win"]             =  0
                        BALL_NO_DATA["Temp_Strategy_Win"]    =  0
                        BALL_NO_DATA["Temp_Rule"]            =  None
                        BALL_NO_DATA["Temp_Rule_Idx"]        =  0

                        BALL_NO_DATA["Temp_Cut"]             =  0
                        if self.cutin == 0:
                            BALL_NO_DATA["Temp_Cut_Flag"]    =  1
                        else:
                            BALL_NO_DATA["Temp_Cut_Flag"]    =  0
                        BALL_NO_DATA["Temp_CutIn"]           =  0
                        BALL_NO_DATAS[ballno]                 =  BALL_NO_DATA
                    config_cptype["BALL_NO_DATAS"] = BALL_NO_DATAS            
            last_run_date = run_date
            
            for cptype in config_cptypes:
                config_cptype = config_cptypes[cptype]
                sql     = "select type,expect,opencode,opentime  from  ssc_data where type = %d and TO_DAYS(opentime) = TO_DAYS('%s') and expect > '%s' ORDER BY expect LIMIT 1"%(config_cptype["type"], run_date, config_cptype["last_expect_issue"])
                row_all   = self.db.query(sql)
                if row_all == None or len(row_all) == 0:
                    print(cptype + "***等待开奖***")   
                    continue;
                row_1 = row_all[0]
                cur_expect_issue = row_1[1]

                print(cptype + "**********" + cur_expect_issue + "**************")   

                if config_cptype["last_expect_issue"] != "" and int(config_cptype["last_expect_issue"]) + 1 != int(cur_expect_issue):
                    print(cptype + "***等待开奖***")   
                    continue
                
                cur_expect_issue_Road = []      
                opencodes = row_1[2].split(",")
                for opencode in opencodes:
                    cur_expect_issue_Road.append(self.GetType(opencode))
            
            
                if config_cptype["BallNum"] != len(cur_expect_issue_Road):
                    print(cptype + "***数据还在加载中***")   
                    continue

                config_cptype["roads"][cur_expect_issue] = cur_expect_issue_Road
            
                config_cptype["last_expect_issue"] = cur_expect_issue

                for ballno in range(1, config_cptype["BallNum"] + 1):
                    self.delBallNo(cur_expect_issue_Road, int(ballno), config_cptype)    

    def Paser(self):
        Strategy = ""
        #生成config对象
        conf = configparser.ConfigParser()
        fp   = codecs.open("cpanalyze.txt", "r", "utf-8-sig")
        if not fp:
            raise "config file maybe not exist."
        else:
            conf.readfp(fp)          
        #用config对象读取配置文件
        #conf.read("cpanalyze.txt")
        
        if conf.has_section("Strategy") == True:
            Strategy = conf.get("Strategy", "value")
        else:
            return

        Jump_idx = 0
        self.Strategys = {}
        blocks = Strategy.split("==============================")
        for block in blocks:
            if block == "" or block == "\n":
                continue
            Strategy = {}
            inblocks = re.split('\n\n', block)
            for inblock in inblocks:
                if inblock == "" or block == "\n":
                    continue
                if "rules" not in Strategy:
                    rules = []
                    lines = inblock.split("\n")
                    if len(lines)==0:
                        return
                    for line in lines:
                        rule = re.split('=', line)
                        rules.append(rule) 
                    Strategy["rules"] = rules
                elif "monerys" not in Strategy:
                    monerys = []
                    lines = inblock.split("\n")
                    if len(lines)==0:
                        return
                    for line in lines:
                        monery = re.split('=',line)
                        monerys.append(monery) 
                    Strategy["monerys"] = monerys
                elif "jumps" not in Strategy:
                    Jumps = {}
                    #本方案累积赢[1000]元跳转到方案[1]
                    #本方案累积输[1000]元跳转到方案[1]
                    lines = inblock.split("\n")
                    if len(lines)==0:
                        return 
                    for line in lines:
                        searchObj  = re.search('^本方案累积赢\\[(\d+)\\]元跳转到方案\\[(\d+)\\]$',line)
                        if searchObj:
                            (a, b) = searchObj .groups()
                            Jumps["Win"] = [a, b]
                        searchObj  = re.search('^本方案累积输\\[(\d+)\\]元跳转到方案\\[(\d+)\\]$',line)
                        if searchObj:
                            (a, b) = searchObj .groups()
                            Jumps["Faild"] = [a, b]
                    Strategy["jumps"] = Jumps
            Jump_idx = Jump_idx + 1
            Strategy["Jump_idx"]     = Jump_idx
            self.Strategys[Jump_idx] = Strategy
        return True    


def main():
    cp = CPAnalyze()
    cp.Paser()
    cp.autorun()
    
if __name__ == "__main__":
    main()
