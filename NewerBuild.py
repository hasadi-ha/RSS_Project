import tkinter as tk
import os
from PIL import Image, ImageTk
import feedparser
from tkinter import Frame, CENTER, Label, BOTH


def manage_time():
    global tracker
    if tracker == 1:
        label_maker(infoFrame, 0, 0, 630, 389, image=newImage1, background='red')
        label_maker(infoFrame, 630, 0, 655, 389, text=entry1.title, background='blue', font=("", 20), wraplength=600)
        label_maker(infoFrame, 0, 389, 1286, 389, text=entry1.description, wraplength=1250, font=("", 16),
                    background='green')
        tracker = 2
        root.after(15000, manage_time)
    elif tracker == 2:
        label_maker(infoFrame, 0, 0, 630, 389, image=newImage2, background='red')
        label_maker(infoFrame, 630, 0, 655, 389, text=entry2.title, background='blue', font=("", 20), wraplength=600)
        label_maker(infoFrame, 0, 389, 1286, 389, text=entry2.description, wraplength=1250, font=("", 16),
                    background='green')
        tracker = 3
        root.after(15000, manage_time)
    elif tracker == 3:
        label_maker(infoFrame, 0, 0, 630, 389, image=newImage3, background='red')
        label_maker(infoFrame, 630, 0, 655, 389, text=entry3.title, background='blue', font=("", 20), wraplength=600)
        label_maker(infoFrame, 0, 389, 1286, 389, text=entry3.description, wraplength=1250, font=("", 16),
                    background='green')
        tracker = 4
        root.after(15000, manage_time)
    elif tracker == 4:
        label_maker(infoFrame, 0, 0, 630, 389, image=newImage4, background='red')
        label_maker(infoFrame, 630, 0, 655, 389, text=entry4.title, background='blue', font=("", 20), wraplength=600)
        label_maker(infoFrame, 0, 389, 1286, 389, text=entry4.description, wraplength=1250, font=("", 16),
                    background='green')
        tracker = 5
        root.after(15000, manage_time)
    elif tracker == 5:
        label_maker(infoFrame, 0, 0, 630, 389, image=newImage5, background='red')
        label_maker(infoFrame, 630, 0, 655, 389, text=entry5.title, background='blue', font=("", 20), wraplength=600)
        label_maker(infoFrame, 0, 389, 1286, 389, text=entry5.description, wraplength=1250, font=("", 16),
                    background='green')

        tracker = 1
        root.after(15000, manage_time)
    else:
        root.destroy()


def label_maker(master, x, y, w, h, *args, **kwargs):
    frame = Frame(master, width=w, height=h)
    frame.pack_propagate(0)
    frame.place(x=x, y=y)
    label = Label(frame, *args, **kwargs).pack(fill=BOTH, expand=1)
    return label


# create a new tk window and gets screen size based on monitor display
root = tk.Tk()
tracker = 1
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# path variable to store image path
path = str(os.getcwd()) + "\old_well.jpg"

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
blueFrame = Frame(root, bg='#4B9CD3', width=int(screenWidth * .85),
                  height=int(screenHeight * .757))
blueFrame.place(relx=.5, rely=.5, anchor=CENTER)

# initialize infoFrame and use it to encompass other three frames
infoFrame = Frame(blueFrame, width=screenWidth * .765, height=screenHeight * .6813)
infoFrame.place(x=75, y=40)
infoFrame.pack_propagate(0)


# create new photo image of one of the sites' pics and save it as newImage
input1 = str(os.getcwd()) + "\\krebs.jpg"
img1 = Image.open(input1)
image1 = img1.resize((691, 389))
newImage1 = ImageTk.PhotoImage(image1)
input2 = str(os.getcwd()) + "\\threat_post_img.png"
img2 = Image.open(input2)
image2 = img2.resize((660, 389))
newImage2 = ImageTk.PhotoImage(image2)
input3 = str(os.getcwd()) + "\\security_list.jfif"
img3 = Image.open(input3)
image3 = img3.resize((691, 389))
newImage3 = ImageTk.PhotoImage(image3)
input4 = str(os.getcwd()) + "\\sophos_sec.jfif"
img4 = Image.open(input4)
image4 = img4.resize((691, 389))
newImage4 = ImageTk.PhotoImage(image4)
input5 = str(os.getcwd()) + "\\cisco_security.jfif"
img5 = Image.open(input5)
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

root.after(15000, manage_time())
root.mainloop()
