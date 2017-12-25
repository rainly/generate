## -*- coding: utf-8 -*-
##Author：哈士奇说喵
from tkinter import *
import tkinter.messagebox as messagebox
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import messagebox as mBox
import threading  
import time
from selenium import webdriver


class TestThread(threading.Thread):

    def __init__(self, target, thread_num=0, timeout=1.0):
        super(TestThread, self).__init__()
        self.target = target
        self.thread_num = thread_num
        self.stopped = False
        self.timeout = timeout

    def run(self):
        def target_func():
            #inp = raw_input("Thread %d: " % self.thread_num)
            #print('Thread %s input %s' % (self.thread_num, inp))
            while self.stopped != True:
                PostUrl = "http://bw1.cpa700.com/"
                driver=webdriver.Chrome()
                driver.get(PostUrl)
                self.target.insert(tk.INSERT,'第' + str(0) + '线程\n')  
                #time.sleep(1000)
                while self.stopped != True:
                    try:
                        frame  = driver.find_element_by_xpath("//*[@id='fset1']/frame[2]")
                    except:
                        print("error lineno:"+str(sys._getframe().f_lineno))
                        time.sleep(1)
                        continue
                        pass
                    
                    print(name3.text)
                    print(rate3.text)
                    print(money3.text)

        subthread = threading.Thread(target=target_func, args=())
        subthread.setDaemon(True)
        subthread.start()

        while not self.stopped:
            subthread.join(self.timeout)

        print('Thread stopped')

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped


