from tkinter import *
from tkinter import ttk
import time


TIME = 0

def tick():
    global TIME
    h = 0
    m = TIME // 60
    s = TIME % 60
    now = '0{}:{}:{}'.format(h, m, s)
    clock.configure(text=now)
    TIME -= 1
    root.after(1000, tick)


def five_minutes():
    global TIME
    TIME = 300
    h = 0
    m = TIME // 60
    s = 0
    clock.configure(text='0{}:0{}:0{}'.format(h, m, s))


def ten_minutes():
    global TIME
    TIME = 600
    h = 0
    m = TIME // 60
    s = 0
    clock.configure(text='0{}:{}:0{}'.format(h, m, s))


def fifteen_minutes():
    global TIME
    TIME = 900
    h = 0
    m = TIME // 60
    s = 0
    clock.configure(text='0{}:{}:0{}'.format(h, m, s))


def stop():
    root.after(0, stop)

root = Tk()
root.title('Timer')
root.geometry('160x100')
clock = ttk.Label(root, text="00:00:00", font='Arial 40')
clock.grid(columnspan=4, row=1)
# time
five = ttk.Button(root, text='5', width=2, command=five_minutes)
five.grid(column=0, row=2)
ten = ttk.Button(root, text='10', width=2, command=ten_minutes)
ten.grid(column=1, row=2)
fifteen = ttk.Button(root, text='15', width=2, command=fifteen_minutes)
fifteen.grid(column=2, row=2)

start = ttk.Button(root, width=10, text='Start', command=tick)
start.grid(column=0, columnspan=3, row=4)

root.mainloop()