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
if test_flag == False:
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)


    
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
        #print("**********target_func begin***********")
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
        '''
        if test_flag == False:
            driver.implicitly_wait(5)           
            while self.stopped == False:
                #print("**********find title***********")
                try:
                    if driver.title == "新海运 v5.1.2":
                        break
                    time.sleep(5)
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
                    pass
                except:
                    self.logprint("error lineno:" + str(sys._getframe().f_lineno))
                    pass
        '''    
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

                if test_flag == False:
                    driver.switch_to.default_content()
                    #print("default current_url:" + driver.current_url)
                    #print("default title:" + driver.title)


                    ifr_Index = driver.find_element_by_xpath("//*[@id=\"ifr_Index\"]")
                    driver.switch_to.frame(ifr_Index)
                    #print("//*[@id=\"ifr_Index\"] current_url:" +driver.current_url)
                    #print("//*[@id=\"ifr_Index\"] title:" +driver.title)
                    mainFrame = driver.find_element_by_xpath("/html/frameset/frameset/frame[2]")
                    
                    #/html/frameset
                    #    //*[@id="topFrame"]
                    #    /html/frameset/frameset
                    #        //*[@id="leftFrame"]
                    #        //*[@id="mainFrame"]    
                    driver.switch_to.frame(mainFrame)
                    #print("/html/frameset/frameset/frame[2] current_url:" + driver.current_url)
                    #print("/html/frameset/frameset/frame[2] title:" + driver.title)                
                    Cur_Award_Issue1 = driver.find_element_by_xpath("//*[@id=\"UP_LID\"]").text
                    Cur_Award_Issue2 = driver.find_element_by_xpath("//*[@id=\"k_qs\"]").text
                    ##用于保证数据可以下注
                    if self.target["lottery"] == 0:
                        driver.find_element_by_xpath("//*[@id=\"jeuM_0_40000\"]")
                    elif self.target["lottery"] == 1:
                        driver.find_element_by_xpath("//*[@id=\"jeuM_0_80000\"]")
                    else:
                        pass
                else:
                    Cur_Award_Issue1  = str(Test_no) 
                    Cur_Award_Issue2  = str(Test_no + 1)
                    Test_no = Test_no + 1
                    
                self.logprint("开奖期号：" + Cur_Award_Issue1)
                self.logprint("购买期号：" + Cur_Award_Issue2)
                if Cur_Award_Issue1 == "" or Cur_Award_Issue2 == "":
                    self.logprint("***等待开奖1***关盘中")
                    continue
                #指定数据不差1，跳过
                if int(Cur_Award_Issue2) != int(Cur_Award_Issue1) + 1:
                    self.logprint("***等待开奖2***期号未相关1")   
                    continue  

                if Last_Award_Issue != "" and int(Last_Award_Issue) == int(Cur_Award_Issue2):
                    self.logprint("***等待开奖3***已下注")   
                    continue                    
                
                Award_Issue_Road = []                    
                if test_flag == False:
                    for idx  in range(1,11):
                        BallText = driver.find_element_by_xpath("//*[@id=\"d_GameLottery\"]/table/tbody/tr/td[" + str(idx + 1) + "]").get_attribute("class").replace("No_", "")
                        Award_Issue_Road.append(int(BallText))
                else:
                    for idx  in range(1,11):
                        BallText = random.randint(1,10)
                        Award_Issue_Road.append(int(BallText))
                
                self.logprint("路单数据" + str(Award_Issue_Road))
                
                Last_Award_Issue = Cur_Award_Issue2
                
                for buyno in buynos:
                    self.delBallNo(Award_Issue_Road, int(buyno), BALL_NO_DATAS[buyno])
                    time.sleep(1)
                
                if test_flag == False:
                    driver.find_element_by_xpath("//*[@id=\"confirm\"]").click()
                    time.sleep(1)    
                    driver.find_element_by_xpath("//*[@id=\"_ButtonOK_div_order\"]").click()
                    time.sleep(1)
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
    
    def delBallNo(self, road, buyno, BALL_NO_DATA):
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

        if test_flag == False :
            for no in self.target["rules"][BALL_NO_DATA["Temp_Rule_Idx"]]:
                
                if self.target["lottery"] == 0:
                    #jeuM_0_40000
                    if buyno <= 6:
                        idx = 40000 + (buyno - 1) * 16 + (int(no) - 1)
                    else:
                        idx = 40094 + (buyno - 6 - 1) * 14 + (int(no) - 1)  
                    driver.find_element_by_xpath("//*[@id=\"jeuM_0_" + str(idx) + "\"]").clear()
                    driver.find_element_by_xpath("//*[@id=\"jeuM_0_" + str(idx) + "\"]").send_keys(str(self.target["monerys"][BALL_NO_DATA["Temp_Monery_Idx"]][1]))   
                elif self.target["lottery"] == 1:
                    #jeuM_0_80000
                    if buyno <= 6:
                        idx = 80000 + (buyno - 1) * 16 + (int(no) - 1)
                    else:
                        idx = 80094 + (buyno - 6 - 1) * 14 + (int(no) - 1)  
                    driver.find_element_by_xpath("//*[@id=\"jeuM_0_" + str(idx) + "\"]").clear()
                    driver.find_element_by_xpath("//*[@id=\"jeuM_0_" + str(idx) + "\"]").send_keys(str(self.target["monerys"][BALL_NO_DATA["Temp_Monery_Idx"]][1]))                  
                else:
                    pass
    
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
        self.conf.read("xxoo.ini")


        if self.conf.has_section("url") == True:
            self.m_url.SetValue(self.conf.get("url", "value"))     
        else:
            self.conf.add_section("url")
            self.conf.set("url", "value", "http://99081.ajjkk6779.com")
            self.m_url.SetValue("http://99081.ajjkk6779.com")     

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
            driver.get(self.m_url.GetValue())
    
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
        driver.get(self.m_url.GetValue())        
        self.conf.set("url", "value", self.m_url.GetValue())
        #写回配置文件
        self.conf.write(open("xxoo.ini","w"))                
                
    def onsave(self, event):  
        self.conf.set("rules", "value", self.m_rules.GetValue())
        self.conf.set("monerys", "value", self.m_monerys.GetValue())
        self.conf.set("buynos", "value", self.m_buynos.GetValue())
        #写回配置文件
        self.conf.write(open("xxoo.ini","w"))
        
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
            self.rules.append(rule) 
        
        self.monerys = []
        lines = self.m_monerys.GetValue().split("\n")
        if len(lines)==0:
            return False
        for line in lines:
            monery = line.split('=')
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

