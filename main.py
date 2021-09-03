
from tkinter import *
t=Tk()
t.geometry("")

def Login():
    frame2 = Frame()
    frame2.place(x=0, y=0, width=400, height=300)
    name=Entry(frame2)
    name.pack()
    pwd=Entry(frame2)
    pwd.pack()
    login_btn=Button(frame2,text="Login")
    login_btn.pack()

frame1=Frame()
frame1.place(x=0,y=0,width=400,height=300)

#first Window
Welcome_btn=Button(frame1,text="Welcome to ABC Bank", command=Login, height =10, width=50)
Welcome_btn.pack()


t.mainloop()
