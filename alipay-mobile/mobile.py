# -*- coding: UTF-8 -*-    
import wx  
import basewin  
import sys   
import configparser
import threading  
import time
import datetime
import random
import logging
from logging import handlers
import logging
import traceback

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.domain.AlipayTradeAppPayModel import AlipayTradeAppPayModel
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.domain.AlipayTradePayModel import AlipayTradePayModel
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.SettleDetailInfo import SettleDetailInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant
from alipay.aop.api.request.AlipayOfflineMaterialImageUploadRequest import AlipayOfflineMaterialImageUploadRequest
from alipay.aop.api.request.AlipayTradeAppPayRequest import AlipayTradeAppPayRequest
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
from alipay.aop.api.request.AlipayTradePayRequest import AlipayTradePayRequest
from alipay.aop.api.response.AlipayOfflineMaterialImageUploadResponse import AlipayOfflineMaterialImageUploadResponse
from alipay.aop.api.response.AlipayTradePayResponse import AlipayTradePayResponse

from alipay.aop.api.domain.AlipayFundTransToaccountTransferModel import AlipayFundTransToaccountTransferModel
from alipay.aop.api.request.AlipayFundTransToaccountTransferRequest import AlipayFundTransToaccountTransferRequest
import random
import string

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')

"""
设置配置，包括支付宝网关地址、app_id、应用私钥、支付宝公钥等，其他配置值可以查看AlipayClientConfig的定义。
"""
alipay_client_config = AlipayClientConfig()
alipay_client_config.server_url = 'https://openapi.alipay.com/gateway.do'

