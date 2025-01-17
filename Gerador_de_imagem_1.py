import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import random

class ImageRandomizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Randomizer")

        self.label = tk.Label(root, text="Selecione um diretório")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Selecionar Diretório", command=self.select_directory)
        self.select_button.pack(pady=5)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.random_button = tk.Button(root, text="Sortear Imagem", command=self.display_random_image, state=tk.DISABLED)
        self.random_button.pack(pady=5)

        self.image_files = []

    def select_directory(self):
        self.image_dir = filedialog.askdirectory()
        if self.image_dir:
            self.image_files = [os.path.join(self.image_dir, file) for file in os.listdir(self.image_dir) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            if self.image_files:
                self.random_button.config(state=tk.NORMAL)
                self.label.config(text="Diretório selecionado: " + self.image_dir)
            else:
                self.label.config(text="Nenhuma imagem encontrada no diretório")

    def display_random_image(self):
        if self.image_files:
            image_path = random.choice(self.image_files)
            image = Image.open(image_path)
            image = image.resize((400, 400), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo)
            self.image_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageRandomizerApp(root)
    root.mainloop()
