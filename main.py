import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess
import platform
import re
import functions as F
import styles as S
import app

import home, concat, extract, joinav, convert, m3u8

class Main(tk.Frame):
    '''
    main frame
    '''
    name = "main"
    root = None
    win = None

    active_frame = None

    # children:
    frames = {
        "home": None,
        "concat": None,
        "extract": None,
        "joinav": None,
        "convert": None,
    }
    
    def __init__(self, root, win):
        super().__init__(root)
        self.pack(side="right")
        self.root = root    # app
        self.win = win

        # always open home frame when main is created
        self.frames["home"] = home.Home(self, win)
        self.active_frame = self.frames["home"]
        self.frames["concat"] = concat.Concat(self, win)
        self.frames["extract"] = extract.Extract(self, win)
        self.frames["joinav"] = joinav.JoinAV(self, win)
        self.frames["convert"] = convert.Convert(self, win)
        self.frames["m3u8"] = m3u8.M3U8(self, win)
    
    def frame_switch(self, name:str):
        '''
        switch frame
        '''
        print("switch frame", name)

        # hide all frames
        for frame in self.frames.values():
            if frame is not None:
                frame.pack_forget()
        
        self.frames[name].pack()
        self.active_frame = self.frames[name]