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
            BALL_NO_DATA["Temp_Monery"]          =  self.target["monerys"][0]
            BALL_NO_DATA["Temp_Rule"]            =  None
            BALL_NO_DATA["Temp_Rule_Idx"]        =  0
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
        self.roads  = {}   
        self.backup = 0
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
                    driver.find_element_by_xpath("//*[@id=\"jeuM_0_40010\"]")
                    
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
                    
                def GetType(BallNo):
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
                    
                Award_Issue_Road = []                    
                if test_flag == False:
                    Award_Issue_Road_t = []
                    for idx  in range(1,11):
                        BallText = driver.find_element_by_xpath("//*[@id=\"d_GameLottery\"]/table/tbody/tr/td[" + str(idx + 1) + "]").get_attribute("class").replace("No_", "")
                        Award_Issue_Road.append(GetType(BallText))
                        Award_Issue_Road_t.append(BallText)
                    Award_Issue_Road.append(GetType(int(Award_Issue_Road_t[0]) + int(Award_Issue_Road_t[9])))
                else:
                    Award_Issue_Road_t = []
                    for idx  in range(1,11):
                        BallText = random.randint(1,10)
                        Award_Issue_Road.append(GetType(BallText))
                        Award_Issue_Road_t.append(BallText)
                    Award_Issue_Road.append(GetType(int(Award_Issue_Road_t[0]) + int(Award_Issue_Road_t[9])))
                
                self.logprint("路单数据" + str(Award_Issue_Road))
                
                Last_Award_Issue = Cur_Award_Issue2
                
                self.roads[Cur_Award_Issue2] = Award_Issue_Road
        
                Bet = False
                for buyno in buynos:
                    Bet = Bet | self.delBallNo(Award_Issue_Road, int(buyno), BALL_NO_DATAS[buyno])
                    time.sleep(1)
                    
                if test_flag == False:
                    if Bet == True:
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
        self.logprint("********************end**************************")  
        self.logprint("********************end**************************")  
        self.logprint("********************end**************************")      
    def delBallNo(self, road, buyno, BALL_NO_DATA):
        Win = 0
        #处理中奖结果
        if BALL_NO_DATA["Temp_Rule"] != None:
            if  BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] in road[buyno - 1]:
                Win = 1
                self.logprint("位置" + str(buyno) + "***中奖***金额:" + BALL_NO_DATA["Temp_Monery"][1])
            else:
                Win = 0
                self.logprint("位置" + str(buyno) + "***未中奖***")
            
            
            ##[1, 10, 2, 2]    
            for monery in self.target["monerys"]:
                if  Win == 1 and monery[0] == BALL_NO_DATA["Temp_Monery"][2]:
                    BALL_NO_DATA["Temp_Monery"] = monery
                    break
                elif  Win == 0 and monery[0] == BALL_NO_DATA["Temp_Monery"][3]:
                    BALL_NO_DATA["Temp_Monery"] = monery
                    break
        else:
            self.logprint("位置" + str(buyno) + "***未下注***")

        #处理中奖结果
        if BALL_NO_DATA["Temp_Rule"] != None:
            BALL_NO_DATA["Temp_Rule_Idx"] = BALL_NO_DATA["Temp_Rule_Idx"] + 1
            if len(BALL_NO_DATA["Temp_Rule"][1]) <= BALL_NO_DATA["Temp_Rule_Idx"]:
                BALL_NO_DATA["Temp_Rule"] = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0

            #不回揽
            if self.backup == 0:
                self.logprint("位置" + str(buyno) + "***不回揽***")
                pass
            #中回揽
            elif self.backup == 1 and Win == 1:
                BALL_NO_DATA["Temp_Rule"] = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0
                self.logprint("位置" + str(buyno) + "***中回揽***")
            #错回揽
            elif self.backup == 2 and Win == 1:
                BALL_NO_DATA["Temp_Rule"] = None
                BALL_NO_DATA["Temp_Rule_Idx"] = 0
                self.logprint("位置" + str(buyno) + "***错回揽***")
           
        #处理路单规则                
        if BALL_NO_DATA["Temp_Rule"] == None:
            keys = sorted(self.roads)
            tmp  = ""
            for key in keys:
                tmp = tmp + str(self.roads[key][buyno - 1])

            self.logprint("位置" + str(buyno) + "***当前路单***" + tmp)

            for rule in self.target["rules"]:
                #[大大， 小小]
                rule0 = rule[0]
                self.logprint("位置" + str(buyno) + "***查找规则***" + rule0)
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
                        for item in self.roads[roadKey][buyno - 1]:
                            if item == rule0[idx]:
                                _isEqual = True
                        if _isEqual == False:
                            isEqual = False
                            break
                if isEqual:
                    BALL_NO_DATA["Temp_Rule"]     = rule
                    BALL_NO_DATA["Temp_Rule_Idx"] = 0
                    self.logprint("位置" + str(buyno) + "***规则符合条件***" + str(rule[0]) + "=" + str(rule[1]))
                    break
                else:
                    self.logprint("位置" + str(buyno) + "***规则不符合条件***" + str(rule[0]) + "=" + str(rule[1]))  
                    pass 
        else: 
            self.logprint("位置" + str(buyno) + "***回揽未结束***")
            pass
                      
        #双面玩法
        if BALL_NO_DATA["Temp_Rule"] != None:
            self.logprint("位置" + str(buyno) + "***购买:" + BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] + "金额：" + str(BALL_NO_DATA["Temp_Monery"][1]))
            Bet = True
            #jeuM_0_40010
            #jeuM_0_40104
            if buyno <= 6:
                idx = 40010 + (buyno - 1) * 16
            else:
                idx = 40104 + (buyno - 7) * 14
            ####
            if BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] == "大":
                idx = idx + 0;  
            elif BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] == "小":
                idx = idx + 1;  
            elif BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] == "单":
                idx = idx + 2; 
            elif BALL_NO_DATA["Temp_Rule"][1][BALL_NO_DATA["Temp_Rule_Idx"]] == "双":
                idx = idx + 3; 
            driver.find_element_by_xpath("//*[@id=\"jeuM_0_" + str(idx) + "\"]").clear()
            driver.find_element_by_xpath("//*[@id=\"jeuM_0_" + str(idx) + "\"]").send_keys(str(BALL_NO_DATA["Temp_Monery"][1]))
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
        self.conf.read("xxoo_2.ini")

    
        if self.conf.has_section("url") == True:
            self.m_url.SetValue(self.conf.get("url", "value"))     
        else:
            self.conf.add_section("url")
            self.conf.set("url", "value", "http://16781.ajjkk6779.com")
            self.m_url.SetValue("http://16781.ajjkk6779.com")     

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

        
        if test_flag == False :
            self.webthread = WebdriverThread(self.m_url.GetValue())
            self.webthread.start()
    
    def onEnter( self, event ):
        global driver
        driver.get(self.m_url.GetValue())        
        self.conf.set("url", "value", self.m_url.GetValue())
        #写回配置文件
        self.conf.write(open("xxoo_2.ini","w"))                
                
    def onsave(self, event):  
        self.conf.set("rules", "value", self.m_rules.GetValue())
        self.conf.set("monerys", "value", self.m_monerys.GetValue())
        self.conf.set("buynos", "value", self.m_buynos.GetValue())
        #写回配置文件
        self.conf.write(open("xxoo_2.ini","w"))
        
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
        
        self.m_button2.SetLabel('关闭')
        self.thread = BettingThread(target)
        self.thread.start()
        
    def parse(self):
        self.rules = []
        lines = self.m_rules.GetValue().split("\n")
        if len(lines)==0:
            wx.MessageBox("购买规则配置出错", caption="提示", style=wx.OK)
            return False
        for line in lines:
            rule = line.split('=')    
            if len(rule) != 2:        
                wx.MessageBox("购买规则配置出错", caption="提示", style=wx.OK)
                return False            
            self.rules.append(rule)
        ###############################
        self.monerys = []
        lines = self.m_monerys.GetValue().split("\n")
        if len(lines)==0:
            wx.MessageBox("购买金额配置出错", caption="提示", style=wx.OK)
            return False
        for line in lines:
            monery = line.split('=')
            if len(monery) != 4:
                wx.MessageBox("购买金额配置出错", caption="提示", style=wx.OK)
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

