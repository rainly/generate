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

test_flag = False
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
        self.logprint("位置:" + self.target["buynos"])
        self.logprint("规则:" + str(self.target["rules"]))
        self.logprint("金额:" + str(self.target["monerys"]))
        
        buynos = self.target["buynos"].split(",")   
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

        if self.conf.has_section("rules") == True:
            self.m_rules.SetValue(self.conf.get("rules", "value"))     
        else:
            self.conf.add_section("rules")
            self.conf.set("rules", "value", "")
            
        if self.conf.has_section("monerys") == True:
            self.m_monerys.SetValue(self.conf.get("monerys", "value")) 
        else:
            self.conf.add_section("monerys")
            self.conf.set("monerys", "value", "")
            
        if self.conf.has_section("buynos") == True:
            self.m_buynos.SetValue(self.conf.get("buynos", "value"))     
        else:
            self.conf.add_section("buynos")
            self.conf.set("buynos", "value", "")
        
        self.type = 0
        self.m_radioBtn1.SetValue(True)
        
        self.lottery = 0
        self.m_radioBtn4.SetValue(True)
        
        if test_flag == False :
            self.webthread = WebdriverThread(self.m_url.GetValue())
            self.webthread.start()
        
    def OnRadio1( self, event ):
        #event.Skip()
        self.type = 0
    
    def OnRadio2( self, event ):
        #event.Skip()
        self.type = 1
        
    def OnRadio3( self, event ):
        #event.Skip()            
        self.type = 2
        
    def OnRadio4( self, event ):
        #event.Skip()
        self.lottery = 0
    
    def OnRadio5( self, event ):
        #event.Skip()
        self.lottery = 1
    
    def onEnter( self, event ):
        global driver
        driver.get(self.m_url.GetValue())        
        self.conf.set("url", "value", self.m_url.GetValue())
        #写回配置文件
        self.conf.write(open("hsgj19_2.ini","w"))                
                
    def onsave(self, event):  
        self.conf.set("rules", "value", self.m_rules.GetValue())
        self.conf.set("monerys", "value", self.m_monerys.GetValue())
        self.conf.set("buynos", "value", self.m_buynos.GetValue())
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
        
        if self.parse() == False:
            return
            
        target = {}
        target["buynos"]  = self.m_buynos.GetValue();
        target["rules"]   = self.rules
        target["monerys"] = self.monerys
        target["type"]    = self.type
        target["lottery"] = self.lottery
        
        self.m_button2.SetLabel('关闭')
        self.thread = BettingThread(target)
        self.thread.start()
        
    def parse(self):
        self.rules = []
        lines = self.m_rules.GetValue().split("\n")
        if len(lines)==0:
            return False
        for line in lines:
            rule = line.split(',')
            for no in rule:
                if no.isdigit() == False:
                    wx.MessageBox("购买规则配置出错(包含非数字类型)", caption="提示", style=wx.OK)
                    return False
                if (int(no) < 1) or (int(no) > 10):
                    wx.MessageBox("购买规则配置出错(数据异常)", caption="提示", style=wx.OK)
                    return False                    
            self.rules.append(rule)
            
        self.monerys = []
        lines = self.m_monerys.GetValue().split("\n")
        if len(lines)==0:
            return False
        for line in lines:
            monery = line.split('=')
            if len(monery) != 4:
                wx.MessageBox("购买金额规则配置出错", caption="提示", style=wx.OK)
                return False
            self.monerys.append(monery)
            
        
        return True
        
        
def main():
    app = wx.App()  
    main_win = MianWindow(None)  
    main_win.init_main_window()  
    main_win.Show()  
    app.MainLoop()  

if __name__ == "__main__":
    main()

