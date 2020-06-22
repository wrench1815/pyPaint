""" 
Author : Hardeep Kumar
Created On : Sat Jun 20 2020
File : main.py
"""
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("pyPaint")
root.geometry("800x650")


def draw(e):
    # Brush Parameters
    brush_colour = 'green'
    brush_size = 20
    # Types Available:- BUTT, ROUND, PROJECTING
    brush_type = ROUND

    # Starting Axis
    x1, y1 = e.x - 1, e.y - 1
    # Stopping Axis
    x2, y2 = e.x + 1, e.y + 1
    # Draw on Canvas
    root_canvas.create_line(x1,
                            y1,
                            x2,
                            y2,
                            fill=brush_colour,
                            width=brush_size,
                            capstyle=brush_type,
                            smooth=True)


def change_brush_size(pos_return):
    brush_size_slider_label.config(text=int(brush_size_slider.get()))


wt = 600
ht = 400

root_canvas = Canvas(root, width=wt, height=ht, bg="white")
root_canvas.pack(pady=20)

root_canvas.bind('<B1-Motion>', draw)

# Brush Options Frame
brush_options_frame = Frame(root, bg="white")
brush_options_frame.pack(pady=20)

# Brush Size
brush_size_frame = LabelFrame(brush_options_frame, text="Brush Size")
brush_size_frame.grid(row=0, column=0, padx=50)

# Size Slider
brush_size_slider = ttk.Scale(brush_size_frame,
                              from_=1,
                              to=100,
                              command=change_brush_size,
                              orient=VERTICAL,
                              value=20)
brush_size_slider.pack(pady=10, padx=10)

# Brush Size Slider Label
brush_size_slider_label = Label(brush_size_frame, text=brush_size_slider.get())
brush_size_slider_label.pack(pady=5)

root.mainloop()
