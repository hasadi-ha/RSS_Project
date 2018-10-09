from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import feedparser

# create a new tk window and gets screen size
root = tk.Tk()

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# path variable to store image path
path = "old_well.jpg"

# opens image from path
image = Image.open(path)

# resize image to fit the tk window, root
bgImg = image.resize((screenWidth, screenHeight), Image.ANTIALIAS)

# stores resized image, bgImg
bgImg = ImageTk.PhotoImage(bgImg)

# creates a label of the resized image
img = tk.Label(root, image=bgImg)

# bc this is a background photo, can just pack it in
img.pack(side="top", fill="both", expand=True)

# blueBg creates a Carolina blue canvas overlayed on the bgImg
# bg is background and the hex code within represents the id for
# UNC blue, or at least very close to it
# height and width were based on whatever the size of the display
# screen is * .65 or .7 so that the bgImg can be seen as a sort of border
blueBg = Canvas(root, bg='#4B9CD3', width=screenWidth*.85, height=screenHeight*.75, highlightthickness=0)

# using the place geometry manager, the canvas can be placed relative
# to the overall window (i just googled and apparently .5 works,
# I assume bc it places the center of the canvas halfway down and
# halfway across the window) and anchor places the canvas in a
# centered position relative to the window itself
blueBg.place(relx=0.5, rely=0.5, anchor=CENTER)

# create first of three new canvases
site1 = feedparser.parse('https://krebsonsecurity.com/feed')
entry1 = site1.entries[0]
post1 = entry1.title + "  "
titleLabel = Label(root, bg="red", width=int(screenWidth*.0472), height=int(screenHeight*.025), text=post1, anchor=S)
titleLabel.place(x=screenWidth*.075, y=screenHeight*.063)
tk.Misc.lift(titleLabel)










# mainloop to keep the window running until it is manually closed
root.mainloop()