import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("500x500")
window.configure(bg='grey')

path = "old_well.jpg"

img = ImageTk.PhotoImage(Image.open(path))

panel = tk.Label(window, image=img)

panel.pack()

window.mainloop()