'''
alipay_client_config.app_id = '2018061060383084'
#alipay_client_config.app_private_key   = 'MIIEowIBAAKCAQEAidAsiclMMRWnGmHZ58aeTBlo8sLr26wR+trX3VovT8FSMnq3G4hLIZaGj7SUr3lLlZwnUAIQ6VMP5SIYqg1Rk7yU8bTxs2QPAxRd38GUhZsRAWD2XLP27TZVjjyo68SSX0Lso/cFshM/s2viHoolS0D7+8BHWX4sNRu6KsdbZUMwKHl4WHSWNea66p5m9U4jw5ZbThZqBG28YVTH0yXImiUK0WQ+SUG93V1qJTTaVmzfCxcSq199Z18nE22FUffM2dWaUL2kzZm2RRcf8SEgUIMPinnU7nw6892jXKa4CI3QeddMqsFb6ONTe2XkaR20fJ3IsX6qK8SdhZeJV5/t0wIDAQABAoIBAGaE72z8y2pEUlAE9OY/0eiIipL1QCHlimaTwDvRaBqrlKsqsOaRaFqvMKDc1DMJR5ofVPtm3g/Ek7F/wNtYFxSRGDgKxDcQOz6uOvtGdWdCqM7ew8bItetXHSQ3qe3iCIVHMuTy0VDckum1WrwfRokJ6aopKqq/esFzQ/Wo4iucSwlZq8nsCDkrsKKDAJB41THbgWJijuNtX3BH5Ac8hREONVsuVcDRbcEG/z6f4mm8QJO1kw8ywewYCeGaN5PTvSAjNnx/TVHMDTM3T40g7iEI6aVG4UkJuF1uWB1JfHsQC4EoFD0IEYj1kxCsZgASYVIPQMTC1Dng7CpP8zJemXkCgYEA1X2ZKLck6r0jCriRawQO23LXCLT+TP0Uy3xbhL/2xLVirhc+DrN6KVAjGf4ISNwOIGUmLh/KM0DiCZDCH5p7qENa2JvbTXPW7QoOPQY4q67YLmmSDpzFeMWb9Y+pe0YBriA06kszgzClVyV6yso1lXIIjPZwwYaBaIiugUOwZAcCgYEApUEEtxjfCTX2UFPjyjv7ZQN3HuXM7cEf/ruGsJE4M+p0f7OlFLW5uam95pRIeL98J1jnQ4KRd2CswInxC4wKxmQ5317qo4E4SsKFxBOQTReLykfWpfqdwFeRP8N6AFhD5iWWyGdwfaA78rxN62pCNGOxpwSovRXLiDrrEk4YrNUCgYADy4jGdYL9fUE7No63NUpCUmdKK1V97t3IxDwoPvVXB9ZqO9WJk10vkNIe6yogiXDi2Il2NnB0usmJ2/3na+qY0iGySgr69H00l4IrSYoGW0RShuPmyJimDfU4x0X+//6VptLp+04+HcZCp1LoefG751wJjXPxrL9uKUfY2mgvTwKBgGdNZa0vlv0jBn7gch0Rse1LZUOjU5+sgluyzlfB7+hEP980ZZW0pA0z1so1F7ijuvC92pORI24EuPkDQfN9755lOOgxZWwgcxgI0aXotOP8PB6PGddX+xUpqFq7z6A3jPpptQBB6UgeylrK68ql+gzV5VAK0ZCh90GJ0zj2KOahAoGBAKJYUXvmFLpySQsP8HotpSgPHBK5OHmpFRKkMBxSnErkxFNzXs2OD5b4FcwO3iXa8jYEEO5vjtqxDajqK8cKs1AE4FgjCHesz+905AEC8bToRv+DYTUwJAh0+4qSCAXXkgCWjWypYP77+Aopgx/QVyH/OdVHHVmAzRZ0HKz1u0mF'
#alipay_client_config.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAidAsiclMMRWnGmHZ58aeTBlo8sLr26wR+trX3VovT8FSMnq3G4hLIZaGj7SUr3lLlZwnUAIQ6VMP5SIYqg1Rk7yU8bTxs2QPAxRd38GUhZsRAWD2XLP27TZVjjyo68SSX0Lso/cFshM/s2viHoolS0D7+8BHWX4sNRu6KsdbZUMwKHl4WHSWNea66p5m9U4jw5ZbThZqBG28YVTH0yXImiUK0WQ+SUG93V1qJTTaVmzfCxcSq199Z18nE22FUffM2dWaUL2kzZm2RRcf8SEgUIMPinnU7nw6892jXKa4CI3QeddMqsFb6ONTe2XkaR20fJ3IsX6qK8SdhZeJV5/t0wIDAQAB'
alipay_client_config.app_private_key   = 'MIIEowIBAAKCAQEAidAsiclMMRWnGmHZ58aeTBlo8sLr26wR+trX3VovT8FSMnq3G4hLIZaGj7SUr3lLlZwnUAIQ6VMP5SIYqg1Rk7yU8bTxs2QPAxRd38GUhZsRAWD2XLP27TZVjjyo68SSX0Lso/cFshM/s2viHoolS0D7+8BHWX4sNRu6KsdbZUMwKHl4WHSWNea66p5m9U4jw5ZbThZqBG28YVTH0yXImiUK0WQ+SUG93V1qJTTaVmzfCxcSq199Z18nE22FUffM2dWaUL2kzZm2RRcf8SEgUIMPinnU7nw6892jXKa4CI3QeddMqsFb6ONTe2XkaR20fJ3IsX6qK8SdhZeJV5/t0wIDAQABAoIBAGaE72z8y2pEUlAE9OY/0eiIipL1QCHlimaTwDvRaBqrlKsqsOaRaFqvMKDc1DMJR5ofVPtm3g/Ek7F/wNtYFxSRGDgKxDcQOz6uOvtGdWdCqM7ew8bItetXHSQ3qe3iCIVHMuTy0VDckum1WrwfRokJ6aopKqq/esFzQ/Wo4iucSwlZq8nsCDkrsKKDAJB41THbgWJijuNtX3BH5Ac8hREONVsuVcDRbcEG/z6f4mm8QJO1kw8ywewYCeGaN5PTvSAjNnx/TVHMDTM3T40g7iEI6aVG4UkJuF1uWB1JfHsQC4EoFD0IEYj1kxCsZgASYVIPQMTC1Dng7CpP8zJemXkCgYEA1X2ZKLck6r0jCriRawQO23LXCLT+TP0Uy3xbhL/2xLVirhc+DrN6KVAjGf4ISNwOIGUmLh/KM0DiCZDCH5p7qENa2JvbTXPW7QoOPQY4q67YLmmSDpzFeMWb9Y+pe0YBriA06kszgzClVyV6yso1lXIIjPZwwYaBaIiugUOwZAcCgYEApUEEtxjfCTX2UFPjyjv7ZQN3HuXM7cEf/ruGsJE4M+p0f7OlFLW5uam95pRIeL98J1jnQ4KRd2CswInxC4wKxmQ5317qo4E4SsKFxBOQTReLykfWpfqdwFeRP8N6AFhD5iWWyGdwfaA78rxN62pCNGOxpwSovRXLiDrrEk4YrNUCgYADy4jGdYL9fUE7No63NUpCUmdKK1V97t3IxDwoPvVXB9ZqO9WJk10vkNIe6yogiXDi2Il2NnB0usmJ2/3na+qY0iGySgr69H00l4IrSYoGW0RShuPmyJimDfU4x0X+//6VptLp+04+HcZCp1LoefG751wJjXPxrL9uKUfY2mgvTwKBgGdNZa0vlv0jBn7gch0Rse1LZUOjU5+sgluyzlfB7+hEP980ZZW0pA0z1so1F7ijuvC92pORI24EuPkDQfN9755lOOgxZWwgcxgI0aXotOP8PB6PGddX+xUpqFq7z6A3jPpptQBB6UgeylrK68ql+gzV5VAK0ZCh90GJ0zj2KOahAoGBAKJYUXvmFLpySQsP8HotpSgPHBK5OHmpFRKkMBxSnErkxFNzXs2OD5b4FcwO3iXa8jYEEO5vjtqxDajqK8cKs1AE4FgjCHesz+905AEC8bToRv+DYTUwJAh0+4qSCAXXkgCWjWypYP77+Aopgx/QVyH/OdVHHVmAzRZ0HKz1u0mF';
alipay_client_config.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAidAsiclMMRWnGmHZ58aeTBlo8sLr26wR+trX3VovT8FSMnq3G4hLIZaGj7SUr3lLlZwnUAIQ6VMP5SIYqg1Rk7yU8bTxs2QPAxRd38GUhZsRAWD2XLP27TZVjjyo68SSX0Lso/cFshM/s2viHoolS0D7+8BHWX4sNRu6KsdbZUMwKHl4WHSWNea66p5m9U4jw5ZbThZqBG28YVTH0yXImiUK0WQ+SUG93V1qJTTaVmzfCxcSq199Z18nE22FUffM2dWaUL2kzZm2RRcf8SEgUIMPinnU7nw6892jXKa4CI3QeddMqsFb6ONTe2XkaR20fJ3IsX6qK8SdhZeJV5/t0wIDAQAB';
'''


