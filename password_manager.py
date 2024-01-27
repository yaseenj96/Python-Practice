import json
from tkinter import *
from tkinter import messagebox
FONT = ("Arial", 12)
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():

    website = website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Error", message="Please don't leave any passwords empty!")
    else:
        try:
            with open('data.json', 'r') as file:
                #Read old data file
                data = json.load(file)
        except FileNotFoundError:
            #If file is not found, create a new file and update it
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            #Update old data with the new data if file is found
            data.update(new_data)
            with open('data.json', 'w') as file:
                #Save updated data
                json.dump(data, file, indent=4)
        finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- Find Password ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as file:
            # Read old data file
            data = json.load(file)
    except FileNotFoundError:
        # If file is not found, shoot an error
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        try:
            messagebox.showinfo(title="Password Info", message=f"Website: {website}\n"
                                                               f"Password: {data[website]["password"]}")
        except KeyError as error_message:
            messagebox.showinfo(title="Error", message=f"No details for {error_message} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)

canvas = Canvas(width= 200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100,100,image = logo)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:",font=FONT)
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:",font=FONT)
email_label.grid(row=2,column=0)
password_label = Label(text="Password:",font=FONT)
password_label.grid(row=3,column=0)

#Entries
website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry=Entry(width=38)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, 'yaseenj96@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

#Buttons
generate_password = Button(text="Generate Password",command=generate_password)
generate_password.grid(row=3,column=2)
add = Button(text="Add",width=36, command=add_password)
add.grid(row=4,column=1,columnspan=2)
search = Button(text="Search",command=find_password)
search.grid(row=1,column=2)


window.mainloop()
