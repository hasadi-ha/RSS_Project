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

infoFrame = Frame(blueFrame, width=screenWidth*.765, height=screenHeight*.6813)
infoFrame.place(relx=.5, rely=.5, anchor=CENTER)
infoFrame.pack_propagate(False)

extraFrame1 = Frame(infoFrame, width=screenWidth*.765, height=screenHeight*.6813)
extraFrame1.pack(side="top")

extraFrame2 = Frame(infoFrame, width=screenWidth*.765, height=screenHeight*.6813)
extraFrame2.pack(side="bottom")

picLabel = Label(extraFrame1, width=int(screenWidth*.3826),
                 height=int(screenHeight*.34065), image=bgImg).pack(side="left",
                                                                    fill="both", expand=True)
titleLabel = Label(extraFrame1, bg="red", width=int(screenWidth*.3826),
                   height=int(screenHeight*.34065), text=post1).pack()
descLabel = Label(extraFrame1, bg="green", width=int(screenWidth * .765),
                  height=int(screenHeight * .3826), text=entry1.description)\
    .pack(side="bottom")

# mainloop to keep the window running until it is manually closed
root.mainloop()