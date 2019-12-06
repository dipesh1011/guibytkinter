from tkinter import *

eqn=""
def number(n):
    global eqn
    eqn=eqn+str(n)
    input.set(eqn)

def calculate(n1):
    try:
        res=eval(n1)
        input.set(res)
    except:
        input.set("Error!!!")

def cancel(c):
    global eqn
    input.set("")
    eqn=""

root = Tk()
root.configure(bg='grey')
root.title("Calculator")
root.geometry("265x265")
root.resizable(0,0)
input=StringVar()
e1=Entry(root,bg="white",fg="black",font="Times",width=30,textvariable=input).grid(row=0,column=0,rowspan=2,columnspan=4,padx=10,pady=10)
b1=Button(root,text="1",bg="white",fg="black",font="times",width=5,command=lambda:number(1)).grid(row=2,column=0,padx=5,pady=5)
b2=Button(root,text="2",font="Times",width=5,command=lambda:number(2)).grid(row=2,column=1,padx=5,pady=5)
b3=Button(root,text="3",font="Times",width=5,command=lambda:number(3)).grid(row=2,column=2,padx=5,pady=5)
b4=Button(root,text="+",font="Times",width=5,command=lambda:number("+")).grid(row=2,column=3,padx=5,pady=5)
b5=Button(root,text="4",font="Times",width=5,command=lambda:number(4)).grid(row=3,column=0,padx=5,pady=5)
b6=Button(root,text="5",font="Times",width=5,command=lambda:number(5)).grid(row=3,column=1,padx=5,pady=5)
b7=Button(root,text="6",font="Times",width=5,command=lambda:number(6)).grid(row=3,column=2,padx=5,pady=5)
b8=Button(root,text="-",font="Times",width=5,command=lambda:number("-")).grid(row=3,column=3,padx=5,pady=5)
b9=Button(root,text="7",font="Times",width=5,command=lambda:number(7)).grid(row=4,column=0,padx=5,pady=5)
b10=Button(root,text="8",font="Times",width=5,command=lambda:number(8)).grid(row=4,column=1,padx=5,pady=5)
b11=Button(root,text="9",font="Times",width=5,command=lambda:number(9)).grid(row=4,column=2,padx=5,pady=5)
b13=Button(root,text="*",font="Times",width=5,command=lambda:number("*")).grid(row=4,column=3,padx=5,pady=5)
b14=Button(root,text="0",font="Times",width=5,command=lambda:number("0")).grid(row=5,column=0,padx=5,pady=5)
b15=Button(root,text=".",font="Times",width=5,command=lambda:number(".")).grid(row=5,column=1,padx=5,pady=5)
b16=Button(root,text="C",font="Times",width=5,command=lambda:cancel("eqn")).grid(row=5,column=2,padx=5,pady=5)
b8=Button(root,text="/",font="Times",width=5,command=lambda:number("/")).grid(row=5,column=3,padx=5,pady=5)
b19=Button(root,text="=",font='Times',width=5,command=lambda:calculate(eqn)).grid(row=6,column=0,rowspan=2,columnspan=4,padx=10,pady=10)
root.mainloop()