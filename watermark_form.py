from tkinter import *
from tkinter.colorchooser import askcolor


class Form:
    def __init__(self):
        self.label = Label()
        self.entry = Entry()
        self.color_label = Label()
        self.color_button = Button()
        self.upload_button = Button()
        self.save_button = Button()
        self.show_button = Button()

    def text_label(self):
        self.label.config(text="Text", background="black", foreground="white")
        self.label.grid(row=0, column=1)

    def text_entry(self):
        self.entry.config(width=20, background="#45474B", foreground="white")
        self.entry.grid(row=0, column=2, padx=10)

    def show(self):
        self.show_button.config(text="Show", background="black", foreground="white")
        self.show_button.grid(row=0, column=3, padx=10)

    def color_picker_label(self):
        self.color_label.config(
            text="Color Picker", background="black", foreground="white"
        )
        self.color_label.grid(row=1, column=1, padx=30)

    def color_picker(self):
        color = askcolor(title="Choose color")
        print(color)

    def choose_color_button(self):
        self.color_button.config(
            text="Choose",
            command=self.color_picker,
            background="black",
            foreground="white",
        )
        self.color_button.grid(row=1, column=2, padx=10)

    def upload_picture_button(self):
        self.upload_button.config(text="Upload", background="black", foreground="white")
        self.upload_button.grid(row=2, column=1, padx=10)

    def save_picture_button(self):
        self.save_button.config(text="Save", background="black", foreground="white")
        self.save_button.grid(row=2, column=2, padx=10)
