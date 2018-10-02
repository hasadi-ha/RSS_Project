from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

# create a new tk window and initializes its size
root = tk.Tk()
root.geometry("1920x1080")

# path variable to store image path
path = "old_well.jpg"

# opens image from path
image = Image.open(path)

# resize image to fit the tk window, root
bgImg = image.resize((1920, 1080), Image.ANTIALIAS)

# stores resized image, bgImg
bgImg = ImageTk.PhotoImage(bgImg)

# creates a label of the resized image
img = tk.Label(root, image=bgImg)

# bc this is a background photo, can just pack it in
img.pack()

# canvas creates a Carolina blue canvas over layed on the bgImg
# bg is background and the hex code within represents the id for
# UNC blue, or at least very close to it
# height and width were based on a 1920x1080 screen, subtracting 20%
# from the 1920 and 1080 measurements so that the canvas takes up
# roughly 80% of the screen, highlightthickness is set to 0 so there
# won't be an outline around the canvas
canvas = Canvas(root, bg='#4B9CD3', width=1536, height=864, highlightthickness=0)
# using the place geometry manager, the canvas can be placed relative
# to the overall window (i just googled and apparently .5 works,
# I assume bc it places the center of the canvas halfway down and
# halfway across the window) and anchor places the canvas in a
# centered position relative to the window itself
canvas.place(relx=.5, rely=.5, anchor=CENTER)
# mainloop to keep the window running until it is manually closed
root.mainloop()





