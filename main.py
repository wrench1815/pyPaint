""" 
Author : Hardeep Kumar
Created On : Sat Jun 20 2020
File : main.py
"""
from tkinter import *

root = Tk()
root.title("wrench1815's Paint Program")
root.geometry("800x650")

wt = 600
ht = 400

root_canvas = Canvas(root, width=wt, height=ht, bg="white")
root_canvas.pack(pady=20)

root.mainloop()