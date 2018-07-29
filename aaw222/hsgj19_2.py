# -*- coding: UTF-8 -*-    
import wx  
import basewin  
import sys   
import configparser
from selenium import webdriver
from selenium.common.exceptions import *
import threading  
import time
import datetime
import random
import logging
from logging import handlers
import operator

def isTrue(str):
     if str == "True":
          return True
     else:
          return False

def bool2str(data):
     if data == True:
          return "True"
     else:
          return "False"
     

class Logger(object):
    #日志级别关系映射
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }

    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        sh.setLevel(logging.DEBUG)
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        th.setLevel(logging.DEBUG)
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)
        
tf = datetime.datetime.now().strftime('%Y-%m-%d')    
log = Logger(tf + '.log',level='debug')


def logdebug(msg, *args, **kwargs):
    log.logger.debug(msg, *args, **kwargs)
    
def loginfo(msg, *args, **kwargs):
    log.logger.info(msg, *args, **kwargs)
    
def logwarning(msg, *args, **kwargs):
    log.logger.warning(msg, *args, **kwargs)
    
def logerror(msg, *args, **kwargs):
    kwargs["exc_info"] = 1
    log.logger.error(msg, *args, **kwargs)

def logcrit(msg, *args, **kwargs):
    kwargs["exc_info"] = 1
    log.logger.crit(msg, *args, **kwargs)

test_flag = True
driver    = None

