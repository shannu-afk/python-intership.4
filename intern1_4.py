from tkinter import *
import random,string
root=Tk()
root.geometry("460x580")
root.title("Password Generator")

#intro text
title=StringVar()
label=Label(root,textvariable=title).pack()
title.set("The strenght of password")
def selection():
    selection=choice.get()
choice=IntVar()
R1=Radiobutton(root,text="poor",variable=choice,value=1,command=selection).pack(anchor=CENTER)
R2=Radiobutton(root,text="AVERAGE",variable=choice,value=2,command=selection).pack(anchor=CENTER)
R3=Radiobutton(root,text="ADVANCE",variable=choice,value=3,command=selection).pack(anchor=CENTER)

labelchoice=Label(root)
labelchoice.pack()

lenlabel=StringVar()
lenlabel.set("Password length")
lentitle=Label(root,textvariable=lenlabel).pack()

val=IntVar()
spinlength=Spinbox(root,from_=8,to_=24,textvariable=val,width=13).pack()

def callback():
    sum1.config(text=passgen())
passgenButton=Button(root,text="Generate password",bd=5,height=2,command=callback,pady=3)
passgenButton.pack()
password=str(callback)

sum1=Label(root,text="")
sum1.pack(side=BOTTOM)
#the poor contains lower and upper case alphabets
poor=string.ascii_uppercase+string.ascii_lowercase
#the average contains lower and upper alphabets and also numbers
average=string.ascii_uppercase+string.ascii_lowercase+string.digits
symbols="""@#$%^&*!{}[]()?"""
#the advance contains lower and upper alphabets ,numbers and special symbols
advance=poor+average+symbols

def passgen():
    if choice.get()==1:
        return "".join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return "".join(random.sample(average,val.get()))
    elif choice.get()==3:
        return "".join(random.sample(advance,val.get()))

root.mainloop()