g_file         = None
g_mutex     = threading.Lock()
g_idx        = 0
g_mobiles   = [];

def getstr(num):
    #第一种方法
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    sa = []
    for i in range(num):
      sa.append(random.choice(seed))
    salt = ''.join(sa)
    
    #运行结果：l7VSbNEG
    #第二种方法
    salt = ''.join(random.sample(string.ascii_letters + string.digits, num))
    #print (salt)
    return salt
    #运行结果：VOuCtHZs



class AlipayThread(threading.Thread):
    def __init__(self, target, thread_num=0, timeout=5.0):
        super(AlipayThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout
        """
        得到客户端对象。
        注意，一个alipay_client_config对象对应一个DefaultAlipayClient，定义DefaultAlipayClient对象后，alipay_client_config不得修改，如果想使用不同的配置，请定义不同的DefaultAlipayClient。
        logger参数用于打印日志，不传则不打印，建议传递。
        """
        self.client = DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)
        self.show_name_idx 	= 0;
        self.remark_idx 	= 0;
        self.amount_idx 	= 0;
        self.show_names 	= self.target["show_name"].split("/")
        self.remarks 		= self.target["remark"].split("/")
        self.amounts 		= self.target["amount"].split("/")		
		
        
    def run(self):
        logger.info("*************begin*****************\n")
        global g_idx;
        global g_max;
        while self.stopped == False:
            mobile = ""
            g_mutex.acquire()
            g_idx = g_idx + 1
            if g_idx >= len(g_mobiles):
                g_mutex.release()
                break;
            mobile = g_mobiles[g_idx];            
            g_mutex.release()
            logger.info(mobile + "")
            try:
                self.once(mobile)
                pass
            except Exception as e:
                pass;
        logger.info("****************end**************\n")
            
    def once(self, mobile):
        global g_file;
        """
        系统接口示例：alipay.trade.pay
        """
        # 对照接口文档，构造请求对象
        model = AlipayFundTransToaccountTransferModel()
        model.out_biz_no         = getstr(32)
        model.payee_type         = "ALIPAY_LOGONID"
        model.payee_account      = mobile
        #model.amount            = self.target["amount"]
        '''
        self.show_name_idx = self.show_name_idx + 1
        if self.show_name_idx >= len(self.show_names):
            self.show_name_idx = 0;
        show_name = self.show_names[self.show_name_idx];
        
        self.remark_idx = self.remark_idx + 1
        if self.remark_idx >= len(self.remarks):
            self.remark_idx = 0;
        remark = self.remarks[self.remark_idx];
		
        self.amount_idx = self.amount_idx + 1
        if self.amount_idx >= len(self.amounts):
            self.amount_idx = 0;
        amount = self.amounts[self.amount_idx];
        model.payer_show_name    = show_name
        #model.payee_real_name   = self.target["real_name"]
        model.remark             = remark
        model.amount             = amount
        '''
		
        model.payer_show_name    = self.show_names[random.randint(0,len(self.show_names))]
        model.remark             = self.remarks[random.randint(0,len(self.remarks))]
        model.amount             = self.amounts[random.randint(0,len(self.amounts))]
		
        request = AlipayFundTransToaccountTransferRequest(biz_model=model)
        # 如果有auth_token、app_auth_token等其他公共参数，放在udf_params中
        # udf_params = dict()
        # from alipay.aop.api.constant.ParamConstants import *
        # udf_params[P_APP_AUTH_TOKEN] = "xxxxxxx"
        # request.udf_params = udf_params
        # 执行请求，执行过程中如果发生异常，会抛出，请打印异常栈
        response_content = None
        try:
            response_content = self.client.execute(request)
        except Exception as e:
            #pass
            print(traceback.format_exc())
        if not response_content:
            print("failed execute2\n")
        else:
            response = AlipayTradePayResponse()
            # 解析响应结果
            response.parse_response_content(response_content)
            #logger.info(response.body)
            if response.is_success() or response.sub_code == "EXCEED_LIMIT_SM_MIN_AMOUNT":
                # 如果业务成功，则通过respnse属性获取需要的值
                #print("get response trade_no:" + response.sub_msg)
                g_file.write(mobile + "\n")
                # 刷新缓冲区
                g_file.flush()
            else:
                # 如果业务失败，则从错误码中可以得知错误情况，具体错误码信息可以查看接口文档
                logger.info(response.code + "," + response.msg + "," + response.sub_code + "," + response.sub_msg + "\n")                
        
    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped
        
        
