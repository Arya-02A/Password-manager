from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message=f"Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("password_file.json", "r") as password_file:
                data = json.load(password_file)   # Reading old data in the password file.
        except FileNotFoundError:
            with open("password_file.json", "w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            data.update(new_data)   # Updating the old data with the new data.

            with open("password_file.json", "w") as password_file:
                json.dump(data, password_file, indent=3)   # Saving the updated data.
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("password_file.json", "r") as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Error!", message=f"No data file found !")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f"Search {website}", message=f"details for '{website}':\n email : {email}\n password : {password}")
        else:
            messagebox.showinfo(title=f"Error!", message=f"Not found details for '{website}' in your saved data.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_input = Entry(width=25)
website_input.grid(row=1, column=1)
website_input.focus()

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_input = Entry(width=43)
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

password_input = Entry(width=25)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
