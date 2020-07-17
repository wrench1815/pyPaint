""" 
Author : Hardeep Kumar
Created On : Sat Jun 20 2020
File : main.py
"""

from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser as cs
from tkinter import filedialog as fd
from tkinter import messagebox
import os
from PIL import Image, ImageDraw, ImageGrab, ImageTk
import PIL

root = Tk()
root.title("pyPaint")
root.minsize(800, 700)
# root.geometry('800x700')

brush_color = "black"


def draw(e):
    # Brush Parameters
    brush_size = int(brush_size_slider.get())

    # Starting Axis
    x1, y1 = e.x - 1, e.y - 1
    # Stopping Axis
    x2, y2 = e.x + 1, e.y + 1
    # Draw on Canvas
    root_canvas.create_line(x1,
                            y1,
                            x2,
                            y2,
                            fill=brush_color,
                            width=brush_size,
                            capstyle=brush_type.get(),
                            smooth=True)


# function changes brush width using Slider values
def change_brush_size(pos_return):
    brush_size_slider_label.config(text=int(brush_size_slider.get()))


# Change Brush Color
def change_brush_color():
    global brush_color
    brush_color = "black"
    brush_color = cs.askcolor(color=brush_color)[1]


# Change Canvas Color
def change_canvas_color():
    canvas_color = "black"
    canvas_color = cs.askcolor(color=canvas_color)[1]
    root_canvas.config(bg=canvas_color)


#  Clear Screen
def clear_screen():
    root_canvas.delete(ALL)
    root_canvas.config(bg="white")


#  Save to png
def save_to_png():
    picture = fd.asksaveasfilename(initialdir=os.getcwd(),
                                   filetypes=(("png files", "*.png"),
                                              ("all files", "*.*")))
    if picture.endswith('.png'):
        pass
    else:
        picture = picture + '.png'

    if picture:
        x = root.winfo_rootx() + root_canvas.winfo_x()
        y = root.winfo_rooty() + root_canvas.winfo_y()
        x1 = x + root_canvas.winfo_width()
        y1 = y + root_canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(picture)

        # Sucess Box
        messagebox.showinfo("Image Saved", "Image Saved Successfully")


# Exit pyPaint
def exit_pyPaint():
    root.quit()


root_canvas = Canvas(root,
                     width=root.winfo_reqwidth(),
                     height=root.winfo_reqheight(),
                     bg="white")
root_canvas.pack(fill=BOTH, expand=YES, pady=20)

# Bind draw action to left click + Drag
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

# Brush Type
brush_type_frame = LabelFrame(brush_options_frame,
                              text="Brush Type",
                              height=400)
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
brush_type.set("round")

# Brush Type Radios
brush_type_radio1 = Radiobutton(brush_type_frame,
                                text="Round",
                                variable=brush_type,
                                value="round")
brush_type_radio2 = Radiobutton(brush_type_frame,
                                text="Slash",
                                variable=brush_type,
                                value="butt")
brush_type_radio3 = Radiobutton(brush_type_frame,
                                text="Diamond",
                                variable=brush_type,
                                value="projecting")
brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# Change Colors
# change_colors_frame = LabelFrame(brush_options_frame, text="Change Colors")
# change_colors_frame.grid(row=0, column=2)

# Change Brush Color Button
# brush_color_button = Button(change_colors_frame,
#                             text="Brush Color",
#                             command=change_brush_color)
# brush_color_button.pack(padx=10, pady=10)

# canvas_color_button = Button(change_colors_frame,
#                              text="Canvas Color",
#                              command=change_canvas_color)
# canvas_color_button.pack(padx=10, pady=10)

# # Program Options
# options_frame = LabelFrame(brush_options_frame, text="Program Options")
# options_frame.grid(row=0, column=3, padx=10)

# # Clear Screen
# clear_button = Button(options_frame, text="Clear Screen", command=clear_screen)
# clear_button.pack(padx=10, pady=10)

# # Save Image
# save_button = Button(options_frame, text="Save png", command=save_to_png)
# save_button.pack(padx=10, pady=10)

# Top Menu widget
option_menu = Menu(root)

# file menu
file_menu = Menu(option_menu)

# svae menu >>> start
file_menu.add_command(label='Save as png', command=save_to_png)
# save menu <<< end
# clear menu >>> start
file_menu.add_command(label='Clear', command=clear_screen)
# clear menu <<< end

# colors menu
color_menu = Menu(option_menu)

# canvas color menu >>> start
color_menu.add_command(label='Brush Color', command=change_brush_color)
# canvas color menu <<< stop

# brush color menu >>> start
color_menu.add_command(label='Canvas Color', command=change_canvas_color)
# brush color menu <<< stop

option_menu.add_cascade(label='File', menu=file_menu)
option_menu.add_cascade(label='Colors', menu=color_menu)
option_menu.add_command(label='Exit', command=exit_pyPaint)
root.config(menu=option_menu)

# starting point
root.mainloop()
""" testing code
menu = Menu(window) 
new_item = Menu(menu) 
new_item.add_command(label='New', command = clicked) 
menu.add_cascade(label='File', menu=new_item) 
window.config(menu=menu)
 """