from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    passs.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    output1 = web.get()
    output2 = ema.get()
    output3 = passs.get()
    new_data={output1:{
        "email":output2,
        "password":output3,
    }}
    if len(output1) == 0 or len(output3) == 0:
        messagebox.showinfo(
            title="Dumbass Located", message="Fill out the form idiot!!"
        )
    else:
        try:
            with open("data.json", "r") as f:
                data=json.load(f)
                data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data , f,indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data , f,indent=4)
        

def delete_entry():
    web.delete(0, END)
    passs.delete(0, END)

def search_data():
    pass

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)


web = Entry(width=34)
web.grid(row=1, column=1)
web.focus()
ema = Entry(width=34)
ema.grid(row=2, column=1)
ema.insert(0, "anujacharya877@gmail.com")


passs = Entry(width=24)
passs.grid(row=3, column=1)

generate = Button(text="Generate Password", command=generate_password)
generate.grid(row=3, column=2)

add = Button(text="Add",width=32, command=lambda: [save(), delete_entry()])
add.grid(row=4, column=1)

search= Button(text="Search")
search.grid(row=1, column=2)
window.mainloop()
