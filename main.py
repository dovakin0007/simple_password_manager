from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def create_password():

    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    random.shuffle(password_list)
    password = "".join(password_list)
    if len(password_entry.get()) == 0:
        password_entry.insert(0, string=password)
        pyperclip.copy(password)
    else:
        password_entry.delete(0, END)
        password_entry.insert(0, string=password)
        pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website_name = name_entry.get()
    email_id = email_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email id": email_id,
            "password": password
        }
    }
    if len(website_name) == 0 or len(email_id) == 0 or len(password) == 0:
        messagebox.showerror(title="Insert fields", message="Please insert the required fields")
    else:
        try:
            with open(file="password.json", mode="r") as file:
                # json.dump(new_data, file, indent=4)
                # json.load(file)
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open(file="password.json", mode="w") as file:
                json.dump(new_data, file, indent=4)

        else:
            with open(file="password.json", mode="w") as file:
                json.dump(data, file, indent=4)

        finally:
            name_entry.delete(0, END)
            password_entry.delete(0, END)


def Search_entry():
    try:
        with open("password.json", "r") as fileread:
            data = json.load(fileread)
        # try:
        #     website_name = name_entry.get()
        #     x = (data[website_name])
        # except KeyError:
        #
        #     messagebox.showerror(title="Error", message="Value doesnt exits")
        # else:
        #     print(x)
        #     messagebox.showinfo(title=website_name, message=f"email id : {data[website_name]['email id']}\n"
        #                                                            f"password : {data[website_name]['password']}")

    except FileNotFoundError:
        messagebox.showerror(title="error",message="file not found")
    else:
        try:
            website_name = name_entry.get()
            x = (data[website_name])
        except KeyError:

            messagebox.showerror(title="Error", message="Value doesnt exits")
        else:
            print(x)
            messagebox.showinfo(title=website_name, message=f"email id : {data[website_name]['email id']}\n"
                                                                   f"password : {data[website_name]['password']}")
            name_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=189)
photofile = PhotoImage(file="logo.png")
canvas.create_image(100, 94, image=photofile)
canvas.grid(row=1, column=1)

name_label = Label(text="Website:")
name_label.grid(row=2, column=0)
name_entry = Entry(width=21)
name_entry.focus()
search_entry = Button(text="Search", command=Search_entry)
name_entry.grid(row=2, column=1)
search_entry.grid(row=2,column=2)
email_label = Label(text="Email_id/Username:")
email_label.grid(row=3, column=0)
email_entry = Entry(width=35)
email_entry.insert(0, "dovakin0007@gmail.com")
email_entry.grid(row=3, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=4, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=4, column=1)

generate_password = Button(text="Generate pass", command=create_password)
generate_password.grid(row=4, column=2)

add_password = Button(text="Add password", width=36, height=1, command=save_password)
add_password.grid(row=5, column=1, columnspan=2)
window.mainloop()







