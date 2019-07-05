import tkinter as tk
import random
from tkinter import messagebox

correct_list = list(range(1,9))
correct_list.append(0)
# list = random.sample(correct_list, len(correct_list))
list = [1,2,3,4,5,6,7,0,8]

def count_column(list):
    ct = 1
    list_len = len(list)
    while True:
        if list_len // ct == ct:
            break
        else:
            ct += 1
    return ct

def judge(event):
    label = event.widget['text'] # クリックされたラベル名を取得
    index = list.index(label) # 入力された値を配列から探し、添字を返す
    bool = False
    ct = count_column(list)
    # 4角判定
    if index == 0:
        if list[index+1] == 0 or list[index+ct] == 0:
            bool = True
    elif index == ct - 1:
        if list[index-1] == 0 or list[index+ct] == 0:
            bool = True
    elif index == len(list) - 1:
        if list[index-1] == 0 or list[index-ct] == 0:
            bool = True
    elif index == len(list) - ct:
        if list[index+1] == 0 or list[index-ct] == 0:
            bool = True
    # ４角以外の辺
    elif index % ct == 0:
        # 左辺
        if list[index+1] == 0 or list[index-ct] == 0 or list[index+ct] == 0:
            bool = True
    elif index // ct == 0:
        # 上辺
        if list[index+1] == 0 or list[index-1] == 0 or list[index+ct] == 0:
            bool = True
    elif index // ct == ct - 1:
        # 底辺
        if list[index+1] == 0 or list[index-1] == 0 or list[index-ct] == 0:
            bool = True
    elif index % ct == ct - 1:
        # 右辺
        if list[index-1] == 0 or list[index-ct] == 0 or list[index+ct] == 0:
            bool = True
    else:
        # 内側全て
        if (list[index-1] == 0 or
            list[index+1] == 0 or
            list[index-ct] == 0 or
            list[index+ct] == 0):
            bool = True
    swap(list, bool, index)

def close():
    messagebox.showinfo('ゲームクリア', message='終了します')
    root.destroy()

def swap(list, bool, index):
    zero_index = list.index(0)
    if bool:
        # 配列入れ替え
        tmp = list[index]
        list[zero_index] = tmp
        list[index] = 0
        # 表示入れ替え
        create_flame(list)
        if list == correct_list:
            print('claer')
            close()
    else:
        print('no change')

def create_flame(list):
    for i in range(0, 9):
        label = tk.Label(flame, text = list[i])
        label.bind('<1>', judge)
        label.grid(column = i % 3, row = i // 3, padx = 30, pady = 30)

# ウィンドウ生成
root = tk.Tk()
root.title('クリックイベント練習')
root.geometry('300x300')
flame = tk.LabelFrame(root) # フレーム生成
create_flame(list)

flame.pack(side = 'top')
root.mainloop()
