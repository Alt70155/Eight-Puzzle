import tkinter as tk
import random
from tkinter import messagebox

def create_list(list):
    tmp_list = []
    zero_ary = [-1] * 5
    ct = 0
    for i in range(0, 5):
        x = []
        if i == 0 or i == 4:
            tmp_list.append(zero_ary)
        else:
            for j in range(0, 5):
                if j == 0 or j == 4 or ct == 9:
                    x.append(-1)
                else:
                    x.append(list[ct])
                    ct += 1
            tmp_list.append(x)
    return tmp_list

def disp():
    # for a in random_list: print(*a)
    for i in range(1,4):
        for j in range(1,4):
            print(random_list[i][j], end='')
        print()

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
    coor = search_index(label)
    x, y = coor[0], coor[1]
    bool = False
    for i in [-1, 1]:
        if random_list[x][y+i] == 0 or random_list[x+i][y] == 0:
            bool = True

    zero_coor = search_index(0)
    zero_x, zero_y = zero_coor[0], zero_coor[1]
    if bool:
        tmp = random_list[x][y]
        random_list[zero_x][zero_y] = tmp
        random_list[x][y] = 0
        # 表示入れ替え
        create_flame(random_list)
        if random_list == correct_list:
            print('claer')
            close()
    else:
        print('no change')

# 管理用配列作成
first_list = [1,2,3,4,5,6,7,8,0]
correct_list = create_list(first_list)
# random_list  = create_list(random.sample(first_list, len(first_list)))
random_list = create_list([1,2,3,4,5,6,7,0,8])
# ウィンドウ生成
root = tk.Tk()
root.title('8パズル')
root.geometry('300x300')
flame = tk.LabelFrame(root) # フレーム生成
create_flame(random_list)

flame.pack(side = 'top')
root.mainloop()
