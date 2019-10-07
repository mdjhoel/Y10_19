from tkinter import *
from tkinter import filedialog
from PIL import ImageTk

def test(event):
    global myimg
    global can2
    root.filename =  filedialog.askopenfilename(initialdir = "/Users/mhoel/Pictures",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    myimg = ImageTk.PhotoImage(file=root.filename)
    can2.create_image(10, 10, image = myimg, anchor = NW)
    

root = Tk()
root.title("photo tagger")

topframe = Frame(root,bg="blue")
topframe.pack(fill=X) # make as wide as root

can1 = Canvas(topframe, width="20",height="20",bg="blue",bd=0,highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill="white")
can1.create_line(0, 10, 20, 10,fill="white")
can1.create_line(0, 15, 20, 15,fill="white")
can1.bind("<Button-1>",test )
can1.pack(side=LEFT, padx=5, pady=5)

canframe = Frame(root)
canframe.pack(fill=X) 

can2 = Canvas(canframe,bd=0,highlightthickness=0)
can2.pack(side=LEFT,fill=X)

myimg = ImageTk.PhotoImage(file = "/Users/mhoel/Desktop/matdesign/bremners.jpg")
can2.create_image(10, 10, image = myimg, anchor = NW)

frame1 = Frame(root)
frame1.pack(fill=X)

lbl1 = Label(frame1, text="Title", width=6,bg="blue",fg="white")
lbl1.pack(side=LEFT, padx=5, pady=5)

entry1 = Entry(frame1)
entry1.pack(fill=X, padx=5, expand=True)

frame2 = Frame(root)
frame2.pack(fill=X)

frame3 = Frame(root)
frame3.pack(fill=BOTH, expand=True)

lbl3 = Label(frame3, text="Review", width=6)
lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

txt = Text(frame3)
txt.pack(fill=BOTH, pady=5, padx=5, expand=True)




