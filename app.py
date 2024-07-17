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
btn_action_concat = ttk.Button(root, text="快速拼接")
btn_action_concat.pack(pady=20)
btn_action_extract = ttk.Button(root, text="快速截取")
btn_action_extract.pack(pady=20)
btn_action_join_audio_video = ttk.Button(root, text="合并音视频")
btn_action_join_audio_video.pack(pady=20)
btn_action_convert = ttk.Button(root, text="转换格式")
btn_action_convert.pack(pady=20)
btn_action_m3u8 = ttk.Button(root, text="下载m3u8网络资源")
btn_action_m3u8.pack(pady=20)


## LOWER HALF:

frame = ttk.Frame(root)
frame['padding'] = (20, 20)


# MAIN LOOP
root.mainloop()