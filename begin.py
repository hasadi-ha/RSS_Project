import feedparser
from tkinter import *
import tkinter.scrolledtext

# creating site var for the data from each site, parsed

site1 = feedparser.parse('https://krebsonsecurity.com/feed')
site2 = feedparser.parse('https://threatpost.com/feed/')
site3 = feedparser.parse('https://securityboulevard.com/feed/')
site4 = feedparser.parse('https://nakedsecurity.sophos.com/feed')
site5 = feedparser.parse('https://feeds.feedblitz.com/thesecurityledger')

# getting the first article from each site and saving them as an entry var
entry1 = site1.entries[0]
entry2 = site2.entries[0]
entry3 = site3.entries[0]
entry4 = site4.entries[0]
entry5 = site5.entries[0]

# getting title of each of the first articles from the sites
# and adding space between them so they are distinguishable
post1 = entry1.title + "  "
post2 = entry2.title + "  "
post3 = entry3.title + "  "
post4 = entry4.title + "  "
post5 = entry5.title + "  "

# creating a new GUI by assigning newsDisplay to a new
# Tkinter object
newsDisplay = Tk()

# creating new labels for each site and packing them to
# the display with leftward orientation so they are horizontal
label = Label(newsDisplay, text=post1)
label.pack(side=LEFT)

label = Label(newsDisplay, text=post2)
label.pack(side=LEFT)

label = Label(newsDisplay, text=post3)
label.pack(side=LEFT)

label = Label(newsDisplay, text=post4)
label.pack(side=LEFT)

label = Label(newsDisplay, text=post5)
label.pack(side=LEFT)

# using mainloop() to loop the GUI display continuously and
# prevent it from closing immediately, allows it to stay
# running until manually told to quit by x'ing out the window
newsDisplay.mainloop()

