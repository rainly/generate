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
        logdebug(log)
        
    def target_func(self):
        global driver
        self.logprint("********************start**************************")  
        self.logprint("********************start**************************")  
        self.logprint("********************start**************************")  
        try:
            pass
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
        self.conf.read("alipay.ini")

        if self.conf.has_section("monery") == True:
            self.m_monery.SetValue(self.conf.get("monery", "value"))     
        else:
            self.conf.add_section("monery")
            self.conf.set("monery", "value", "0.01")
            self.m_monery.SetValue("0.01")
            
        if self.conf.has_section("users") == True:
            self.m_users.SetValue(self.conf.get("users", "value")) 
        else:
            self.conf.add_section("users")
            self.conf.set("users", "value", "")
        
        if test_flag == False :
            self.webthread = WebdriverThread("https://www.alipay.com/")
            self.webthread.start()       
                    
    def onsave(self, event):  
        self.conf.set("monery", "value", self.m_monery.GetValue())
        self.conf.set("users", "value", self.m_users.GetValue())
        #写回配置文件
        self.conf.write(open("alipay.ini","w"))
        
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
        target["monery"]  = self.monery
        target["users"]   = self.users
        self.m_button2.SetLabel('关闭')
        self.thread = BettingThread(target)
        self.thread.start()
        
    def parse(self):
        self.users = []
        lines = self.m_users.GetValue().split("\n")
        if len(lines)==0:
            return False
        for line in lines:
            user = line.split('=')
            self.users.append(user)
        
        return True
        
        
def main():
    app = wx.App()  
    main_win = MianWindow(None)  
    main_win.init_main_window()  
    main_win.Show()  
    app.MainLoop()  

if __name__ == "__main__":
    main()

