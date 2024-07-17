import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess
import platform
import re
import functions as F
import styles as S
import app

class NavBtn(ttk.Button):
    name="navbtn"
    display = "导航按钮"
    root = None
    win = None
    '''
    button
    '''
    def __init__(self, name, root, text, bootstyle=(PRIMARY, OUTLINE), state=NORMAL):
        super().__init__(root, text=text, bootstyle=bootstyle, state=state, command=self.click)
        self.pack(pady=20)
        self.name = name
        self.display = text
        self.root = root    # nav
        self.win = root.win
    
    def click(self):
        '''
        click event
        '''
        print("click", self.name)
        self.root.btn_active.config(state=NORMAL, bootstyle=(PRIMARY, OUTLINE))
        self.root.btn_active = self
        self.config(state=ACTIVE, bootstyle=(PRIMARY, SOLID))

        self.root.frame_switch(self.name)

class Nav(ttk.Frame):
    '''
    left navigation bar
    '''
    name="nav"
    root = None
    win = None

    btn_active = None

    # children:
    btns = {
        "home": None,
        "concat": None,
        "extract": None,
        "joinav": None,
        "convert": None,
        "m3u8": None,
    }
    
    def __init__(self, root, win):
        super().__init__(root)
        self.pack(side="left", padx=20, pady=20)
        self.root = root    # app
        self.win = win

        # buttons to choose action
        self.btns["home"] = NavBtn("home", self, text="欢迎使用", bootstyle=(PRIMARY, SOLID), state=ACTIVE)
        self.btn_active = self.btns["home"]
        self.btns["concat"] = NavBtn("concat", self, text="快速拼接", state=DISABLED)
        self.btns["extract"] = NavBtn("extract", self, text="快速截取", state=DISABLED)
        self.btns["joinav"] = NavBtn("joinav", self, text="合并音视频", state=DISABLED)
        self.btns["convert"] = NavBtn("convert", self, text="格式转换", state=DISABLED)
        self.btns["m3u8"] = NavBtn("m3u8", self, text="下载m3u8网络资源", state=DISABLED)
    
    def frame_switch(self, name:str):
        '''
        switch to another frame
        '''
        print("switch to", name)
        self.win.main.frame_switch(name)