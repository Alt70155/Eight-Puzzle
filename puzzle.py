import tkinter as tk
import random
from tkinter import messagebox

def create_list(list):
    outside_list = [-1] * 5
    tmp_list = [outside_list]
    ct = -1
    for i in range(1, 4):
        tmp_list.append([ -1 if j == 0 or j == 4 else list[j+ct] for j in range(0, 5)])
        ct += 3
    tmp_list.append(outside_list)
    return tmp_list

def search_index(search_num):
    for i in range(1,4):
        if search_num in random_list[i]:
            return i, random_list[i].index(search_num)

def create_flame(list):
    ct = 0
    for i in range(1,4):
        for j in range(1,4):
            label = tk.Label(flame, text = list[i][j])
            label.bind('<1>', judge)
            label.grid(column = ct % 3, row = ct // 3, padx = 30, pady = 30)
            ct+=1

def close():
    messagebox.showinfo('ゲームクリア', message='ゲームクリア！\n終了します')
    root.destroy()

def judge(event):
    label = event.widget['text'] # クリックされたラベル名を取得
    coor = search_index(label)   # ラベルの座標を取得
    x, y = coor[0], coor[1]
    bool = False
    for i in [-1, 1]:
        if random_list[x][y+i] == 0 or random_list[x+i][y] == 0:
            bool = True

    zero_coor = search_index(0)
    zero_x, zero_y = zero_coor[0], zero_coor[1]
    if bool:
        # swap
        random_list[x][y], random_list[zero_x][zero_y] = random_list[zero_x][zero_y], random_list[x][y]
        # 表示更新
        create_flame(random_list)
        if random_list == correct_list:
            print('claer')
            close()
    else:
        print('no change')

# 管理用配列作成
first_list = list(range(1,9))
first_list.append(0)
correct_list = create_list(first_list)
# random_list = create_list([1,2,3,4,5,6,7,0,8])
random_list  = create_list(random.sample(first_list, len(first_list)))

# ウィンドウ生成
root = tk.Tk()
root.title('8パズル')
root.geometry('250x250')
flame = tk.LabelFrame(root) # フレーム生成
create_flame(random_list)

flame.pack(side = 'top')
root.mainloop()
