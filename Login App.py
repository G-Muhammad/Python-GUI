from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# Function to handle login logic
def handle_login():
    email = email_input.get()
    password = password_input.get()

    if not email or not password:
        messagebox.showwarning('Warning', 'Please fill in all fields')
    elif email.strip().lower() == 'gmohammad@gmail.com' and password == '1234':
        messagebox.showinfo('Success', 'Login Successful')
    else:
        messagebox.showerror('Error', 'Login Failed')

# Function to exit the application
def handle_exit():
    root.destroy()

# Function to create and arrange all widgets
def create_widgets():
    # Flipkart logo
    try:
        img = Image.open('flipkart-logo.png')
        resized_img = img.resize((70, 70))
        logo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(root, image=logo_img, bg='#0096DC')
        img_label.image = logo_img  # Keep a reference to avoid garbage collection
        img_label.grid(row=0, column=0, columnspan=2, pady=(10, 10))
    except FileNotFoundError:
        messagebox.showwarning('Warning', 'Logo file not found!')

    # App title
    text_label = Label(root, text='Flipkart', fg='white', bg='#0096DC')
    text_label.config(font=('verdana', 24, 'bold'))
    text_label.grid(row=1, column=0, columnspan=2, pady=(10, 10))

    # Email input
    email_label = Label(root, text='Enter Email', fg='black', bg='#0096DC')
    email_label.config(font=('verdana', 10, 'bold'))
    email_label.grid(row=2, column=0, pady=(20, 5), padx=10, sticky='e')

    global email_input  # Declare global to access in handle_login
    email_input = Entry(root, width=35)
    email_input.grid(row=2, column=1, ipady=3, pady=(20, 5), padx=10)

    # Password input
    password_label = Label(root, text='Enter Password', fg='black', bg='#0096DC')
    password_label.config(font=('verdana', 12, 'bold'))
    password_label.grid(row=3, column=0, pady=(20, 5), padx=10, sticky='e')

    global password_input  # Declare global to access in handle_login
    password_input = Entry(root, width=35, show='*')  # Secure input
    password_input.grid(row=3, column=1, ipady=3, pady=(20, 5), padx=10)

    # Login button
    login_btn = Button(root, text='Login', bg='gray', fg='blue', width=12, height=1, command=handle_login)
    login_btn.config(font=('verdana', 12, 'bold'))
    login_btn.grid(row=4, column=0, columnspan=2, pady=(20, 10))

    # Exit button
    exit_btn = Button(root, text='Exit', bg='gray', fg='blue', width=12, height=1, command=handle_exit)
    exit_btn.config(font=('verdana', 12, 'bold'))
    exit_btn.grid(row=5, column=0, columnspan=2, pady=(10, 20))

# Main application
root = Tk()
root.title('Beautiful Login Form')

# Ensure icon file exists, else skip
try:
    root.iconbitmap('IMG_20241027_230002.ico')
except FileNotFoundError:
    print("Icon file not found. Continuing without icon.")

root.geometry('400x400')
root.configure(background='#0096DC')

create_widgets()

root.mainloop()
