from tkinter import *
import string
import random

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
root.config(bg='gold')
root.title("Password Generator")
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='green',fg='white')
passwordLabel.grid(row=0, column=1,pady=10)


lengthLabel=Label(root,text='Enter Password Length :',font=Font,bg='green',fg='white')
lengthLabel.grid(pady=3)

length_Box=Spinbox(root,from_=4,to_=18,width=5,font=Font)
length_Box.grid(row=2,column=2,pady=5)

weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.grid(row=3,column=1,pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(row=4,column=1,pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.grid(row=5,column=1,pady=5)

generateButton=Button(root,text='Generate Password',font=Font,command=generator,bg="blue",fg="white")
generateButton.grid(row=6,column=1,pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid(row=7,column=1)


root.mainloop()
