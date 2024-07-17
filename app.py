import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess
import platform
import re

import functions as F

class App(tk.Tk):
    name = "app"
    display = "音视频处理小工具"
    root = None
    win = None
    style = None
    OS = ""

    # children:
    nav = None
    sep_v = None
    main = None

    def __init__(self):
        super().__init__()
        self.title("音视频处理小工具  Media Tools")
        self.geometry("960x540")

        # check the operating system
        self.OS = platform.system()  # 'Linux', 'Darwin' (macOS), 'Java', 'Windows'
        print(self.OS)

        import styles as S
        self.style = ttk.Style()
        self.style.configure("TButton", font=S.P, fill="both", expand=True)
        self.style.configure("TLabel", font=S.P)

        import ui, nav, main
        self.nav = nav.Nav(self, self)
        self.sep_v = ui.SepV(self, self)
        self.main = main.Main(self, self)
        self.mainloop()

