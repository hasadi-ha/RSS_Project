import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()

label = tk.Label(root)
img = Image.open(r"C:\Users\zgoodman\desktop\work\RSS_Project\krebs.jpg")
label.img = ImageTk.PhotoImage(img)
label['image'] = label.img

label.pack()
root.mainloop()