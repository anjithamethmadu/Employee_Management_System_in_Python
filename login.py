from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
     if usernameEntry.get()==''or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
     elif usernameEntry.get()=='anji' and passwordEntry.get()=='1234':
         messagebox.showinfo('Success','Login is successful')
         root.destroy()
         import ems

     else:
         messagebox.showerror('Error','Wrong Username or Password')
         clear()

def clear():
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)

root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('Login Page')
image=CTkImage(Image.open('pg.jpg'),size=(930,478))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headingLabel=CTkLabel(root,text='Employee Management System',bg_color='#DFF3FA',text_color='dark blue',font=('Goudy Old Style',25,'bold'))
headingLabel.place(x=80,y=150)

usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username',bg_color='#DFF3FA',width=180)
usernameEntry.place(x=130,y=190)

passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password',bg_color='#DFF3FA',width=180,show='*')
passwordEntry.place(x=130,y=240)

loginButton=CTkButton(root,text='Login',bg_color='#DFF3FA',cursor='hand2',command=login)
loginButton.place(x=150,y=290)

root.mainloop()

