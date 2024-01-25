import tkinter
from tkinter import *
from watermark_form import Form
from perform_functions import PerformFunctions

window = Tk()
window.config(padx=5, pady=5, background="black")
form = Form()
perform_functions = PerformFunctions()
canvas = Canvas(width=780, height=550)
logo = PhotoImage(file="demo.png")
image = canvas.create_image(0, 0, anchor=tkinter.NW, image=logo)
canvas.grid(row=0, column=0, rowspan=3, padx=20, pady=20)


def get_img():
    new_image = perform_functions.upload()

    # Set a maximum canvas size
    max_canvas_width = 950
    max_canvas_height = 650

    # Resize the canvas if the image dimensions exceed the maximum
    if new_image.width() > max_canvas_width or new_image.height() > max_canvas_height:
        # new_image = new_image.resize((max_canvas_width, max_canvas_height))
        canvas.config(width=max_canvas_width, height=max_canvas_height)
    else:
        canvas.config(width=new_image.width(), height=new_image.height())

    canvas.itemconfig(image, image=new_image)


def get_text():
    text = form.entry.get()


def make_form():
    form.text_label()
    form.text_entry()
    form.show()
    form.show_button.config(command=get_text)
    form.color_picker_label()
    form.choose_color_button()
    form.upload_picture_button()
    form.upload_button.config(command=get_img)
    form.save_picture_button()


# def display_image():
#     canvas = Canvas()


make_form()
window.mainloop()
