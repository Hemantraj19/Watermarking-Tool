from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkinter import filedialog


class PerformFunctions:
    def __init__(self):
        self.uploaded_image_path = None
        self.photo_image = None
        self.draggable_text = None
        self.text = None
        self.watermark_text = None
        self.color = None

    def upload(self):
        filetypes = (("All files", "*.*"),)
        uploaded_image_path = fd.askopenfilename(filetypes=filetypes)

        if uploaded_image_path:
            self.uploaded_image_path = uploaded_image_path
            img = Image.open(uploaded_image_path)
            print(img.width)
            if img.width > 800 or img.height > 550:
                img = img.resize((800, 550))
            self.photo_image = ImageTk.PhotoImage(img)
            return self.photo_image
        else:
            return None

    def get_img(self, canvas, image):
        new_image = self.upload()

        # Set a maximum canvas size
        max_canvas_width = 800
        max_canvas_height = 550

        # Resize the canvas if the image dimensions exceed the maximum
        if (
            new_image.width() > max_canvas_width
            or new_image.height() > max_canvas_height
        ):
            # new_image = new_image.resize((max_canvas_width, max_canvas_height))
            canvas.config(width=max_canvas_width, height=max_canvas_height)
        else:
            canvas.config(width=new_image.width(), height=new_image.height())

        canvas.itemconfig(image, image=new_image)

    def get_text_over_image(self, form, canvas):
        self.text = form.entry.get()
        self.watermark_text = canvas.create_text(350, 250, text=self.text)

    def change_text_font(self, canvas, font, font_size):
        canvas.itemconfig(self.watermark_text, font=(font, font_size, "bold"))

    def change_text_color(self, canvas, color):
        self.color = color[1]
        canvas.itemconfig(
            self.watermark_text,
            fill=color[1],
        )

    def change_opacity(self, canvas, opacity):
        opacity = max(0, min(opacity, 255))

        # Convert opacity from 0-255 to hexadecimal format
        alpha_hex = format(opacity, "02x")

        # Construct a transparent color using the alpha value
        transparent_color = "#{:02x}{}{}{}".format(
            opacity, self.color[1:3], self.color[3:5], self.color[5:]
        )

        # Set the fill color for the text item on the canvas
        canvas.itemconfig(self.watermark_text, fill=transparent_color)

    def move_up(self, canvas):
        canvas.move(self.watermark_text, 0, -10)

    def move_down(self, canvas):
        canvas.move(self.watermark_text, 0, 10)

    def move_left(self, canvas):
        canvas.move(self.watermark_text, -10, 0)

    def move_right(self, canvas):
        canvas.move(self.watermark_text, 10, 0)

    def rotate_text(self, canvas, angle):
        canvas.itemconfig(self.watermark_text, angle=angle)

    def save_image(self, canvas):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG files", "*.png")]
        )

        if file_path:
            canvas.postscript(file=file_path + ".eps", colormode="color")
            img = Image.open(file_path + ".eps")
            img.save(file_path + ".png", "png")
