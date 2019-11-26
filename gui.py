from tkinter import *

'''root = Tk() #initializing object
root.title("Tkinter Window")#sets title
root.geometry("700x300")#sets size
root.resizable(0,0) #make window's size same
root.mainloop() #making screen appear'''

#widgets and pack layout
'''root1 = Tk()
root1.geometry("400x400")
var = Label(root1, text = "Hello World")
var.pack() #pack layout
Label(root1,text = "How are you!").pack()
root1.mainloop()'''

#grid layout
'''root2 = Tk()
root2.geometry('500x500')
var = Label(root2, text = "dipesh")
var.grid(row = 0,column =0)
var1 = Label(root2, text = "koirala").grid(row = 0,column = 1)
root2.mainloop()'''

#place layout
'''root3 = Tk()
root3.geometry("500x500")
root3.resizable(0,0)
var = Label(root3, text = "dipesh")
var.place(relx = 0.5,rely = 0)
Label(root3,text = "koirala").place(relx = 0.5, rely = 0.5)
root3.mainloop()'''

#widgets
'''root4 = Tk()
root4.config(background = "black")
root4.geometry("600x600")
root4.resizable(0,0)
var = Label(root4, text = "dipesh")
var.config(font=("Times New Roman",30),bg ="green",fg="blue")
var.pack()
var1 = Label(root4,text="koirala")
var1.config(font=("Times New Roman",30),background="red",foreground="green")
var1.pack()

but1 = Button(root4, text = "Click",font=("",20))
but1.pack(padx=(10,10),pady=(10,10))

logo = PhotoImage(file = "log.png")
small_logo = logo.subsample(1,1)
but1.config(image=small_logo,compound=LEFT)
root4.mainloop()'''


#buttons doing some function

def click():
    txt.set("You clicked")

root6=Tk()
root6.geometry("500x500")
root6.resizable(0,0)
Label(root6,text="dipesh").pack()
txt=StringVar()
var=Label(root6,textvariable=txt)
var.config(font=("",30),bg="teal",fg="grey")
var.pack()
but1=Button(root6,text="Click",font=("",30),command=click)
but1.pack(padx=(10,10),pady=(10,10))
root6.mainloop()


