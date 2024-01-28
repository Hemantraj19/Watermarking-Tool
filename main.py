import tkinter
from tkinter import *
from watermark_form import Form
from perform_functions import PerformFunctions

window = Tk()
window.config(padx=5, pady=5, background="black")
window.geometry("1200x600")
perform_functions = PerformFunctions()
canvas = Canvas(width=780, height=550)
logo = PhotoImage(file="demo.png")
image = canvas.create_image(0, 0, anchor=tkinter.NW, image=logo)
canvas.grid(row=0, column=0, rowspan=10, padx=20, pady=20)


def bind_for_change_text_color():
    color = form.color
    perform_functions.change_text_color(canvas, color)


form = Form(change_text_color_callback=bind_for_change_text_color)


def bind_for_get_text_over_image():
    perform_functions.get_text_over_image(form, canvas)


def bind_for_get_img():
    perform_functions.get_img(canvas, image)


def bind_for_change_font(event):
    font = form.font_entry.get()
    font_size = form.font_size_entry.get()
    perform_functions.change_text_font(canvas, font, int(font_size))


def bind_for_opacity():
    opacity = int(form.opacity_entry.get())
    perform_functions.change_opacity(canvas, opacity)


def bind_for_move_up():
    perform_functions.move_up(canvas)


def bind_for_move_down():
    perform_functions.move_down(canvas)


def bind_for_move_left():
    perform_functions.move_left(canvas)


def bind_for_move_right():
    perform_functions.move_right(canvas)


def bind_for_rotate_text():
    angle = form.degree_entry.get()
    perform_functions.rotate_text(canvas, angle)


def bind_for_save_img():
    perform_functions.save_image(canvas)


def make_form():
    form.text_label()
    form.text_entry()
    form.show()
    form.color_picker_label()
    form.place_opacity_fields(window)
    form.choose_color_button()
    form.place_move_up_button()
    form.place_move_left_button()
    form.place_move_right_button()
    form.place_move_down_button()
    form.place_degree_contents()
    form.show_font_entry(window)
    form.show_font_size_entry(window)
    form.upload_picture_button()
    form.save_picture_button()
    form.show_button.config(command=bind_for_get_text_over_image)
    form.upload_button.config(command=bind_for_get_img)
    form.opacity_button.config(command=bind_for_opacity)
    form.move_up_button.config(command=bind_for_move_up)
    form.move_down_button.config(command=bind_for_move_down)
    form.move_left_button.config(command=bind_for_move_left)
    form.move_right_button.config(command=bind_for_move_right)
    form.degree_button.config(command=bind_for_rotate_text)
    form.save_button.config(command=bind_for_save_img)
    form.font_entry.bind("<<ComboboxSelected>>", bind_for_change_font)
    form.font_size_entry.bind("<<ComboboxSelected>>", bind_for_change_font)


make_form()
window.mainloop()
