from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from fonts_list import fonts


class Form:
    def __init__(self, change_text_color_callback):
        self.label = Label()
        self.entry = Entry()
        self.color_label = Label()
        self.color_button = Button()
        self.upload_button = Button()
        self.save_button = Button()
        self.show_button = Button()
        self.move_up_button = Button()
        self.move_down_button = Button()
        self.move_left_button = Button()
        self.move_right_button = Button()
        self.font_label = Label()
        self.font_entry = None
        self.font_size_label = Label()
        self.font_size_entry = None
        self.degree_label = Label()
        self.degree_entry = Entry()
        self.degree_button = Button()
        self.color = None
        self.change_text_color_callback = change_text_color_callback
        self.opacity = 1.0
        self.opacity_label = Label()
        self.opacity_entry = None
        self.opacity_button = Button()

    def text_label(self):
        self.label.config(text="Text:", background="black", foreground="white")
        self.label.grid(row=0, column=1, padx=5, sticky="w")

    def text_entry(self):
        self.entry.config(foreground="red")
        self.entry.grid(row=0, column=2, padx=10, sticky="w", columnspan=3)

    def show(self):
        self.show_button.config(text="Show", background="black", foreground="white")
        self.show_button.grid(
            row=0,
            column=4,
            columnspan=2,
            padx=10,
            sticky="we",
        )

    def show_font_entry(self, window):
        self.font_label.config(text="Font: ", background="black", foreground="white")
        self.font_entry = ttk.Combobox(window, values=fonts)
        self.font_entry.current(0)
        self.font_label.grid(row=1, column=1, sticky="nw", padx=5, pady=20)
        self.font_entry.grid(row=1, column=2, sticky="nw", columnspan=3, pady=20)

    def show_font_size_entry(self, window):
        self.font_size_label.config(
            text="Font Size:", background="black", foreground="white"
        )
        self.font_size_entry = ttk.Combobox(
            window, values=[str(i) for i in range(20, 90, 5)]
        )
        self.font_size_entry.current(0)
        self.font_size_label.grid(row=2, column=1, sticky="nw")
        self.font_size_entry.grid(row=2, column=1, sticky="ne", columnspan=3)

    def color_picker_label(self):
        self.color_label.config(
            text="Color Picker", background="black", foreground="white"
        )
        self.color_label.grid(row=3, column=1)

    def color_picker(self):
        self.color = askcolor(title="Choose color:")
        # print(self.color)
        if self.color:
            self.change_text_color_callback()

    def choose_color_button(self):
        self.color_button.config(
            text="Choose",
            command=self.color_picker,
            background="black",
            foreground="white",
        )
        self.color_button.grid(row=3, column=2, sticky="w")

    def place_opacity_fields(self, window):
        self.opacity_label.config(
            text="Opacity", background="black", foreground="white"
        )
        self.opacity_entry = Scale(window, from_=0, to=255, orient=HORIZONTAL)
        self.opacity_button.config(
            text="Change Opacity", background="black", foreground="white"
        )
        self.opacity_label.grid(row=3, column=3)
        self.opacity_entry.grid(row=3, column=4)
        self.opacity_button.grid(row=4, column=4, sticky="n")

    def place_move_up_button(self):
        self.move_up_button.config(text=" ▲ ", background="black", foreground="white")
        self.move_up_button.grid(row=4, column=2, sticky="e", pady=10)

    def place_move_left_button(self):
        self.move_left_button.config(text="◀️", background="black", foreground="white")
        self.move_left_button.grid(row=5, column=2, sticky="ne", padx=25, pady=10)

    def place_move_right_button(self):
        self.move_right_button.config(text="▶️", background="black", foreground="white")
        self.move_right_button.grid(row=5, column=3, sticky="nw", pady=10)

    def place_move_down_button(self):
        self.move_down_button.config(text=" ▼ ", background="black", foreground="white")
        self.move_down_button.grid(row=6, column=2, sticky="ne")

    def place_degree_contents(self):
        self.degree_label.config(
            text="Rotate: ", background="black", foreground="white"
        )
        self.degree_button.config(text="Rotate", background="black", foreground="white")
        self.degree_label.grid(row=7, column=1, sticky="w")
        self.degree_entry.grid(row=7, column=2, sticky="w", columnspan=3)
        self.degree_button.grid(row=7, column=4, sticky="w", padx=20)

    def upload_picture_button(self):
        self.upload_button.config(text="Upload", background="black", foreground="white")
        self.upload_button.grid(
            row=9, column=1, sticky="nswe", pady=25, padx=15, columnspan=2
        )

    def save_picture_button(self):
        self.save_button.config(text="Save", background="black", foreground="white")
        self.save_button.grid(
            row=9, column=3, padx=25, pady=25, sticky="nswe", columnspan=4
        )
