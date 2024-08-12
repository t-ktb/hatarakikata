import tkinter as tk
from datetime import datetime
import os

def update_time():
    current_time = datetime.now()
    time_label.config(text=current_time.strftime("%Y-%m-%d %H:%M:%S"))
    check_time_and_display_message()
    root.after(1000, update_time)

def check_time_and_display_message():
    current_time = datetime.now()
    if 8 <= current_time.hour < 18:
        message_label.config(text="業務時間中です")
        lock_button.pack_forget()
        more_work_button.pack_forget()
        alternate_label.config(text="")
    else:
        message_label.config(text="業務時間外です")
        alternating_message()
        lock_button.pack()
        more_work_button.pack()

def alternating_message():
    global message_index
    if rest_message_active:
        return
    messages = ["そんな給料高ないぞ","天スタ食いにいけ","筋トレして寝ろ"]
    alternate_label.config(text=messages[message_index])
    message_index = (message_index + 1) % len(messages)
    root.after(300000, alternating_message)  # 5分ごとに更新

def lock_computer():
    os.system("rundll32.exe user32.dll, LockWorkStation")

def more_work():
    global rest_message_active
    rest_message_active = True
    alternate_label.config(text="せめてタバコ吸え")
    root.after(60000, reset_rest_message)  # 1分間表示

def reset_rest_message():
    global rest_message_active
    rest_message_active = False
    alternating_message()  # 5分ごとのメッセージに戻る

# メインウィンドウの設定
root = tk.Tk()
root.title("働き方改革")
root.geometry("400x300")

# 時刻表示用のラベル
time_label = tk.Label(root, text="", font=("Helvetica", 16))
time_label.pack(pady=10)

# 常に表示するメッセージ用のラベル
message_label = tk.Label(root, text="", font=("Helvetica", 16))
message_label.pack(pady=10)

# 交互に表示するメッセージ用のラベル
alternate_label = tk.Label(root, text="", font=("Helvetica", 16))
alternate_label.pack(pady=10)

# ロック用のボタン
lock_button = tk.Button(root, text="帰ります", command=lock_computer)
lock_button.pack_forget()

# 仕事を続けるためのボタン
more_work_button = tk.Button(root, text="もう少し仕事します", command=more_work)
more_work_button.pack_forget()

# 交互に表示するメッセージの初期化
message_index = 0
rest_message_active = False

# 時間チェックと時刻更新の開始
update_time()

# メインループの開始
root.mainloop()