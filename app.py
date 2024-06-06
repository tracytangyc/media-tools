from tkinter import *
from tkinter import ttk
import functions as f

root = Tk()
root.title("音视频处理小工具  Media Tools")
root.geometry("800x600")


## UPPER HALF:

label_welcome = ttk.Label(root, text="欢迎使用音视频处理小工具  Media Tools",)
label_welcome.pack(pady=20)

# buttons to choose action
btn_action_concat = ttk.Button(root, text="拼接")
btn_action_convert = ttk.Button(root, text="转换格式")
btn_action_extract = ttk.Button(root, text="截取")
btn_action_join_audio_video = ttk.Button(root, text="合并音视频")
btn_action_m3u8 = ttk.Button(root, text="下载m3u8格式的网络资源")


## LOWER HALF:

frame = ttk.Frame(root)
frame['padding'] = (20, 20)

### concat

### convert

### extract
label_starttime = ttk.Label(root, text="开始时间(HH:MM:SS)：")
label_starttime.pack(pady=20)
sv_starttime = StringVar()
entry_starttime = ttk.Entry(root, textvariable=sv_starttime, validate='key', validatecommand='f.re_hhmmss', width=20)
entry_starttime.pack(pady=20)

label_endtime = ttk.Label(root, text="结束时间(HH:MM:SS)：")
label_endtime.pack(pady=20)
sv_endtime = StringVar()
entry_endtime = ttk.Entry(root, textvariable=sv_endtime, validate='key', validatecommand='f.re_hhmmss', width=20)
entry_endtime.pack(pady=20)

def update_duration():
    starttime = f.str_to_seconds(sv_starttime.get())
    endtime = f.str_to_seconds(sv_endtime.get())
    sv_duration.set(f.seconds_to_str(endtime - starttime))
    label_duration.config(text="目标时长："+ str(sv_duration))

button_confirm = ttk.Button(root, text="确认", command=update_duration)
button_confirm.pack(pady=10)
button_confirm.state(f.btn_state)

sv_duration = StringVar()
label_duration = ttk.Label(root, text="目标时长：")
label_duration.pack(pady=20)

### join_audio_video

### m3u8


# MAIN LOOP
root.mainloop()