#由于tkinter中没有ToolTip功能，所以自定义这个功能如下
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
 
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.thread = None
        self.createWidgets()

    #===================================================================
    def createToolTip(self, widget, text):
        self.toolTip = ToolTip(widget)
        def enter(event):
            self.toolTip.showtip(text)
        def leave(event):
            self.toolTip.hidetip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

    def createWidgets(self):
        # Tab Control introduced here --------------------------------------
        self.tabControl = ttk.Notebook(self)          # Create Tab Control
        self.tab1 = ttk.Frame(self.tabControl)            # Create a tab
        self.tabControl.add(self.tab1, text='第一页')      # Add the tab
        self.tab2 = ttk.Frame(self.tabControl)            # Add a second tab
        self.tabControl.add(self.tab2, text='第二页')      # Make second tab visible
        self.tab3 = ttk.Frame(self.tabControl)            # Add a third tab
        self.tabControl.add(self.tab3, text='第三页')      # Make second tab visible
        self.tabControl.pack(expand=1, fill="both")  # Pack to make visible
        # ~ Tab Control introduced here -----------------------------------------
        self.createTab1()
        self.createTab2()
        self.createTab3()
        self.createmenu()

    def createTab1(self):
        #---------------Tab1控件介绍------------------#
        # Modified Button Click Function
        def clickMe():
            text = self.btaction.config('text')
            if  text[4] == '关闭':
                self.btaction.configure(text='开始' + self.name.get())
                self.thread.stop()
                self.thread.join()
            else:
                self.btaction.configure(text='关闭' + self.name.get())
                #btaction.configure(state='disabled') # Disable the Button Widget
                self.thread = TestThread(self.scr)
                self.thread.start()

        # Spinbox callback
        def _spin():
            value = self.spin.get()
            #print(value)
            self.scr.insert(tk.INSERT, value + '\n')

        def _spin2():
            value = self.spin2.get()
            #print(value)
            self.scr.insert(tk.INSERT, value + '\n')


        # We are creating a container tab3 to hold all other widgets
        self.monty = ttk.LabelFrame(self.tab1, text='控件示范区1')
        self.monty.grid(column=0, row=0, padx=8, pady=4)

        # Changing our Label
        ttk.Label(self.monty, text="输入文字:").grid(column=0, row=0, sticky='W')

        # Adding a Textbox Entry widget
        self.name = tk.StringVar()
        self.nameEntered = ttk.Entry(self.monty, width=12, textvariable=self.name)
        self.nameEntered.grid(column=0, row=1, sticky='W')

        # Adding a Button
        self.btaction = ttk.Button(self.monty,text="开始",width=10,command=clickMe)   
        self.btaction.grid(column=2,row=1,rowspan=2,ipady=7)

        ttk.Label(self.monty, text="请选择一本书:").grid(column=1, row=0,sticky='W')

        # Adding a Combobox
        self.book = tk.StringVar()
        self.bookChosen = ttk.Combobox(self.monty, width=12, textvariable=self.book)
        self.bookChosen['values'] = ('平凡的世界', '亲爱的安德烈','看见','白夜行')
        self.bookChosen.grid(column=1, row=1)
        self.bookChosen.current(0)  #设置初始显示值，值为元组['values']的下标
        self.bookChosen.config(state='readonly')  #设为只读模式

        # Adding 2 Spinbox widget using a set of values
        self.spin = Spinbox(self.monty, from_=10,to=25, width=5, bd=8, command=_spin) 
        self.spin.grid(column=0, row=2)

        self.spin2 = Spinbox(self.monty, values=('Python3入门', 'C语言','C++', 'Java', 'OpenCV'), width=13, bd=3, command=_spin2) 
        self.spin2.grid(column=1, row=2,sticky='W')
 
        # Using a scrolled Text control
        self.scrolW = 30
        self.scrolH = 5
        self.scr = scrolledtext.ScrolledText(self.monty, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, sticky='WE', columnspan=3)

        # Add Tooltip
        self.createToolTip(self.spin,       '这是一个Spinbox.')
        self.createToolTip(self.spin2,      '这是一个Spinbox.')
        self.createToolTip(self.btaction,   '这是一个Button.')
        self.createToolTip(self.nameEntered,'这是一个Entry.')
        self.createToolTip(self.bookChosen, '这是一个Combobox.')
        self.createToolTip(self.scr,        '这是一个ScrolledText.')

        # 一次性控制各控件之间的距离
        for child in self.monty.winfo_children(): 
            child.grid_configure(padx=3,pady=1)
        # 单独控制个别控件之间的距离
        self.btaction.grid(column=2,row=1,rowspan=2,padx=6)
        #---------------Tab1控件介绍------------------#
    def createTab2(self):
        #---------------Tab2控件介绍------------------#
        # We are creating a container tab3 to hold all other widgets -- Tab2
        self.monty2 = ttk.LabelFrame(self.tab2, text='控件示范区2')
        self.monty2.grid(column=0, row=0, padx=8, pady=4)
        # Creating three checkbuttons
        self.chVarDis = tk.IntVar()
        self.check1 = tk.Checkbutton(self.monty2, text="失效选项", variable=self.chVarDis, state='disabled')
        self.check1.select()  
        self.check1.grid(column=0, row=0, sticky=tk.W)                 

        self.chVarUn = tk.IntVar()
        self.check2 = tk.Checkbutton(self.monty2, text="遵从内心", variable=self.chVarUn)
        self.check2.deselect()   #Clears (turns off) the checkbutton.
        self.check2.grid(column=1, row=0, sticky=tk.W)                  
 
        self.chVarEn = tk.IntVar()
        self.check3 = tk.Checkbutton(self.monty2, text="屈于现实", variable=self.chVarEn)
        self.check3.deselect()
        self.check3.grid(column=2, row=0, sticky=tk.W)                 

        # GUI Callback function
        def checkCallback(*ignoredArgs):
            # only enable one checkbutton
            if chVarUn.get(): check3.configure(state='disabled')
            else:             check3.configure(state='normal')
            if chVarEn.get(): check2.configure(state='disabled')
            else:             check2.configure(state='normal') 
 
        # trace the state of the two checkbuttons #？？
        self.chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())    
        self.chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())   

        # Radiobutton list
        values = ["富强民主", "文明和谐", "自由平等","公正法治","爱国敬业","诚信友善"]

        # Radiobutton callback function
        def radCall():
            radSel = radVar.get()
            if   radSel == 0: monty2.configure(text='富强民主')
            elif radSel == 1: monty2.configure(text='文明和谐')
            elif radSel == 2: monty2.configure(text='自由平等')
            elif radSel == 3: monty2.configure(text='公正法治')
            elif radSel == 4: monty2.configure(text='爱国敬业')
            elif radSel == 5: monty2.configure(text='诚信友善')

        # create three Radiobuttons using one variable
        self.radVar = tk.IntVar()

        # Selecting a non-existing index value for radVar
        self.radVar.set(99)    

        # Creating all three Radiobutton widgets within one loop
        for col in range(4):
            #curRad = 'rad' + str(col)
            self.curRad = tk.Radiobutton(self.monty2, text=values[col], variable=self.radVar, value=col, command=radCall)
            self.curRad.grid(column=col, row=6, sticky=tk.W, columnspan=3)
        for col in range(4,6):
            #curRad = 'rad' + str(col)
            self.curRad = tk.Radiobutton(self.monty2, text=values[col], variable=self.radVar, value=col, command=radCall)
            self.curRad.grid(column=col - 4, row=7, sticky=tk.W, columnspan=3)

        style = ttk.Style()
        style.configure("BW.TLabel", font=("Times", "10",'bold'))
        ttk.Label(self.monty2, text="   社会主义核心价值观",style="BW.TLabel").grid(column=2, row=7,columnspan=2, sticky=tk.EW)

        # Create a container to hold labels
        self.labelsFrame = ttk.LabelFrame(self.monty2, text=' 嵌套区域 ')
        self.labelsFrame.grid(column=0, row=8,columnspan=4)
 
        # Place labels into the container element - vertically
        ttk.Label(self.labelsFrame, text="你才25岁，你可以成为任何你想成为的人。").grid(column=0, row=0)
        ttk.Label(self.labelsFrame, text="不要在乎一城一池的得失，要执着。").grid(column=0, row=1,sticky=tk.W)

        # Add some space around each label
        for child in self.labelsFrame.winfo_children(): 
            child.grid_configure(padx=8,pady=4)
        #---------------Tab2控件介绍------------------#
    def createTab3(self):
        #---------------Tab3控件介绍------------------#
        self.tab3 = tk.Frame(self.tab3, bg='#AFEEEE')
        self.tab3.pack()
        for i in range(2):
            canvas = 'canvas' + str(i)
            canvas = tk.Canvas(self.tab3, width=162, height=95, highlightthickness=0, bg='#FFFF00')
            canvas.grid(row=i, column=i)
        #---------------Tab3控件介绍------------------#

    def createmenu(self):
        #----------------菜单栏介绍-------------------#
        # Exit GUI cleanly
        def _quit():
            quit()
            destroy()
            exit()
    
        # Creating a Menu Bar
        menuBar = Menu(self)
        self.config(menu = menuBar)
        # Add menu items
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="新建")
        fileMenu.add_separator()
        fileMenu.add_command(label="退出", command=_quit)
        menuBar.add_cascade(label="文件", menu=fileMenu)


        # Display a Message Box
        def _msgBox1():
            mBox.showinfo('Python Message Info Box', '通知：程序运行正常！')
        def _msgBox2():
            mBox.showwarning('Python Message Warning Box', '警告：程序出现错误，请检查！')
        def _msgBox3():
            mBox.showwarning('Python Message Error Box', '错误：程序出现严重错误，请退出！')
        def _msgBox4():
            answer = mBox.askyesno("Python Message Dual Choice Box", "你喜欢这篇文章吗？\n您的选择是：") 
            if answer == True:
                mBox.showinfo('显示选择结果', '您选择了“是”，谢谢参与！')
            else:
                mBox.showinfo('显示选择结果', '您选择了“否”，谢谢参与！')

        # Add another Menu to the Menu Bar and an item
        msgMenu = Menu(menuBar, tearoff=0)
        msgMenu.add_command(label="通知 Box", command=_msgBox1)
        msgMenu.add_command(label="警告 Box", command=_msgBox2)
        msgMenu.add_command(label="错误 Box", command=_msgBox3)
        msgMenu.add_separator()
        msgMenu.add_command(label="判断对话框", command=_msgBox4)
        menuBar.add_cascade(label="消息框", menu=msgMenu)
        #----------------菜单栏介绍-------------------#
## Create instance
#win = tk.Tk()   
## Add a title
#win.title("Python 图形用户界面")
## Disable resizing the GUI
#win.resizable(0,0)
## Change the main windows icon
##win.iconbitmap(r'C:\Users\feng\Desktop\研.ico')
## Place cursor into name Entry
#nameEntered.focus()      
##======================
## Start GUI
##======================
#win.mainloop()

def main():
    app = Application()
    app.title("Python 图形用户界面")
    # 主消息循环:
    app.mainloop()

if __name__ == "__main__":
    main()

