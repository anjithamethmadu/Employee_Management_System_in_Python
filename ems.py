from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database

#functions

def delete_all():
    result=messagebox.askyesno('Confirm','Do You really want to delete all the records?')
    if result:
        database.deleteall_records()
        treeview_data()
    else:
        pass


def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchbox.set('Search By')


def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Enter value to search')
    elif searchbox.get()=='Search By':
        messagebox.showerror('Error', 'Please Select an option')
    else:
        searched_data=database.search(searchbox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('', END, values=employee)


def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Employee Data is Successfully deleted')




def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to update')
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Employee Data is Successfully Updated.')


def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        print(row)
        idEntry.insert(0,row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        salaryEntry.insert(0, row[5])
        rolebox.set(row[3])
        genderbox.set(row[4])



def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    salaryEntry.delete(0, END)
    rolebox.set('Web Developer')
    genderbox.set('Male')


def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)



def add_employee():
    if idEntry.get()==''or phoneEntry.get()==''or nameEntry.get()==''or salaryEntry.get()=='':
        messagebox.showerror('Error','All fields are required. ')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error', 'Id Already Exists.')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error', 'Invalid ID format')

    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is Added')

#GUI Part
window=CTk()
window.geometry('930x580+100+100')
window.resizable(False,False)
window.title('Employee Management System')
window.configure(fg_color='#333333')
logo=CTkImage(Image.open('qg.jpg'),size=(930,158))
logoLabel=CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(window,fg_color='#333333')
leftFrame.grid(row=1,column=0)


idLabel=CTkLabel(leftFrame,text='Id No:(EMP###)',font=('arial',18,'bold'))
idLabel.grid(row=0,column=0,padx=(0,20),pady=10,sticky='w')

idEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)


nameLabel=CTkLabel(leftFrame,text='Name:',font=('arial',18,'bold'))
nameLabel.grid(row=1,column=0,padx=(0,20),pady=10,sticky='w')

nameEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame,text='Phone No:',font=('arial',18,'bold'))
phoneLabel.grid(row=2,column=0,padx=(0,20),pady=10,sticky='w')

phoneEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
phoneEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text='Role:',font=('arial',18,'bold'))
roleLabel.grid(row=3,column=0,padx=(0,20),pady=10,sticky='w')

role_options=['Web Developer','Data Analyst','ML Engineer','BI Developer','Data Scientist','AI Engineer','IT Consultant','UX/UI Designer']
rolebox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',15,'bold'),state='readonly')
rolebox.grid(row=3,column=1)
rolebox.set(role_options[0])

genderLabel=CTkLabel(leftFrame,text='Gender:',font=('arial',18,'bold'))
genderLabel.grid(row=4,column=0,padx=(0,20),pady=10,sticky='w')

gender_options=['Male','Female']
genderbox=CTkComboBox(leftFrame,values=gender_options,width=180,font=('arial',15,'bold'),state='readonly')
genderbox.grid(row=4,column=1)
genderbox.set(gender_options[0])

salaryLabel=CTkLabel(leftFrame,text='Salary:',font=('arial',18,'bold'))
salaryLabel.grid(row=5,column=0,padx=(0,20),pady=10,sticky='w')

salaryEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
salaryEntry.grid(row=5,column=1)




rightFrame=CTkFrame(window,fg_color='#333333')
rightFrame.grid(row=1,column=1)

search_options=['Id','Name','Phone No','Role','Gender','Salary']
searchbox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchbox.grid(row=0,column=0)
searchbox.set('Search By')

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightFrame,text='Show All',width=100,command=show_all)
showallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone No','Role','Gender','Salary')
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone No',text='Phone No')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')

tree.column('Id',width=80,anchor=CENTER)  #anchor=CENTER
tree.column('Name',width=100,anchor=CENTER)
tree.column('Phone No',width=120)
tree.column('Role',width=160,anchor=CENTER)
tree.column('Gender',width=80,anchor=CENTER)
tree.column('Salary',width=100)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',12,'bold'))
style.configure('Treeview',font=('arial',11,'bold'),rowheight=30,background='#DFF3FA',foreground='black')
scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(window,fg_color='#333333')
buttonFrame.grid(row=2,column=0,columnspan=2,pady=10)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda:clear(True) )
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame,text='Delete All',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)

treeview_data()
window.bind('<ButtonRelease>',selection)

window.mainloop()