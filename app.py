import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# Open CrystalFontz logo, resize it, then place it at the top left corner
logo_image = Image.open("res/Christmas_Cards_2010.ppm")
logo_image = logo_image.resize((180,38))
logo_image_tk = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(image = logo_image_tk)
logo_label.image = logo_image_tk

logo_label.place(x = 0, y = 0)

# Resize the window
root.geometry("480x480")

root.mainloop()

