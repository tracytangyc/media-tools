from tkinter import ttk

def setup():
    entry_starttime = ttk.Entry(root, width=20)
    entry_endtime = ttk.Entry(root, width=20)
    entry_starttime.pack(pady=20)
    entry_endtime.pack(pady=20)

    duration = entry_endtime - entry_starttime
    label_duration = ttk.Label(root, text="目标时长：{duration}")