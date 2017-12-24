# -*- coding: utf-8 -*-
#Author：哈士奇说喵
from selenium import webdriver
import os
from pytesseract import *  
import sys,time
from PIL import Image,ImageEnhance

#shift+tab多行缩进(左)
#reload(sys)
PostUrl = "http://yjsymis.hrbeu.edu.cn/gsmis/indexAction.do"
#http://blog.csdn.net/mrlevo520/article/details/51901579

#方法1[推荐]: 
#将tessdata目录的上级目录所在路径(默认为tesseract-ocr安装目录)添加至TESSDATA_PREFIX环境变量中
#例如: C:\Program Files (x86)\Tesseract-OCR
#Please make sure the TESSDATA_PREFIX environment variable is set to the parent directory of your "tessdata" directory.
#方法2:  在.py文件配置中指定tessdata-dir
#tessdata_dir_config = '--tessdata-dir "D:\\Tesseract-OCR\\tessdata"'
# tessdata_dir_config = '--tessdata-dir "'C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
#pytesseract.image_to_string(image, config=tessdata_dir_config)

driver=webdriver.Chrome()
driver.get(PostUrl)

i=0
while 1:#sb登录系统，即使输对所有消息还是登不进去的，需要登录两次及以上

    i=i+1
    try:
        elem_user = driver.find_element_by_name('id')
        elem_psw = driver.find_element_by_name('password')
        elem_code = driver.find_element_by_name('checkcode')
    except:
        break
    #-------------------对验证码进行区域截图，好吧，这方法有点low------------------
    driver.get_screenshot_as_file('F:\\MrLevo\\image1.jpg')#比较好理解
    im =Image.open('F:\\MrLevo\\image1.jpg')
    box = (516,417,564,437)  #设置要裁剪的区域
    region = im.crop(box)     #此时，region是一个新的图像对象。
    #region.show()#显示的话就会被占用，所以要注释掉
    region.save("F:\\image_code.png", "png")

    #-------------------------------------------------------------------

    #--------------ImageGrab.grab()直接可以区域截图，但是有bug，截图不全-------
    '''
    bbox = (780, 0, 1020, 800)
    img = ImageGrab.grab()
    img.save("E:\image_code.jpg")
    img.show()
    '''
    #-------------------------手动输入验证码：适用范围更广，但不够方便------------------------------
    '''
    response = opener.open(CaptchaUrl)
    picture = response.read()
    with open('e:/image.jpg', 'wb') as local:
        local.write(picture)
    # 保存验证码到本地

    #------------对于不能用pytesser+ocr进行识别，手动打开图片手动输入--------
    # 打开保存的验证码图片 输入
    #SecretCode = raw_input('please enter the code: ')
    #----------------------------------------------------------------------
    '''

    #--------------------图片增强+自动识别简单验证码-----------------------------
    #time.sleep(3)防止由于网速，可能图片还没保存好，就开始识别
    def image_file_to_string(file):
        cwd = os.getcwd()
        try :
            os.chdir("F:\\MrLevo\\Anaconda2\\Lib")
            return pytesseract.image_to_string(file)
        finally:
            os.chdir(cwd)
    im=Image.open("F:\\image_code.png")
    imgry = im.convert('L')#图像加强，二值化
    sharpness =ImageEnhance.Contrast(imgry)#对比度增强
    sharp_img = sharpness.enhance(2.0)
    sharp_img.save("F:\\image_code1.png")
    #http://www.cnblogs.com/txw1958/archive/2012/02/21/2361330.html
    #imgry.show()#这是分布测试时候用的，整个程序使用需要注释掉
    #imgry.save("F:\\image_code.png")
    im = Image.open("F:\\image_code.png")
    tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    code= pytesseract.image_to_string(im, config=tessdata_dir_config)#code即为识别出的图片数字str类型
    print (code)
    #打印code观察是否识别正确


    #----------------------------------------------------------------------
    if i <= 2: # 根据自己登录特性，我这里是验证码失败一次，重填所有，失败两次，重填验证码
        elem_user.send_keys('S315080092')
        elem_psw.send_keys('xxxxxxxxxx')

    elem_code.send_keys(code)
    click_login = driver.find_element_by_xpath("//img[@src='main_images/images/loginbutton.gif']")
    click_login.click()


#time.sleep(5)#搜索结果页面停留片刻
#driver.save_screenshot('C:\Users\MrLevo\image.jpg')
#driver.close()
#driver.quit()



