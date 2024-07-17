import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess
import platform
import re
import functions as F
import styles as S
import app, main, ui

class Extract(tk.Frame):
    '''
    extract frame
    '''
    name = "extract"
    display = "快速截取"
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

        self.labels["starttime"] = ttk.Label(self, text="开始时间(HH:MM:SS)：")
        self.labels["starttime"].pack(pady=20)
        self.strvars["starttime"] = tk.StringVar()
        entry_starttime = ttk.Entry(self, textvariable=self.strvars["starttime"], validate='key', validatecommand='f.re_hhmmss', width=20)
        entry_starttime.pack(pady=20)

        self.labels["endtime"] = ttk.Label(self, text="结束时间(HH:MM:SS)：")
        self.labels["endtime"].pack(pady=20)
        self.strvars["endtime"] = tk.StringVar()
        entry_endtime = ttk.Entry(self, textvariable=self.strvars["endtime"], validate='key', validatecommand='f.re_hhmmss', width=20)
        entry_endtime.pack(pady=20)

        self.btns["confirm"] = ui.BtnOk(self, command=self.update_duration)
        self.btns["confirm"].pack(pady=10)
        self.btns["confirm"].state(F.btn_state)

        self.strvars["duration"] = tk.StringVar()
        self.labels["duration"] = ttk.Label(self, text="目标时长：")
        self.labels["duration"].pack(pady=20)

    def pack(self):
        super().pack(fill="x", expand=True, padx=20, pady=20)

    def pack_forget(self):
        super().pack_forget()
    
    def update_duration(self):
        starttime = F.str_to_seconds(self.strvars["starttime"].get())
        endtime = F.str_to_seconds(self.strvars["endtime"].get())
        self.strvars["duration"].set(F.seconds_to_str(endtime - starttime))
        self.labels["duration"].config(text="目标时长："+ str(self.strvars["duration"]))

