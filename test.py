import tkinter as tk

# ウィンドウ生成
root = tk.Tk()
root.title('8パズル')
root.geometry('600x600')

main_flame = tk.LabelFrame(root) # フレーム生成
two_flame  = tk.LabelFrame(root) # フレーム生成

main_label    = tk.Label(main_flame, text = '残り手数:\n')
hand_ct_label = tk.Label(two_flame,  text = '残り手数:\n')

main_label.pack()
hand_ct_label.pack()

main_flame.pack(side = 'right', pady = 10)
two_flame.pack(side = 'left', padx = 50, pady = 10)

root.mainloop()
