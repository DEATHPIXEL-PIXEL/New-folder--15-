from tkinter import*
root=Tk()
root.title=("login app")
root.geometry("400x400")
frame=Frame(master=root,height=250,width=360, bg="#136ce4" )


lbl1=Label(frame, text="Full ame ", bg="#136ce6" , fg="white" , width=12 )
lbl2=Label(frame, text="email id ", bg="#136ce6" , fg="white" , width=12 )
lbl3=Label(frame, text="password ", bg="#136ce6" , fg="white" , width=12 )

name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame,show="*")


def display():
    name=name_entry.get()
    message=name + "account has been created"
    textbox.insert(END,message)

textbox= Text(bg="#BEBEBE" , fg="black")
btn =Button(text="create accout" , command=display,bg="red")


frame.place(x=  20,y=0)
lbl1.place(x=20,y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()