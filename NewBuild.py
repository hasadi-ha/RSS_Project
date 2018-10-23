from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import feedparser
import tkinter.filedialog as fd


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

# trying to create frames now, hopefully can fill frames with labels easier and then just have a frame per site
blueFrame = Frame(root, bg='#4B9CD3', width=int(screenWidth*.85),
                  height=int(screenHeight*.757))
blueFrame.place(relx=.5, rely=.5, anchor=CENTER)

# initialize infoFrame and use it to encompass other three frames
infoFrame = Frame(blueFrame, width=screenWidth*.765, height=screenHeight*.6813)
infoFrame.place(x=75, y=40)
infoFrame.pack_propagate(0)

# resizing image to fit into picLabel
# path = fd.askopenfilename()
path = "C:/Users/zgoodman/desktop/work/RSS_Project/krebs.jpg"
img = Image.open(path)
image2 = img.resize((691, 389), Image.ANTIALIAS)
newImage = ImageTk.PhotoImage(image2)
# create three canvases for pic, title, and description
site1 = feedparser.parse('https://krebsonsecurity.com/feed')
entry1 = site1.entries[0]
post1 = entry1.title + "  "


# define a new label maker function
def label_maker(master, x, y, w, h, *args, **kwargs):
    frame = Frame(master, width=w, height=h)
    frame.pack_propagate(0)
    frame.place(x=x, y=y)
    label = Label(frame, *args, **kwargs).pack(fill=BOTH, expand=1)
    return label


picLabel = label_maker(infoFrame, 0, 0, 630, 389, image=newImage, background='red')
titleLabel = label_maker(infoFrame, 630, 0, 655, 389, text=post1, background='blue', font=("", 20))
descLabel = label_maker(infoFrame, 0, 389, 1286, 389, text=entry1.description, wraplength=1250,
                        font=("", 16), background='green')
# descFrame = Frame(infoFrame, width=1285, height=389)
# descFrame.place(x=0, y=389)
# descLabel = Label(descFrame, width=1300, height=389, text=entry1.description, wraplength=1250)\
#     .pack(fill=BOTH, expand=1)

root.mainloop()
