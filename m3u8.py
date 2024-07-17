import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess
import platform
import re
import functions as F
import styles as S
import app, main, ui

class M3U8(tk.Frame):
    '''
    m3u8 frame
    '''
    name = "m3u8"
    display = "下载m3u8网络资源"
    root = None
    win = None

    # children:
    btns = {
        "confirm": None
    }
    labels = {}
    strvars = {}

    def __init__(self, root, win):
        super().__init__(root)
        self.pack()
        self.root = root    # main
        self.win = win
    
    def pack(self):
        super().pack(fill="x", expand=True, padx=20, pady=20)