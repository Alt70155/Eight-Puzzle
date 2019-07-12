import tkinter as tk

def click(e):
    print(e.widget['text'])

root = tk.Tk()
root.geometry('200x200')
flm = tk.LabelFrame(root)

img = tk.PhotoImage(file = './image/1.png')

label = tk.Label(flame, text = 1, image = img)
label.grid(column = 0, row = 0)
label.bind('<1>', click)
