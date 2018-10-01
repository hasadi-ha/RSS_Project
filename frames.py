from tkinter import *


root = Tk()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
topRightFrame = Frame(root)
topRightFrame.pack(side=RIGHT)
topLeftFrame = Frame(root)
topLeftFrame.pack(side=LEFT)

label1 = Label(bottomFrame, text="bottom")
label1.pack(side=BOTTOM)
label2 = Label(topRightFrame, text="top right")
label2.pack(side=TOP)
label3 = Label(topLeftFrame, text="top left")
label3.pack(side=TOP)


root.mainloop()