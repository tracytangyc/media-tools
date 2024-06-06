from tkinter import *
from tkinter import ttk
import subprocess

root = Tk()
root.title("音视频处理小工具  Media Tools")
root.geometry("800x600")

label = ttk.Label(root, text="欢迎使用音视频处理小工具  Media Tools",)
label.pack(pady=20)

def run_action(action_type,**kwargs):
    cmd = "{action_type}.sh " + " ".join(value for key, value in kwargs.items())

    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderrr=subprocess.PIPE, text=True)
        print(result.stdout)
    except:
        print("Error:", e.stderr)


# buttons to choose action
btn_action_concat = ttk.Button(root, text="拼接")
btn_action_convert = ttk.Button(root, text="转换格式")
btn_action_extract = ttk.Button(root, text="截取")
btn_action_join_audio_video = ttk.Button(root, text="合并音视频")
btn_action_m3u8 = ttk.Button(root, text="下载m3u8格式的网络资源")

### concat

### convert

### extract
entry_starttime = ttk.Entry(root, width=20)
entry_endtime = ttk.Entry(root, width=20)
entry.pack(pady=20)

duration = entry_endtime - entry_starttime
label_duration = ttk.Label(root, text="目标时长：{duration}")

### join_audio_video

### m3u8


# MAIN LOOP
root.mainloop()