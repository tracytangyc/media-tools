import tkinter as tk
from tkinter import ttk

label_starttime = ttk.Label(root, text="开始时间(HH:MM:SS)：")
label_starttime.pack(pady=20)
sv_starttime = tk.StringVar()
entry_starttime = ttk.Entry(root, textvariable=sv_starttime, validate='key', validatecommand='f.re_hhmmss', width=20)
entry_starttime.pack(pady=20)

label_endtime = ttk.Label(root, text="结束时间(HH:MM:SS)：")
label_endtime.pack(pady=20)
sv_endtime = tk.StringVar()
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

sv_duration = tk.StringVar()
label_duration = ttk.Label(root, text="目标时长：")
label_duration.pack(pady=20)
