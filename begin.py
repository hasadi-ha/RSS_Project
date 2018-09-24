import feedparser
from tkinter import *

feed = feedparser.parse('http://www.reddit.com/r/python/.rss')
# for post in feed.entries:
#    print(post.title + ": " + post.link + "\n")

post = feed.entries[0]

newsDisplay = Tk()
news = Label(newsDisplay, text=post.title)
news.pack()
newsDisplay.mainloop()












