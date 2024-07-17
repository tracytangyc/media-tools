from tkinter import *
import subprocess
import re

btn_state = ['!disabled']

def run_action(action_type,**kwargs):
    cmd = "{action_type}.sh " + " ".join(value for key, value in kwargs.items())

    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderrr=subprocess.PIPE, text=True)
        print(result.stdout)
    except Exception as e:
        print("Error:", e.stderr)

def re_hhmmss(input):
    print(">>>", input)
    pattern = r'^([01]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])$'
    if re.match(pattern, input) is not None:
        btn_state = ['!disabled']
        return True
    else:
        btn_state = ['disabled']
        return False

def str_to_seconds(time_str):
    if re_hhmmss(time_str) is False:
        return 0
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def seconds_to_str(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"