class WebdriverThread(threading.Thread):
    def __init__(self, target, thread_num=0, timeout=5.0):
        super(WebdriverThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout
    def run(self):
        if test_flag == False:
            # 加启动配置
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            # 打开chrome浏览器
            global driver
            driver = webdriver.Chrome(chrome_options=option)
            driver.get(self.target)
        
    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped
        
    
class BettingThread(threading.Thread):
    def __init__(self, target, thread_num=0, timeout=5.0):
        super(BettingThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout
    def run(self):
        self.target_func()

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped
    
    def logprint(self, log):
        #tf = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #print(tf + "==>" + log)
        logdebug(log)
        
    def target_func(self):
        global driver
        self.logprint("********************start**************************")  
        self.logprint("********************start**************************")  
        self.logprint("********************start**************************")  

        
        buynos = []
		for i in range(12):
			if self.target["46" + str(i)] == True
				buynos.append(i + 1);

		
        BALL_NO_DATAS = {}
        for buyno in buynos:
            BALL_NO_DATA = {}
            BALL_NO_DATA["Temp_Monery_Idx"]      =  0
            BALL_NO_DATA["Temp_Rule_Idx"]        =  0
            BALL_NO_DATA["Temp_First_Flag"]      =  0
            BALL_NO_DATAS[buyno]                 =  BALL_NO_DATA
            
        Test_no = 1     
        SleepTime  = 5    
        Last_Award_Issue = ""        
        while self.stopped == False:
            try:
                SleepTime = SleepTime + 1
                if SleepTime < 5:
                    time.sleep(1)
                    continue
                SleepTime = 0  
                self.logprint("**********************************************")        
                #关闭温馨提示
                try:
                    driver.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
                except:
                    pass
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button").click()
                except:
                    pass   
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]").click()
                except:
                    pass
                
                if test_flag == False:
                    driver.switch_to.default_content()
                    #print("default current_url:" + driver.current_url)
                    #print("default title:" + driver.title)


                    main_frame = driver.find_element_by_xpath("//*[@id=\"main_frame\"]")
                    driver.switch_to.frame(main_frame)
                    print("//*[@id=\"main_frame\"] current_url:" +driver.current_url)
                    print("//*[@id=\"main_frame\"] title:" +driver.title)             
                    lt_gethistorycode = driver.find_element_by_xpath("//*[@id=\"lt_gethistorycode\"]").text
                    current_issue = driver.find_element_by_xpath("//*[@id=\"current_issue\"]").text
                else:
                    lt_gethistorycode  = str(Test_no) 
                    current_issue  = str(Test_no + 1)
                    Test_no = Test_no + 1

                #try:
                #driver.execute_script("document.getElementById('demo').style.display='none'")
                #except:
                #self.logprint("execute_script")
                #pass
                try:
                    driver.execute_script("var i;var box = document.getElementsByClassName('notice');for (i = 0; i < box.length; i++) {box[i].parentNode.removeChild(box[i]);}")
                except:
                    pass
                
                try:
                    driver.execute_script("function showTiShi(title,content,width,icon, callback){}")
                except:
                    pass
                
                self.logprint("开奖期号：" + lt_gethistorycode)
                self.logprint("购买期号：" + current_issue)
                if lt_gethistorycode == "" or current_issue == "":
                    self.logprint("***等待开奖1***关盘中")
                    continue
                #指定数据不差1，跳过
                if int(current_issue) != int(lt_gethistorycode) + 1:
                    self.logprint("***等待开奖2***期号未相关1")   
                    continue  

                if Last_Award_Issue != "" and int(Last_Award_Issue) == int(current_issue):
                    self.logprint("***等待开奖3***已下注")   
                    continue                    
                
                Award_Issue_Road = None
                try_time = 30
                while try_time > 0:   #无限循环
                    try_time = try_time - 1
                    self.logprint("****获取开奖数据***")   
                    Award_Issue_Road_t = []
                    if test_flag == False:
                        for idx  in range(1,6):
                            try:
                                BallText = driver.find_element_by_xpath("//*[@id=\"showcodebox\"]/span[" + str(idx) + "]").text
                                Award_Issue_Road_t.append(int(BallText))
                            except:
                                pass
                    else:
                        for idx  in range(1,6):
                            BallText = random.randint(1,10)
                            Award_Issue_Road_t.append(int(BallText))
                        Award_Issue_Road = Award_Issue_Road_t;
                    ####################################
                    print(Award_Issue_Road_t)
                    ####################################
                    if Award_Issue_Road == None and len(Award_Issue_Road_t) == 5:
                        Award_Issue_Road = Award_Issue_Road_t;
                    elif operator.eq(Award_Issue_Road, Award_Issue_Road_t):
                        break;
                    else:
                        Award_Issue_Road = Award_Issue_Road_t;
                        time.sleep(1)
                
                self.logprint("路单数据" + str(Award_Issue_Road))
                
                Last_Award_Issue = current_issue
                
                for buyno in buynos:
                    self.delBallNo(Award_Issue_Road, int(buyno), BALL_NO_DATAS[buyno])
                    time.sleep(1)
                #关闭温馨提示
                try:
                    driver.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
                except:
                    pass
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button").click()
                except:
                    pass   
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]").click()
                except:
                    pass    
                if test_flag == False:
                    driver.switch_to.parent_frame()
            
            except NoSuchElementException as msg:
                self.logprint("NoSuchElementException:%s" % msg)
                pass
            except WebDriverException as msg:
                self.logprint("WebDriverException:%s" % msg)
                pass
            except NoSuchWindowException as msg:
                self.logprint("NoSuchWindowException:%s" % msg)
                pass
            except NoSuchAttributeException as msg:
                self.logprint("NoSuchAttributeException:%s" % msg)
                pass
            except NoAlertPresentException as msg:
                self.logprint("NoAlertPresentException:%s" % msg)
                pass
            except ElementNotVisibleException as msg:
                self.logprint("ElementNotVisibleException:%s" % msg)
                pass
            except ElementNotSelectableException as msg:
                self.logprint("ElementNotSelectableException:%s" % msg)
                pass
            except TimeoutException as msg:
                self.logprint("TimeoutException:%s" % msg)
                pass
            except Exception as msg:
                self.logprint("Exception:%s" % msg)
                self.logprint("error lineno:" + str(sys._getframe().f_lineno))
                pass
            except:
                self.logprint("error lineno:" + str(sys._getframe().f_lineno))
                pass
        self.logprint("********************end**************************")  
        self.logprint("********************end**************************")  
        self.logprint("********************end**************************")      
    def delBallNo(self, road, buyno, BALL_NO_DATA):
        global driver
        self.logprint("**********************************************")   
        if BALL_NO_DATA["Temp_First_Flag"] == 1:
            self.logprint("位置" + str(buyno) + "***处理开奖规则序号***:" + str(BALL_NO_DATA["Temp_Rule_Idx"]) + 
            "***规则***:" +  str(self.target["rules"][BALL_NO_DATA["Temp_Rule_Idx"]]))
            self.logprint("位置" + str(buyno) + "***处理开奖金额序号***:" + str(BALL_NO_DATA["Temp_Monery_Idx"]) + 
            "***金额***:" + str(self.target["monerys"][BALL_NO_DATA["Temp_Monery_Idx"]][1]))
            
            Win = 0
            if str(road[buyno - 1]) in self.target["rules"][BALL_NO_DATA["Temp_Rule_Idx"]]:
                Win = 1;
                self.logprint("位置" + str(buyno) + "***中奖***金额:" + str(self.target["monerys"][BALL_NO_DATA["Temp_Monery_Idx"]][1]))
                BALL_NO_DATA["Temp_Monery_Idx"] = int(self.target["monerys"][BALL_NO_DATA["Temp_Monery_Idx"]][2]) - 1
                if self.target["type"] == 0:
                    #中不中都打下一个
                    BALL_NO_DATA["Temp_Rule_Idx"] = BALL_NO_DATA["Temp_Rule_Idx"] + 1
                    self.logprint("位置" + str(buyno) + "***中奖***中不中都打下一个")
                elif self.target["type"] == 1:
                    #中了一直打同一个
                    self.logprint("位置" + str(buyno) + "***中奖***中了一直打同一个")
                    pass
                elif self.target["type"] == 2:
                    #中了回第一个
                    BALL_NO_DATA["Temp_Rule_Idx"] = 0
                    self.logprint("位置" + str(buyno) + "***中奖***中了回第一个")
                else:
                    BALL_NO_DATA["Temp_Rule_Idx"] = 0
                    self.logprint("位置" + str(buyno) + "***中奖***中了回第一个")
            else:
                Win = 0;
                self.logprint("位置" + str(buyno) + "***未中奖***")
                BALL_NO_DATA["Temp_Monery_Idx"] = int(self.target["monerys"][BALL_NO_DATA["Temp_Monery_Idx"]][3]) - 1
                BALL_NO_DATA["Temp_Rule_Idx"] = BALL_NO_DATA["Temp_Rule_Idx"] + 1
            
            if BALL_NO_DATA["Temp_Rule_Idx"] >= len(self.target["rules"]):
                BALL_NO_DATA["Temp_Rule_Idx"] = 0
        else:
            BALL_NO_DATA["Temp_First_Flag"] = 1
            BALL_NO_DATA["Temp_Rule_Idx"]   = 0
            BALL_NO_DATA["Temp_Monery_Idx"] = 0

        self.logprint("位置" + str(buyno) + "***购买规则序号***:" + str(BALL_NO_DATA["Temp_Rule_Idx"]) + "***规则***:" + str(self.target["rules"][BALL_NO_DATA["Temp_Rule_Idx"]]))
        self.logprint("位置" + str(buyno) + "***购买金额序号***:" + str(BALL_NO_DATA["Temp_Monery_Idx"]) + "***金额***:" + str(self.target["monerys"][BALL_NO_DATA["Temp_Monery_Idx"]][1]))
        
        Bet = False        
        if test_flag == False :
            Bet = True       
            try_time = 10                        
            while try_time > 0:   #无限循环
                #关闭温馨提示
                try:
                    driver.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
                except:
                    pass
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button").click()
                except:
                    pass
                try:
                    try_time = try_time - 1
                    if self.target["lottery"] == 0:
                        for no in self.target["rules"][BALL_NO_DATA["Temp_Rule_Idx"]]:
                            #print(no)
                            if buyno == 1:
                                driver.find_element_by_xpath("//*[@id=\"num_group_ww\"]/div[2]/div[" + str(int(no) + 1) + "]").click()
                            elif buyno == 2:
                                driver.find_element_by_xpath("//*[@id=\"num_group_qw\"]/div[2]/div[" + str(int(no) + 1) + "]").click()
                            elif buyno == 3:
                                driver.find_element_by_xpath("//*[@id=\"num_group_bw\"]/div[2]/div[" + str(int(no) + 1) + "]").click()
                            elif buyno == 4:
                                driver.find_element_by_xpath("//*[@id=\"num_group_sw\"]/div[2]/div[" + str(int(no) + 1) + "]").click()
                            elif buyno == 5:
                                driver.find_element_by_xpath("//*[@id=\"num_group_ge\"]/div[2]/div[" + str(int(no) + 1) + "]").click()
                            else:
                                pass
                        #print("ZZZZZZZZZZZZZZZZZZZZZZZZZZ")
                        driver.find_element_by_xpath("//*[@id=\"lt_sel_times\"]").clear()
                        driver.find_element_by_xpath("//*[@id=\"lt_sel_times\"]").send_keys(str(self.target["monerys"][BALL_NO_DATA["Temp_Monery_Idx"]][1]))  
                        driver.find_element_by_xpath("//*[@id=\"lt_buy_now\"]").click()
                        time.sleep(1)        
                        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]").click()
                        time.sleep(1)
                        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
                    elif self.target["lottery"] == 1:
                        for no in self.target["rules"][BALL_NO_DATA["Temp_Rule_Idx"]]:
                            #print(no)
                            if buyno == 1:
                                driver.find_element_by_xpath("//*[@id=\"num_group_ww\"]/div[2]/div[" + str(int(no) + 1) + "]").click()
                            elif buyno == 2:
                                driver.find_element_by_xpath("//*[@id=\"num_group_qw\"]/div[2]/div[" + str(int(no) + 1) + "]").click()
                            elif buyno == 3:
                                driver.find_element_by_xpath("//*[@id=\"num_group_bw\"]/div[2]/div[" + str(int(no) + 1) + "]").click()
                            elif buyno == 4:
                                driver.find_element_by_xpath("//*[@id=\"num_group_sw\"]/div[2]/div[" + str(int(no) + 1) + "]").click()
                            elif buyno == 5:
                                driver.find_element_by_xpath("//*[@id=\"num_group_ge\"]/div[2]/div[" + str(int(no) + 1) + "]").click()
                            else:
                                pass
                        #print("ZZZZZZZZZZZZZZZZZZZZZZZZZZ")
                        driver.find_element_by_xpath("//*[@id=\"lt_sel_times\"]").clear()
                        driver.find_element_by_xpath("//*[@id=\"lt_sel_times\"]").send_keys(str(self.target["monerys"][BALL_NO_DATA["Temp_Monery_Idx"]][1]))  
                        driver.find_element_by_xpath("//*[@id=\"lt_buy_now\"]").click()
                        time.sleep(1)        
                        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]").click()
                        time.sleep(1)
                        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
                except Exception as msg:
                    self.logprint("Exception:%s" % msg)
                    time.sleep(1)
                    continue
                    pass
                except:
                    self.logprint("位置" + str(buyno) + "***报错***重试：" + str(try_time))
                    time.sleep(1)
                    continue
                if try_time == 0:
                    self.logprint("位置" + str(buyno) + "***报错***下注失败")
                break
                
        return Bet
    
