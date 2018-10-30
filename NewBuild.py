from PIL import ImageTk
from PIL import Image
import tkinter as tk
import feedparser
from tkinter import CENTER, Frame, Label, BOTH
import time

# create a new tk window and gets screen size based on monitor display
root = tk.Tk()

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# path variable to store image path
path = "old_well.jpg"

# opens image from path
image = Image.open(path)

# resize image to fit the tk window, root
bgImg = image.resize((screenWidth, screenHeight))

# stores resized image, bgImg, as a photo image
bgImg = ImageTk.PhotoImage(bgImg)

# creates a label of the resized image
img = tk.Label(root, image=bgImg)

# bc this is a background photo, can just pack it in
img.pack(side="top", fill="both", expand=True)

# creates a carolina blue background to contain the information from the sites
blueFrame = Frame(root, bg='#4B9CD3', width=int(screenWidth*.85),
                  height=int(screenHeight*.757))
blueFrame.place(relx=.5, rely=.5, anchor=CENTER)

# initialize infoFrame and use it to encompass other three frames
infoFrame = Frame(blueFrame, width=screenWidth*.765, height=screenHeight*.6813)
infoFrame.place(x=75, y=40)
infoFrame.pack_propagate(0)


# create new photo image of one of the sites' pics and save it as newImage
img1 = Image.open(r"C:\Users\zgoodman\desktop\work\RSS_Project\krebs.jpg")
image1 = img1.resize((691, 389))
newImage1 = ImageTk.PhotoImage(image1)
img2 = Image.open(r"C:\Users\zgoodman\desktop\work\RSS_Project\threat_post_img.png")
image2 = img2.resize((660, 389))
newImage2 = ImageTk.PhotoImage(image2)
img3 = Image.open(r"C:\Users\zgoodman\desktop\work\RSS_Project\security_list.jfif")
image3 = img3.resize((691, 389))
newImage3 = ImageTk.PhotoImage(image3)
img4 = Image.open(r"C:\Users\zgoodman\desktop\work\RSS_Project\sophos_sec.jfif")
image4 = img4.resize((691, 389))
newImage4 = ImageTk.PhotoImage(image4)
img5 = Image.open(r"C:\Users\zgoodman\desktop\work\RSS_Project\cisco_security.jfif")
image5 = img5.resize((691, 389))
newImage5 = ImageTk.PhotoImage(image5)


# creating site var for the data from each site, parsed

site1 = feedparser.parse('https://krebsonsecurity.com/feed/')
site2 = feedparser.parse('https://threatpost.com/feed/')
site3 = feedparser.parse('https://securelist.com/feed/')
site4 = feedparser.parse('https://nakedsecurity.sophos.com/feed')
site5 = feedparser.parse('https://blogs.cisco.com/security/feed')

# getting the first article from each site and saving them as an entry var
entry1 = site1.entries[0]
entry2 = site2.entries[0]
entry3 = site3.entries[0]
entry4 = site4.entries[0]
entry5 = site5.entries[0]


# define a new label maker function to construct labels within frames that will
#  be placed within infoFrame
def label_maker(master, x, y, w, h, *args, **kwargs):
    frame = Frame(master, width=w, height=h)
    frame.pack_propagate(0)
    frame.place(x=x, y=y)
    label = Label(frame, *args, **kwargs).pack(fill=BOTH, expand=1)
    return label


# creates new labels for the site pic, title of the first article, and first article description
def fn1():
    label_maker(infoFrame, 0, 0, 630, 389, image=newImage1, background='red')
    label_maker(infoFrame, 630, 0, 655, 389, text=entry1.title, background='blue', font=("", 20), wraplength=600)
    label_maker(infoFrame, 0, 389, 1286, 389, text=entry1.description, wraplength=1250, font=("", 16),
                background='green')


def fn2():
    label_maker(infoFrame, 0, 0, 630, 389, image=newImage2, background='red')
    label_maker(infoFrame, 630, 0, 655, 389, text=entry2.title, background='blue', font=("", 20), wraplength=600)
    label_maker(infoFrame, 0, 389, 1286, 389, text=entry2.description, wraplength=1250, font=("", 16),
                background='green')


def fn3():
    label_maker(infoFrame, 0, 0, 630, 389, image=newImage3, background='red')
    label_maker(infoFrame, 630, 0, 655, 389, text=entry3.title, background='blue', font=("", 20), wraplength=600)
    label_maker(infoFrame, 0, 389, 1286, 389, text=entry3.description, wraplength=1250, font=("", 16),
                background='green')


def fn4():
    label_maker(infoFrame, 0, 0, 630, 389, image=newImage4, background='red')
    label_maker(infoFrame, 630, 0, 655, 389, text=entry4.title, background='blue', font=("", 20), wraplength=600)
    label_maker(infoFrame, 0, 389, 1286, 389, text=entry4.description, wraplength=1250, font=("", 16),
                background='green')


def fn5():
    label_maker(infoFrame, 0, 0, 630, 389, image=newImage5, background='red')
    label_maker(infoFrame, 630, 0, 655, 389, text=entry5.title, background='blue', font=("", 20), wraplength=600)
    label_maker(infoFrame, 0, 389, 1286, 389, text=entry5.description, wraplength=1250, font=("", 16),
                background='green')


fn1()



# keeps gui running until manually closed
root.mainloop()
