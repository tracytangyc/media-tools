import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess
import platform
import re
import functions as F
import styles as S
import app, main

class Home(tk.Frame):
    '''
    home frame
    '''
    name = "home"
    display = "主页"
    root = None
    win = None

    # children:
    labels = {
        "welcome": None,
        "about": None,
        "ffmpeg": None,
    }

    def __init__(self, root, win):
        super().__init__(root)
        self.pack()
        self.root = root    # main
        self.win = win

        self.labels["welcome"] = ttk.Label(self, justify="center", text="欢迎使用音视频处理小工具  Media Tools", font=S.H1)
        self.labels["welcome"].pack(pady=20)

        self.labels["about"] = ttk.Label(self, justify="center", text="本工具使用Python编写，基于FFmpeg，提供音视频处理的常用功能。\n\n意见反馈：qingzaitracy@qq.com\n项目开源地址：https://www.github.com/tracytangyc/media-tools")
        self.labels["about"].pack(pady=20)

        # check if FFmpeg is installed
        try:
            result = subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        # result:
                        # ffmpeg version 2023-03-05-git-912ac82a3c-full_build-www.gyan.dev Copyright (c) 2000-2023 the FFmpeg developers
                        # built with gcc 12.2.0 (Rev10, Built by MSYS2 project)
                        # ...
            version = re.search(r"ffmpeg version (\d{4}-\d{2}-\d{2}-git-\w+)", result.stdout.decode()).group(1)
            print(version)
            self.labels["ffmpeg"] = ttk.Label(self, justify="center", text="FFmpeg已安装\n版本："+version)
            self.labels["ffmpeg"].pack(pady=20)

            # enable other buttons
            win.nav.btns["concat"].config(state=NORMAL)
            win.nav.btns["extract"].config(state=NORMAL)
            win.nav.btns["joinav"].config(state=NORMAL)
            win.nav.btns["convert"].config(state=NORMAL)
            win.nav.btns["m3u8"].config(state=NORMAL)
        except Exception as e:
            print(e)
            if self.labels["ffmpeg"] is not None:
                self.labels["ffmpeg"] = ttk.Label(self, justify="center", text="程序遇到错误：\n"+e.stderr)
                self.labels["ffmpeg"].pack(pady=20)
            else:
                self.labels["ffmpeg"] = ttk.Label(self, justify="center", text="FFmpeg未安装\n请参阅https://www.gihub.com/tractangyc/media-tools/README.md下载及安装FFmpeg，并重启本程序。")
                self.labels["ffmpeg"].pack(pady=20)
                                        # 失败原因："+e.stderr)
                # self.labels["ffmpeg"] = ttk.Label(win, text="FFmpeg未安装，正在尝试自动安装...")
                # try:
                #     cmd_ffmpeg = {
                #         "Linux": "sudo apt-get install ffmpeg",
                #         "Darwin": "brew install ffmpeg",
                #         "Windows": "choco install ffmpeg"
                #     }
                #     result = subprocess.run(cmd_ffmpeg[OS], shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                #     self.labels["ffmpeg"].config(text="FFmpeg安装成功")
                #     print(result.stdout)
                # except Exception as e:
                #     print("Error:", e.stderr)
    
    def pack(self):
        super().pack(fill="x", expand=True, padx=20, pady=20)
    
    def pack_forget(self):
        super().pack_forget()