##################################################################
##################################################################
##################################################################                
##################################################################
class MianWindow(basewin.BaseMainWind):  
    # 首先，咱们从刚刚源文件中将主窗体继承下来.就是修改过name属性的主窗体咯。  
    def init_main_window(self):  
        self.thread = None
        #生成config对象
        self.conf = configparser.ConfigParser()
        #用config对象读取配置文件
        self.conf.read("hsgj19_2.ini")


        if self.conf.has_section("url") == True:
            self.m_url.SetValue(self.conf.get("url", "value"))     
        else:
            self.conf.add_section("url")
            self.conf.set("url", "value", "https://www.hsgj19.com/")
            self.m_url.SetValue("https://www.hsgj19.com/")     
          
        ##################################################
        if self.conf.has_section("420") == True:
            self.m_comboBox420.SetValue(self.conf.get("420", "value"))
        else:
            self.conf.add_section("420")
            self.conf.set("420", "value", "大")
        #
        if self.conf.has_section("430") == True:
            self.m_textCtrl430.SetValue(self.conf.get("430", "value"))
        else:
            self.conf.add_section("430")
            self.conf.set("430", "value", "10") 
        #
        if self.conf.has_section("440") == True:
            self.m_textCtrl440.SetValue(self.conf.get("440", "value"))
        else:
            self.conf.add_section("440")
            self.conf.set("440", "value", "10") 
        #
        if self.conf.has_section("450") == True:
            self.m_textCtrl450.SetValue(self.conf.get("450", "value"))
        else:
            self.conf.add_section("450")
            self.conf.set("450", "value", "10")
        #
        if self.conf.has_section("460") == True:
            self.m_checkBox460.SetValue(isTrue(self.conf.get("460", "value")))
        else:
            self.conf.add_section("460")
            self.conf.set("460", "value", "True")
        ##################################################
        ##################################################
        if self.conf.has_section("421") == True:
            self.m_comboBox421.SetValue(self.conf.get("421", "value"))
        else:
            self.conf.add_section("421")
            self.conf.set("421", "value", "大")
        #
        if self.conf.has_section("431") == True:
            self.m_textCtrl431.SetValue(self.conf.get("431", "value"))
        else:
            self.conf.add_section("431")
            self.conf.set("431", "value", "10") 
        #
        if self.conf.has_section("441") == True:
            self.m_textCtrl441.SetValue(self.conf.get("441", "value"))
        else:
            self.conf.add_section("441")
            self.conf.set("441", "value", "11") 
        #
        if self.conf.has_section("451") == True:
            self.m_textCtrl451.SetValue(self.conf.get("451", "value"))
        else:
            self.conf.add_section("451")
            self.conf.set("451", "value", "10")
        #
        if self.conf.has_section("461") == True:
            self.m_checkBox461.SetValue(isTrue(self.conf.get("461", "value")))
        else:
            self.conf.add_section("461")
            self.conf.set("461", "value", "True")
        ##################################################
        ##################################################
        if self.conf.has_section("422") == True:
            self.m_comboBox422.SetValue(self.conf.get("422", "value"))
        else:
            self.conf.add_section("422")
            self.conf.set("422", "value", "大")
        #
        if self.conf.has_section("432") == True:
            self.m_textCtrl432.SetValue(self.conf.get("432", "value"))
        else:
            self.conf.add_section("432")
            self.conf.set("432", "value", "10") 
        #
        if self.conf.has_section("442") == True:
            self.m_textCtrl442.SetValue(self.conf.get("442", "value"))
        else:
            self.conf.add_section("442")
            self.conf.set("442", "value", "12") 
        #
        if self.conf.has_section("452") == True:
            self.m_textCtrl452.SetValue(self.conf.get("452", "value"))
        else:
            self.conf.add_section("452")
            self.conf.set("452", "value", "10")
        #
        if self.conf.has_section("462") == True:
            self.m_checkBox462.SetValue(isTrue(self.conf.get("462", "value")))
        else:
            self.conf.add_section("462")
            self.conf.set("462", "value", "True")
        ##################################################
        ##################################################
        if self.conf.has_section("423") == True:
            self.m_comboBox423.SetValue(self.conf.get("423", "value"))
        else:
            self.conf.add_section("423")
            self.conf.set("423", "value", "大")
        #
        if self.conf.has_section("433") == True:
            self.m_textCtrl433.SetValue(self.conf.get("433", "value"))
        else:
            self.conf.add_section("433")
            self.conf.set("433", "value", "10") 
        #
        if self.conf.has_section("443") == True:
            self.m_textCtrl443.SetValue(self.conf.get("443", "value"))
        else:
            self.conf.add_section("443")
            self.conf.set("443", "value", "13") 
        #
        if self.conf.has_section("453") == True:
            self.m_textCtrl453.SetValue(self.conf.get("453", "value"))
        else:
            self.conf.add_section("453")
            self.conf.set("453", "value", "10")
        #
        if self.conf.has_section("463") == True:
            self.m_checkBox463.SetValue(isTrue(self.conf.get("463", "value")))
        else:
            self.conf.add_section("463")
            self.conf.set("463", "value", "True")
        ##################################################
        ##################################################
        if self.conf.has_section("424") == True:
            self.m_comboBox424.SetValue(self.conf.get("424", "value"))
        else:
            self.conf.add_section("424")
            self.conf.set("424", "value", "大")
        #
        if self.conf.has_section("434") == True:
            self.m_textCtrl434.SetValue(self.conf.get("434", "value"))
        else:
            self.conf.add_section("434")
            self.conf.set("434", "value", "10") 
        #
        if self.conf.has_section("444") == True:
            self.m_textCtrl444.SetValue(self.conf.get("444", "value"))
        else:
            self.conf.add_section("444")
            self.conf.set("444", "value", "14") 
        #
        if self.conf.has_section("454") == True:
            self.m_textCtrl454.SetValue(self.conf.get("454", "value"))
        else:
            self.conf.add_section("454")
            self.conf.set("454", "value", "10")
        #
        if self.conf.has_section("464") == True:
            self.m_checkBox464.SetValue(isTrue(self.conf.get("464", "value")))
        else:
            self.conf.add_section("464")
            self.conf.set("464", "value", "True")
        ##################################################
        ##################################################
        if self.conf.has_section("425") == True:
            self.m_comboBox425.SetValue(self.conf.get("425", "value"))
        else:
            self.conf.add_section("425")
            self.conf.set("425", "value", "大")
        #
        if self.conf.has_section("435") == True:
            self.m_textCtrl435.SetValue(self.conf.get("435", "value"))
        else:
            self.conf.add_section("435")
            self.conf.set("435", "value", "10") 
        #
        if self.conf.has_section("445") == True:
            self.m_textCtrl445.SetValue(self.conf.get("445", "value"))
        else:
            self.conf.add_section("445")
            self.conf.set("445", "value", "15") 
        #
        if self.conf.has_section("455") == True:
            self.m_textCtrl455.SetValue(self.conf.get("455", "value"))
        else:
            self.conf.add_section("455")
            self.conf.set("455", "value", "10")
        #
        if self.conf.has_section("465") == True:
            self.m_checkBox465.SetValue(isTrue(self.conf.get("465", "value")))
        else:
            self.conf.add_section("465")
            self.conf.set("465", "value", "True")
        ##################################################
        ##################################################
        if self.conf.has_section("426") == True:
            self.m_comboBox426.SetValue(self.conf.get("426", "value"))
        else:
            self.conf.add_section("426")
            self.conf.set("426", "value", "大")
        #
        if self.conf.has_section("436") == True:
            self.m_textCtrl436.SetValue(self.conf.get("436", "value"))
        else:
            self.conf.add_section("436")
            self.conf.set("436", "value", "10") 
        #
        if self.conf.has_section("446") == True:
            self.m_textCtrl446.SetValue(self.conf.get("446", "value"))
        else:
            self.conf.add_section("446")
            self.conf.set("446", "value", "16") 
        #
        if self.conf.has_section("456") == True:
            self.m_textCtrl456.SetValue(self.conf.get("456", "value"))
        else:
            self.conf.add_section("456")
            self.conf.set("456", "value", "10")
        #
        if self.conf.has_section("466") == True:
            self.m_checkBox466.SetValue(isTrue(self.conf.get("466", "value")))
        else:
            self.conf.add_section("466")
            self.conf.set("466", "value", "True")
        ##################################################
        ##################################################
        if self.conf.has_section("427") == True:
            self.m_comboBox427.SetValue(self.conf.get("427", "value"))
        else:
            self.conf.add_section("427")
            self.conf.set("427", "value", "大")
        #
        if self.conf.has_section("437") == True:
            self.m_textCtrl437.SetValue(self.conf.get("437", "value"))
        else:
            self.conf.add_section("437")
            self.conf.set("437", "value", "10") 
        #
        if self.conf.has_section("447") == True:
            self.m_textCtrl447.SetValue(self.conf.get("447", "value"))
        else:
            self.conf.add_section("447")
            self.conf.set("447", "value", "17") 
        #
        if self.conf.has_section("457") == True:
            self.m_textCtrl457.SetValue(self.conf.get("457", "value"))
        else:
            self.conf.add_section("457")
            self.conf.set("457", "value", "10")
        #
        if self.conf.has_section("467") == True:
            self.m_checkBox467.SetValue(isTrue(self.conf.get("467", "value")))
        else:
            self.conf.add_section("467")
            self.conf.set("467", "value", "True")
        ##################################################
        ##################################################
        if self.conf.has_section("428") == True:
            self.m_comboBox428.SetValue(self.conf.get("428", "value"))
        else:
            self.conf.add_section("428")
            self.conf.set("428", "value", "大")
        #
        if self.conf.has_section("438") == True:
            self.m_textCtrl438.SetValue(self.conf.get("438", "value"))
        else:
            self.conf.add_section("438")
            self.conf.set("438", "value", "10") 
        #
        if self.conf.has_section("448") == True:
            self.m_textCtrl448.SetValue(self.conf.get("448", "value"))
        else:
            self.conf.add_section("448")
            self.conf.set("448", "value", "18") 
        #
        if self.conf.has_section("458") == True:
            self.m_textCtrl458.SetValue(self.conf.get("458", "value"))
        else:
            self.conf.add_section("458")
            self.conf.set("458", "value", "10")
        #
        if self.conf.has_section("468") == True:
            self.m_checkBox468.SetValue(isTrue(self.conf.get("468", "value")))
        else:
            self.conf.add_section("468")
            self.conf.set("468", "value", "True")
        ##################################################
        ##################################################
        if self.conf.has_section("429") == True:
            self.m_comboBox429.SetValue(self.conf.get("429", "value"))
        else:
            self.conf.add_section("429")
            self.conf.set("429", "value", "大")
        #
        if self.conf.has_section("439") == True:
            self.m_textCtrl439.SetValue(self.conf.get("439", "value"))
        else:
            self.conf.add_section("439")
            self.conf.set("439", "value", "10") 
        #
        if self.conf.has_section("449") == True:
            self.m_textCtrl449.SetValue(self.conf.get("449", "value"))
        else:
            self.conf.add_section("449")
            self.conf.set("449", "value", "19") 
        #
        if self.conf.has_section("459") == True:
            self.m_textCtrl459.SetValue(self.conf.get("459", "value"))
        else:
            self.conf.add_section("459")
            self.conf.set("459", "value", "10")
        #
        if self.conf.has_section("469") == True:
            self.m_checkBox469.SetValue(isTrue(self.conf.get("469", "value")))
        else:
            self.conf.add_section("469")
            self.conf.set("469", "value", "True")
        ##################################################
        ##################################################
        if self.conf.has_section("4210") == True:
            self.m_comboBox4210.SetValue(self.conf.get("4210", "value"))
        else:
            self.conf.add_section("4210")
            self.conf.set("4210", "value", "大")
        #
        if self.conf.has_section("4310") == True:
            self.m_textCtrl4310.SetValue(self.conf.get("4310", "value"))
        else:
            self.conf.add_section("4310")
            self.conf.set("4310", "value", "10") 
        #
        if self.conf.has_section("4410") == True:
            self.m_textCtrl4410.SetValue(self.conf.get("4410", "value"))
        else:
            self.conf.add_section("4410")
            self.conf.set("4410", "value", "110") 
        #
        if self.conf.has_section("4510") == True:
            self.m_textCtrl4510.SetValue(self.conf.get("4510", "value"))
        else:
            self.conf.add_section("4510")
            self.conf.set("4510", "value", "10")
        #
        if self.conf.has_section("4610") == True:
            self.m_checkBox4610.SetValue(isTrue(self.conf.get("4610", "value")))
        else:
            self.conf.add_section("4610")
            self.conf.set("4610", "value", "True")
        ##################################################
        ##################################################
        if self.conf.has_section("4211") == True:
            self.m_comboBox4211.SetValue(self.conf.get("4211", "value"))
        else:
            self.conf.add_section("4211")
            self.conf.set("4211", "value", "大")
        #
        if self.conf.has_section("4311") == True:
            self.m_textCtrl4311.SetValue(self.conf.get("4311", "value"))
        else:
            self.conf.add_section("4311")
            self.conf.set("4311", "value", "10") 
        #
        if self.conf.has_section("4411") == True:
            self.m_textCtrl4411.SetValue(self.conf.get("4411", "value"))
        else:
            self.conf.add_section("4411")
            self.conf.set("4411", "value", "111") 
        #
        if self.conf.has_section("4511") == True:
            self.m_textCtrl4511.SetValue(self.conf.get("4511", "value"))
        else:
            self.conf.add_section("4511")
            self.conf.set("4511", "value", "10")
        #
        if self.conf.has_section("4611") == True:
            self.m_checkBox4611.SetValue(isTrue(self.conf.get("4611", "value")))
        else:
            self.conf.add_section("4611")
            self.conf.set("4611", "value", "True")
        ##################################################
            
        #写回配置文件
        self.conf.write(open("hsgj19_2.ini","w"))                   
        if test_flag == False :
            self.webthread = WebdriverThread(self.m_url.GetValue())
            self.webthread.start()
        
    def onEnter( self, event ):
        global driver
        driver.get(self.m_url.GetValue())        
        self.conf.set("url", "value", self.m_url.GetValue())
        #写回配置文件
        self.conf.write(open("hsgj19_2.ini","w"))                
                
    def onsave(self, event):  
        ##################################################
        self.conf.set("420", "value", self.m_comboBox420.GetValue())
        self.conf.set("430", "value", self.m_textCtrl430.GetValue())
        self.conf.set("440", "value", self.m_textCtrl440.GetValue())
        self.conf.set("450", "value", self.m_textCtrl450.GetValue())
        self.conf.set("460", "value", bool2str(self.m_checkBox460.GetValue()))
        ##################################################
        self.conf.set("421", "value", self.m_comboBox421.GetValue())
        self.conf.set("431", "value", self.m_textCtrl431.GetValue())
        self.conf.set("441", "value", self.m_textCtrl441.GetValue())
        self.conf.set("451", "value", self.m_textCtrl451.GetValue())
        self.conf.set("461", "value", bool2str(self.m_checkBox461.GetValue()))
        ##################################################
        self.conf.set("422", "value", self.m_comboBox422.GetValue())
        self.conf.set("432", "value", self.m_textCtrl432.GetValue())
        self.conf.set("442", "value", self.m_textCtrl442.GetValue())
        self.conf.set("452", "value", self.m_textCtrl452.GetValue())
        self.conf.set("462", "value", bool2str(self.m_checkBox462.GetValue()))
        ##################################################
        self.conf.set("423", "value", self.m_comboBox423.GetValue())
        self.conf.set("433", "value", self.m_textCtrl433.GetValue())
        self.conf.set("443", "value", self.m_textCtrl443.GetValue())
        self.conf.set("453", "value", self.m_textCtrl453.GetValue())
        self.conf.set("463", "value", bool2str(self.m_checkBox463.GetValue()))
        ##################################################
        self.conf.set("424", "value", self.m_comboBox424.GetValue())
        self.conf.set("434", "value", self.m_textCtrl434.GetValue())
        self.conf.set("444", "value", self.m_textCtrl444.GetValue())
        self.conf.set("454", "value", self.m_textCtrl454.GetValue())
        self.conf.set("464", "value", bool2str(self.m_checkBox464.GetValue()))
        ##################################################
        self.conf.set("425", "value", self.m_comboBox425.GetValue())
        self.conf.set("435", "value", self.m_textCtrl435.GetValue())
        self.conf.set("445", "value", self.m_textCtrl445.GetValue())
        self.conf.set("455", "value", self.m_textCtrl455.GetValue())
        self.conf.set("465", "value", bool2str(self.m_checkBox465.GetValue()))
        ##################################################
        self.conf.set("426", "value", self.m_comboBox426.GetValue())
        self.conf.set("436", "value", self.m_textCtrl436.GetValue())
        self.conf.set("446", "value", self.m_textCtrl446.GetValue())
        self.conf.set("456", "value", self.m_textCtrl456.GetValue())
        self.conf.set("466", "value", bool2str(self.m_checkBox466.GetValue()))
        ##################################################
        self.conf.set("427", "value", self.m_comboBox427.GetValue())
        self.conf.set("437", "value", self.m_textCtrl437.GetValue())
        self.conf.set("447", "value", self.m_textCtrl447.GetValue())
        self.conf.set("457", "value", self.m_textCtrl457.GetValue())
        self.conf.set("467", "value", bool2str(self.m_checkBox467.GetValue()))
        ##################################################
        self.conf.set("428", "value", self.m_comboBox428.GetValue())
        self.conf.set("438", "value", self.m_textCtrl438.GetValue())
        self.conf.set("448", "value", self.m_textCtrl448.GetValue())
        self.conf.set("458", "value", self.m_textCtrl458.GetValue())
        self.conf.set("468", "value", bool2str(self.m_checkBox468.GetValue()))
        ##################################################
        self.conf.set("429", "value", self.m_comboBox429.GetValue())
        self.conf.set("439", "value", self.m_textCtrl439.GetValue())
        self.conf.set("449", "value", self.m_textCtrl449.GetValue())
        self.conf.set("459", "value", self.m_textCtrl459.GetValue())
        self.conf.set("469", "value", bool2str(self.m_checkBox469.GetValue()))
        ##################################################
        self.conf.set("4210", "value", self.m_comboBox4210.GetValue())
        self.conf.set("4310", "value", self.m_textCtrl4310.GetValue())
        self.conf.set("4410", "value", self.m_textCtrl4410.GetValue())
        self.conf.set("4510", "value", self.m_textCtrl4510.GetValue())
        self.conf.set("4610", "value", bool2str(self.m_checkBox4610.GetValue()))
        ##################################################
        self.conf.set("4211", "value", self.m_comboBox4211.GetValue())
        self.conf.set("4311", "value", self.m_textCtrl4311.GetValue())
        self.conf.set("4411", "value", self.m_textCtrl4411.GetValue())
        self.conf.set("4511", "value", self.m_textCtrl4511.GetValue())
        self.conf.set("4611", "value", bool2str(self.m_checkBox4611.GetValue()))
        #写回配置文件
        self.conf.write(open("hsgj19_2.ini","w"))
        
    def onstart(self, event):  
        self.onsave(event)
        
        if  self.thread != None:
            self.m_button2.SetLabel('开始')
            if self.thread.is_alive():
                self.thread.stop()
            self.thread.join()
            self.thread = None
            return    
            
        target = {}
        ##################################################
        target["420"] = self.m_comboBox420.GetValue()
        target["430"] = self.m_textCtrl430.GetValue()
        target["440"] = self.m_textCtrl440.GetValue()
        target["450"] = self.m_textCtrl450.GetValue()
        target["460"] = self.m_checkBox460.GetValue()
        ##################################################
        target["421"] = self.m_comboBox421.GetValue()
        target["431"] = self.m_textCtrl431.GetValue()
        target["441"] = self.m_textCtrl441.GetValue()
        target["451"] = self.m_textCtrl451.GetValue()
        target["461"] = self.m_checkBox461.GetValue()
        ##################################################
        target["422"] = self.m_comboBox422.GetValue()
        target["432"] = self.m_textCtrl432.GetValue()
        target["442"] = self.m_textCtrl442.GetValue()
        target["452"] = self.m_textCtrl452.GetValue()
        target["462"] = self.m_checkBox462.GetValue()
        ##################################################
        target["423"] = self.m_comboBox423.GetValue()
        target["433"] = self.m_textCtrl433.GetValue()
        target["443"] = self.m_textCtrl443.GetValue()
        target["453"] = self.m_textCtrl453.GetValue()
        target["463"] = self.m_checkBox463.GetValue()
        ##################################################
        target["424"] = self.m_comboBox424.GetValue()
        target["434"] = self.m_textCtrl434.GetValue()
        target["444"] = self.m_textCtrl444.GetValue()
        target["454"] = self.m_textCtrl454.GetValue()
        target["464"] = self.m_checkBox464.GetValue()
        ##################################################
        target["425"] = self.m_comboBox425.GetValue()
        target["435"] = self.m_textCtrl435.GetValue()
        target["445"] = self.m_textCtrl445.GetValue()
        target["455"] = self.m_textCtrl455.GetValue()
        target["465"] = self.m_checkBox465.GetValue()
        ##################################################
        target["426"] = self.m_comboBox426.GetValue()
        target["436"] = self.m_textCtrl436.GetValue()
        target["446"] = self.m_textCtrl446.GetValue()
        target["456"] = self.m_textCtrl456.GetValue()
        target["466"] = self.m_checkBox466.GetValue()
        ##################################################
        target["427"] = self.m_comboBox427.GetValue()
        target["437"] = self.m_textCtrl437.GetValue()
        target["447"] = self.m_textCtrl447.GetValue()
        target["457"] = self.m_textCtrl457.GetValue()
        target["467"] = self.m_checkBox467.GetValue()
        ##################################################
        target["428"] = self.m_comboBox428.GetValue()
        target["438"] = self.m_textCtrl438.GetValue()
        target["448"] = self.m_textCtrl448.GetValue()
        target["458"] = self.m_textCtrl458.GetValue()
        target["468"] = self.m_checkBox468.GetValue()
        ##################################################
        target["429"] = self.m_comboBox429.GetValue()
        target["439"] = self.m_textCtrl439.GetValue()
        target["449"] = self.m_textCtrl449.GetValue()
        target["459"] = self.m_textCtrl459.GetValue()
        target["469"] = self.m_checkBox469.GetValue()
        ##################################################
        target["4210"] = self.m_comboBox4210.GetValue()
        target["4310"] = self.m_textCtrl4310.GetValue()
        target["4410"] = self.m_textCtrl4410.GetValue()
        target["4510"] = self.m_textCtrl4510.GetValue()
        target["4610"] = self.m_checkBox4610.GetValue()
        ##################################################
        target["4211"] = self.m_comboBox4211.GetValue()
        target["4311"] = self.m_textCtrl4311.GetValue()
        target["4411"] = self.m_textCtrl4411.GetValue()
        target["4511"] = self.m_textCtrl4511.GetValue()
        target["4611"] = self.m_checkBox4611.GetValue()
        
        self.m_button2.SetLabel('关闭')
        self.thread = BettingThread(target)
        self.thread.start()
        
        
def main():
    app = wx.App()  
    main_win = MianWindow(None)  
    main_win.init_main_window()  
    main_win.Show()  
    app.MainLoop()  

if __name__ == "__main__":
    main()

