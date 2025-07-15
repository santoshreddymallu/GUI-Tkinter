from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()
    
    if email == 'santoshreddymallu@gmail.com' and password == '1234':
        messagebox.showinfo('yes','Login Successful')
    else:
        messagebox.showerror('Error','Login failed')
        

root = Tk()
root.title('Login Form')
root.geometry('350x500')
root.configure(background='#0096DC')

#Load and resize image
img = Image.open('flipkart-logo.png') # open image
resized_img = img.resize((70,70)) # resize image if image is larger
img = ImageTk.PhotoImage(resized_img)

#image display
img_label = Label(root,image=img)
img_label.pack(pady=(10,10)) # pack - it packs image in correct size pady used to move image

#title
text_label = Label(root,text='Flipkart',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=("verdana",24))

#email label and input
email_label=Label(root,text='Enter email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=("verdana",12))

email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

#password label and input
password_label=Label(root,text='Enter Password',fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=("verdana",12))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))


#login button
login_btn = Button(root,text='Login Here',bg='white',fg='black',command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',14))

root.mainloop()
