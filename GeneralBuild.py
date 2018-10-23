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

# using the place geometry manager, the canvas can be placed relative
# to the overall window (i just googled and apparently .5 works,
# I assume bc it places the center of the canvas halfway down and
# halfway across the window) and anchor places the canvas in a
# centered position relative to the window itself
# blueBg.place(relx=0.5, rely=0.5, anchor=CENTER)

# create three canvases for pic, title, and description
site1 = feedparser.parse('https://krebsonsecurity.com/feed')
entry1 = site1.entries[0]
post1 = entry1.title + "  "

# trying to create frames now, hopefully can fill frames with labels easier and then just have a frame per site
blueFrame = Frame(root, bg='#4B9CD3', width=int(screenWidth*.85),
                  height=int(screenHeight*.757))
blueFrame.place(relx=.5, rely=.5, anchor=CENTER)

# initialize infoFrame and use it to encompass other three frames
infoFrame = Frame(blueFrame, width=screenWidth*.765, height=screenHeight*.6813)
infoFrame.place(relx=.5, rely=.5, anchor=CENTER)
infoFrame.pack_propagate(0)

# picLabel to be label containing picture scraped from site, default pic in place now
# picLabel to be place in top left side of infoFrame overall
# resizing image to fit into picLabel
path = "old_well.jpg"
image02 = Image.open(path)
image2 = image.resize((691, 389), Image.ANTIALIAS)
newImage = ImageTk.PhotoImage(image2)
picLabel = Label(infoFrame, width="680",
                 height="381", image=newImage, borderwidth=0)

# titleLabel to be label displaying site title in right of extraFrame 1
titleLabel = Label(infoFrame, bg="red", width="100",
                   height="25", text=post1, anchor=CENTER)

# descLabel to display article description, filling extraFrame 2
descLabel = Label(infoFrame, bg="green", width="115",
                  height="16", text=entry1.description, wraplength=1400, font=("", 16))

picLabel.grid(row=0, column=0)
titleLabel.grid(row=0, column=1, columnspan=2)
descLabel.grid(row=1, column=0, columnspan=2)

# mainloop to keep the window running until it is manually closed
root.mainloop()