##################################################################
##################################################################                
##################################################################

import json
import urllib
import urllib.request
import urllib.response
import urllib.error
import http.cookiejar
from mobile import *



#声明一个CookieJar对象实例来保存cookie
cookiejar = cookiejar = http.cookiejar.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookiejar)
#通过handler来构建opener
opener = urllib.request.build_opener(handler)

#此处的open方法同urllib2的urlopen方法，也可以传入request
#response = opener.open('http://www.baidu.com')
user_agent = 'Mozilla/5.0 (Windows NT 6.1 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'  
headers = { 'User-Agent' : user_agent }  

 
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
    






class MianWindow(basewin.BaseMainWind):  
    # 首先，咱们从刚刚源文件中将主窗体继承下来.就是修改过name属性的主窗体咯。  
    def init_main_window(self):  
        global alipay_client_config
        self.threads = [];#存放线程的数组，相当于线程池
        
        #生成config对象
        self.conf = configparser.ConfigParser()
        #用config对象读取配置文件
        self.conf.read("mobile.ini")
        
        if self.conf.has_section("app_id") == True:
            alipay_client_config.app_id = self.conf.get("app_id", "value")

        if self.conf.has_section("app_private_key") == True:
            alipay_client_config.app_private_key = self.conf.get("app_private_key", "value")

        if self.conf.has_section("alipay_public_key") == True:
            alipay_client_config.alipay_public_key = self.conf.get("alipay_public_key", "value")

        if self.conf.has_section("prefix") == True:
            self.m_prefix.SetValue(self.conf.get("prefix", "value"))
            
        if self.conf.has_section("username") == True:
            self.m_username.SetValue(self.conf.get("username", "value"))

        if self.conf.has_section("password") == True:
            self.m_userpwd.SetValue(self.conf.get("password", "value"))
        self.valid = False
        self.onLogin(None)
            

            
    def OnClose( self, event ):
        event.Skip()
        if  len(self.threads) != 0:
            for t in self.threads:
                if t.is_alive():
                    t.stop()
                t.join()
            self.threads = []
            g_file.close()
            self.m_button2.SetLabel('开始')
            return
            
    def onSave(self, event):
        self.conf.set("prefix", "value", self.m_prefix.GetValue())
        self.conf.set("username", "value", self.m_username.GetValue())
        self.conf.set("password", "value", self.m_userpwd.GetValue())
        #写回配置文件
        self.conf.write(open("mobile.ini","w"))
        
    def onStart(self, event):
        self.onSave(event)
        if self.valid != True:
            wx.MessageBox("账号未登录,请先登录", caption="提示", style=wx.OK)
            return
            
        global g_file;
        global g_idx;
        global g_max;
        if  len(self.threads) != 0:
            for t in self.threads:
                if t.is_alive():
                    t.stop()
                t.join()
            self.threads = []
            g_file.close()
            self.m_btstart.SetLabel('开始')
            return

        prefix_mobiles = self.m_prefix.GetValue().split("/")
        for prefix_mobile in prefix_mobiles:
            left_max = 0
            left_len = 11 - len(prefix_mobile)
            for i in range(left_len):
                left_max = left_max * 10 + 9    
            
            for i in range(left_max):
                s      = str(i)
                mobile = prefix_mobile + s.zfill(left_len);
                g_mobiles.append(mobile)
        
        self.m_btstart.SetLabel('关闭')
        tf = datetime.datetime.now().strftime('%y%m%d%I%M%S%p')       
        g_file = open(tf + '.txt', 'w')
        self.threads = []
        for i in range(0, int(self.m_threadnum.GetValue())):
            target = {}
            target["amount"]    = self.m_amount.GetValue()
            target["show_name"] = self.m_show_name.GetValue()
            target["remark"]    = self.m_remark.GetValue()
            thread = AlipayThread(target)
            thread.start()
            self.threads.append(thread)
        print("******************************\n")
    
    def onLogin( self, event ):
        #event.Skip()        
        logindict = {}
        logindict["username"]               = self.m_username.GetValue()
        logindict["password"]               = self.m_userpwd.GetValue()
        data = urllib.parse.urlencode(logindict).encode('utf-8')
        url  = "http://www.duboren.com/agent/alipay.php"
        #print(url)
        html = GetHttp(url = url, data = data, headers = headers, method = 'POST')
        if html == "ok":
            self.valid = True
            self.m_logintip.SetLabel("登录成功")
        else:
            self.valid = False
            self.m_logintip.SetLabel("登录失败")            

        
def main():
    app = wx.App()  
    main_win = MianWindow(None)  
    main_win.init_main_window()  
    main_win.Show()  
    app.MainLoop()  

if __name__ == "__main__":
    main()

