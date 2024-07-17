import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess
import platform
import re
import functions as F
import styles as S
import ui, nav, main

class SepV(ttk.Separator):
    '''
    vertical separator
    '''
    name="sepv"
    root = None
    win = None
    
    def __init__(self, root, win):
        super().__init__(root, orient="vertical")
        self.pack(side="left", fill="both", pady=40)
        self.root = root    # app
        self.win = win

class BtnOk(ttk.Button):
    '''
    ok button
    '''
    name="btnok"
    display="确认"
    root = None
    win = None
    
    def __init__(self, root, command):
        super().__init__(root, text=self.display, bootstyle=(PRIMARY, OUTLINE), command=command)
        self.pack(pady=20)
        self.root = root
        self.win = root.win