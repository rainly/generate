#coding=utf-8
from tkinter import *
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import messagebox as mBox
import tkinter.messagebox as messagebox
import tkinter as tk
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import sqlite3
import threading  
import time

import urllib
import urllib.request
import urllib.response
import urllib.error
import http.cookiejar

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.thread = None
        try:
            #driver.quit()
            pass
        except:
            pass

def main():
    app = Application()
    app.title("cpa700 自动打码神器")
    # 主消息循环:
    app.mainloop()

if __name__ == "__main__":
    main()
    

