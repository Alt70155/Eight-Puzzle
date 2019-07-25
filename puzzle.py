import tkinter as tk
import random
from tkinter import messagebox

# 配列を二次元配列に分割する関数
# rangeの第三引数はstep, nは0,3,9となり、idx:idx+nは0~3,3~6,6~9となる
split_list = lambda l, n: [l[idx:idx + n] for idx in range(0, len(l), n)]

def create_screen(list, image_list, puzzle_flame):
    ct = 0
    for i in range(0, 3):
        for j in range(0, 3):
            index = list[i][j]
            label = tk.Label(puzzle_flame, text = index, image = image_list[index])
            label.bind('<1>', judge) # judge関数を登録
            label.grid(column = ct % 3, row = ct // 3, padx = 30, pady = 30)
            ct += 1

# タイルが押されるとこの関数が実行される
def judge(e):
    global hand_ct

    y, x = search_index(e.widget['text']) # クリックされた数字の座標を取得

    if is_exist_zero(y, x): # 選択された数字の上下左右にゼロがあるか調べる

        hand_ct -= 1
        hand_ct_label.configure(text='残り手数:\n' + str(hand_ct))

        zero_y, zero_x = search_index(0) # ゼロの座標を取得
        # ゼロと選択された数字を入れ替え
        random_list[y][x], random_list[zero_y][zero_x] = random_list[zero_y][zero_x], random_list[y][x]
        create_screen(random_list, image_list, puzzle_flame) # 表示更新

        if random_list == correct_list: close('ゲームクリア！\n終了します')

        elif hand_ct == 0: close('手数をオーバーしました！\n終了します')

def restart(e):
    global random_list, hand_ct

    hand_ct = 30
    hand_ct_label.configure(text='残り手数:\n' + str(hand_ct))
    random_list = split_list(tmp_list, 3)
    create_screen(random_list, image_list, puzzle_flame)

def search_index(search_num):
    # index関数は検索した数字が無い場合例外が発生するため、
    # in演算子で存在を予め調べ、合った場合のみindex関数を使う
    for i, inner_ary in enumerate(random_list):
        if search_num in inner_ary:
            # それぞれ二次元配列のy,x座標になる
            return i, inner_ary.index(search_num)

def is_exist_zero(y, x):

    for i in [-1, 1]:
        yi, xi = y + i, x + i
        # ・配列の範囲内か・上下左右にゼロがあるかを調べる
        if -1 < xi < 3 and random_list[y][xi] == 0 \
           or -1 < yi < 3 and random_list[yi][x] == 0:
            return True
    return False

def close(msg):
    messagebox.showinfo('インフォメーション', message = msg)
    root.destroy()

# 状態管理用配列作成
first_list   = [0 if i == 9 else i for i in range(1, 10)]
correct_list = split_list(first_list, 3) # 3分割
# random_list  = split_list(random.sample(first_list, len(first_list)), 3)
tmp_list     = [1,2,3,4,5,6,7,0,8]
random_list  = split_list(tmp_list, 3) # デバッグ用
RESTART_LIST = split_list(tmp_list, 3)
hand_ct      = 30
elapsed_time = 0

# root area
root = tk.Tk()
root.title('8パズル')
root.geometry('1000x1000')
# パズルに使う画像を読み込んで、それらを配列に格納
image_list = list(map(lambda i: tk.PhotoImage(file='image/{0}.png'.format(i)), list(range(0,9))))

# ----- flame area -----
puzzle_flame       = tk.LabelFrame(root)
left_bar_flame     = tk.LabelFrame(root)
hand_ct_flame      = tk.LabelFrame(left_bar_flame)
elapsed_time_flame = tk.LabelFrame(left_bar_flame)
right_bar_flame    = tk.LabelFrame(root)
restart_flame      = tk.LabelFrame(right_bar_flame)

# ----- label area -----
hand_ct_label      = tk.Label(hand_ct_flame,      text = '残り手数:\n' + str(hand_ct))
elapsed_time_label = tk.Label(elapsed_time_flame, text = '経過時間:\n' + str(elapsed_time))

create_screen(random_list, image_list, puzzle_flame) # フレームと配列を使ってスクリーンを生成

restart_button = tk.Button(restart_flame, text = 'やり直し')
restart_button.bind('<1>', restart)

# ----- pack area -----
hand_ct_label.pack()
elapsed_time_label.pack()
restart_button.pack()

# 書く順番によって表示が変わるので注意
right_bar_flame.pack(side = 'right', padx = 40, pady = 10)
left_bar_flame.pack(side = 'left',   padx = 50, pady = 10)
puzzle_flame.pack(side = 'top',      padx = 30, pady = 40)

hand_ct_flame.pack(padx = 10, pady = 10)
elapsed_time_flame.pack(padx = 10, pady = 10)
restart_flame.pack(padx = 20, pady = 20)

root.mainloop()
