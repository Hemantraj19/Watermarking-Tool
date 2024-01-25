from tkinter import filedialog as fd
from PIL import Image, ImageTk


class PerformFunctions:
    def __init__(self):
        self.uploaded_image_path = None
        self.photo_image = None
        self.draggable_text = None

    def upload(self):
        filetypes = (("All files", "*.*"),)
        uploaded_image_path = fd.askopenfilename(filetypes=filetypes)

        if uploaded_image_path:
            self.uploaded_image_path = uploaded_image_path
            img = Image.open(uploaded_image_path)
            print(img.width)
            if img.width > 950 or img.height > 650:
                img = img.resize((1000, 700))
            self.photo_image = ImageTk.PhotoImage(img)
            return self.photo_image
        else:
            return None
