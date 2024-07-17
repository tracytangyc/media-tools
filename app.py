from tkinter import *
from tkinter import ttk
import functions as f

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
if __name__ == "__main__":
    win_root = Tk()
    setup(win_root)
    win_root.mainloop()

