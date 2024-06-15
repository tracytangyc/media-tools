from tkinter import *
from tkinter import ttk
import subprocess

from components import concat as concat, convert as convert, extract as extract, join_audio_video as joinav, m3u8 as m3u8


def setup(root:Tk):
    root.title("音视频处理小工具  Media Tools")
    root.geometry("960x540")

    label_welcome = ttk.Label(root, text="欢迎使用音视频处理小工具  Media Tools",)
    label_welcome.pack(pady=20)

    # buttons to choose action
    btn_action_concat = ttk.Button(root, text="快速拼接", command=concat.setup)
    btn_action_extract = ttk.Button(root, text="快速截取", command=extract.setup)
    btn_action_joinav = ttk.Button(root, text="合并音频视频", command=joinav.setup)
    btn_action_convert = ttk.Button(root, text="格式转换", command=convert.setup)
    btn_action_m3u8 = ttk.Button(root, text="下载m3u8网络资源", command=m3u8.setup)


def run_action(action_type,**kwargs):
    cmd = "{action_type}.sh " + " ".join(value for key, value in kwargs.items())

    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderrr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)


# MAIN LOOP
if __name__ == "__main__":
    win_root = Tk()
    setup(win_root)
    win_root.mainloop()

