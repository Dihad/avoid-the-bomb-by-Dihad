#moduels
import random
from tkinter import*
import ttkbootstrap as ttk
import tkinter as tk
#window set up
window = ttk.Window(themename = 'darkly')
window.title('avoid the bomb ')
window.geometry('800x600')
#vareables
nums_list = ["0","1","1","1","1","1","1","1","1"]
num_count = 0
#main funtion
def press():
    global nums_list
    global num_count
    num = random.choice(nums_list)
    if num == "0":
        bomb_label.config(text="bomb was\nthere")
        nums_list = ["0","1","1","1","1","1","1","1","1"]
        num_count =0
        num_label.config(text=num_count)
        b1.config(text="cheak")
        b2.config(text="cheak")
        b3.config(text="cheak")
        b4.config(text="cheak")
        b5.config(text="cheak")
        b6.config(text="cheak")
        b7.config(text="cheak")
        b8.config(text="cheak")
        b9.config(text="cheak")
        b1.config(state=tk.NORMAL)
        b2.config(state=tk.NORMAL)
        b3.config(state=tk.NORMAL)
        b4.config(state=tk.NORMAL)
        b5.config(state=tk.NORMAL)
        b6.config(state=tk.NORMAL)
        b7.config(state=tk.NORMAL)
        b8.config(state=tk.NORMAL)
        b9.config(state=tk.NORMAL)
    if num =="1":
        bomb_label.config(text="no bomb\n was there")
        nums_list.pop()
        nums_list.insert(0,"0")
        num_count = num_count+1
        num_label.config(text=num_count)
    if num_count == 8:
        bomb_label.config(text="all bomb\n found")
        b1.config(state=tk.DISABLED)
        b2.config(state=tk.DISABLED)
        b3.config(state=tk.DISABLED)
        b4.config(state=tk.DISABLED)
        b5.config(state=tk.DISABLED)
        b6.config(state=tk.DISABLED)
        b7.config(state=tk.DISABLED)
        b8.config(state=tk.DISABLED)
        b9.config(state=tk.DISABLED)
def p1():
    b1.config(text="cheaked")
    b1.config(state=tk.DISABLED)
    press()
def p2():
    b2.config(text="cheaked")
    b2.config(state=tk.DISABLED)
    press()
def p3():
    b3.config(text="cheaked")
    b3.config(state=tk.DISABLED)
    press()
def p4():
    b4.config(text="cheaked")
    b4.config(state=tk.DISABLED)
    press()
def p5():
    b5.config(text="cheaked")
    b5.config(state=tk.DISABLED)
    press()
def p6():
    b6.config(text="cheaked")
    b6.config(state=tk.DISABLED)
    press()
def p7():
    b7.config(text="cheaked")
    b7.config(state=tk.DISABLED)
    press()
def p8():
    b8.config(text="cheaked")
    b8.config(state=tk.DISABLED)
    press()
def p9():
    b9.config(text="cheaked")
    b9.config(state=tk.DISABLED)
    press()
#buttons and labels
bomb_label = Label(window, text="click to \n cheak bomb",font="Arial 20") 
num_label =     Label(window, text="0",font="Arial 40") 
count_label = Label(window, text="area\nclear",font="Arial 20") 
b1 = Button(window, text="cheak",command=p1)
b2 = Button(window, text="cheak",command=p2)
b3 = Button(window, text="cheak",command=p3)
b4 = Button(window, text="cheak",command=p4)
b5 = Button(window, text="cheak",command=p5)
b6 = Button(window, text="cheak",command=p6)
b7 = Button(window, text="cheak",command=p7)
b8 = Button(window, text="cheak",command=p8)
b9 = Button(window, text="cheak",command=p9)
#row and column
window.rowconfigure((0,1,2), weight = 1, uniform = 'a')
window.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
#placeing and grid
b1.grid(row =0,column=1,sticky = 'nsew')
b2.grid(row =0,column=2,sticky = 'nsew')
b3.grid(row =0,column=3,sticky = 'nsew')
b4.grid(row =1,column=1,sticky = 'nsew')
b5.grid(row =1,column=2,sticky = 'nsew')
b6.grid(row =1,column=3,sticky = 'nsew')
b7.grid(row =2,column=1,sticky = 'nsew')
b8.grid(row =2,column=2,sticky = 'nsew')
b9.grid(row =2,column=3,sticky = 'nsew')
bomb_label.place(x=10,y=20)
num_label.place(x=150,y=140)
count_label.place(x = 10,y=140)
#mainloop
window.mainloop()