from tkinter import *
from tkinter import ttk
import time


def tick():
    now = time.strftime('%H:%M:%S')
    clock.configure(text=now)
    root.after(1000, tick)


def five_minutes():
    clock.configure(text='00:05:00')


def ten_minutes():
    clock.configure(text='00:10:00')


def fifteen_minutes():
    clock.configure(text='00:15:00')


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