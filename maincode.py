#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python3
# coding=UTF-8

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from tkinter import *
import time
import os
import random
import tkinter as tk
import tkinter.messagebox
import warnings





#子函数定义：绘制主体窗口
def mainplace():
    
#【语句块】创建窗口，命名为window
    window = tk.Tk()                        #创建tk对象
    window.title('🦆牌每日小🦆报')         #窗口标题
    window.geometry('520x390')              #窗口尺寸大小
    window.geometry('+520+130')             #窗口位置坐标
    
#【语句块】创建固定标签2个，命名为lab1：学号，lab2：密码
    lab1 = tk.Label(window,
                    width=20,
                    fg='SaddleBrown',
                    font='华文中宋',
                    text="   学号")         #lab1文本内容
    lab1.place(x=50,y=22)                   #lab1位置坐标
    lab2 = tk.Label(window,
                    width=20,
                    fg='OliveDrab',
                    font='华文中宋',
                    text='   密码')         #lab2文本内容
    lab2.place(x=50,y=52)                   #lab2位置坐标

#【语句块】创建专属标签1个，命名tag
    tag=tk.Label(window,
                 text="                             *********************** *********************************************\n\
                              ***********上海大学每日一报********防控疫情人人有责***********\n\
                              ********居家隔离绝不添乱********响应政策利国利民**************\n\
                              *********春节返乡严守纪律*********口罩常戴距离常保************\n\
                              ************************Shanghai University**********************\n\
                              ***********上海大学在校学子***********不堪其扰深受其害********\n\
                              **********代表正义的鸭妈妈***********挺身而出铤而走险*********\n\
                              **********敢冒天下之大不韪*********安定四方救济苍生***********\n\
                              ***********从此不再频频催报********辅导员他好我也好***********\n\
                              **********仅供鸭宝交流使用*********宣扬传播妈鲨了你***********\n\
                              *********************************************************************")
    tag.place(x=-20,y=140)       #tag位置坐标
                 
#把学号密码定义成全局变量
    global account,password,entry_ac,entry_pw             
    account = tk.StringVar()
    password= tk.StringVar()
    
#【前端】从键盘获取学号
    entry_ac = tk.Entry(window,               #学号输入框entry_ac
                        width=20,             #学号entry宽度
                        bg='SandyBrown',      #学号entry背景填充色
                        textvariable=account) #学号entry内容
    entry_ac.pack()                           #打包返回学号
    entry_ac.place(x=190,y=22)                #学号entry位置坐标

#【前端】从键盘获取密码
    entry_pw = tk.Entry(window,               #密码输入框entry_pw
                        width=20,             #密码entry宽度
                        bg='light green',     #密码entry背景填充色
                        textvariable=password,#密码entry内容
                        show="*")             #密码entry内字符加密
    entry_pw.pack()                           #打包返回密码
    entry_pw.place(x=190,y=54)                #密码entry位置坐标
                                              
#【前端】登录按钮                             
    btn = tk.Button(window,text='登录',       
                    width=20,
                    fg='purple',
                    bg='light blue',
                    command=window.destroy)   #简洁明了，直接杀死进程，将变量递入autoreport函数
    btn.pack()                                #打包返回按钮
    btn.place(x=188,y=88)                     #按钮位置坐标

    window.mainloop()                         #进入事件循环
    
#【子函数执行】执行mainplace窗体函数
mainplace()

##############################################################
########居家隔离绝不添乱########响应政策利国利民##############
#########春节返乡严守纪律#########口罩常戴距离常保############
######################Shanghai University#####################
##########上海大学每日一报########防控疫情人人有责############
###########上海大学在校学子###########不堪其扰深受其害########
##########代表正义的鸭妈妈###########挺身而出铤而走险#########
##########敢冒天下之大不韪#########安定四方救济苍生###########
###########从此不再频频催报########辅导员他好我也好###########
##########仅供鸭宝交流使用#########宣扬传播妈鲨了你###########
##############################################################

#【全局】传递全局变量
A=account.get()
#A="输入你的学号"
B=password.get()
#B="输入你的密码"


#【子类定义】自动一报
class SelfReport(object):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('-log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=r'C:\users\青衣子暵\DOWNLOADS\CHROMEDRIVER.exe',options=options,service_log_path=os.devnull)     
        time.sleep(1)

    def auto_report(self): 
        driver=self.driver
        driver.get('https://selfreport.shu.edu.cn/Default.aspx')        #打开上海大学健康之路
        #print("已进入填报网站")
        username = driver.find_element_by_id("username")                #寻找“学工号输入框”元素
        username.send_keys(A)                                           #输入学号
        password = driver.find_element_by_id("password")                #寻找“密码输入框”元素
        password.send_keys(B)                                           #输入密码
        #print("自动填入学号密码完成")
        submit = driver.find_element_by_id("submit")                    #寻找“登录”按钮
        submit.click()                                                  #单击之
        #print("进入每日一报网站")                                       
        driver.find_element_by_id("lnkReport").click()                  #寻找“每日一报”按钮
        promise = driver.find_element_by_id("p1_ChengNuo-inputEl-icon") #寻找“勾选承诺书”元素
        promise.click()                                                 #单击之
        
        inSH=driver.find_element_by_id("fineui_8-inputEl-icon")         #寻找“不在上海”元素
        inSH.click()                                                    #单击之
        adds = driver.find_element_by_id("fineui_12-inputEl-icon")        #寻找“提交”按钮
        adds.click()
        
        #print(time.ctime())
        
        time.sleep(3)
        handin = driver.find_element_by_id("p1_ctl00_btnSubmit")        #寻找“提交”按钮
        handin.click()                                                  #单击之
        sure1=driver.find_element_by_link_text("确定")                  #寻找“确定”按钮
        sure1.click()                                                   #单击之
        
        time.sleep(3)
        driver.close()                                                  #关闭浏览器
        #print("今日自动报毕。")
        
        #driver.quit();       # 关闭 ChromeDriver 接口
        #service.stop();
        
    def run(self):
        self.auto_report()

if __name__ == '__main__':
    sp = SelfReport()
    sp.run()
