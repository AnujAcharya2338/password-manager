from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(row=0,column=1)

website = Label(text="Website:")
website.grid(row=1,column=0)

email = Label(text="Email/Username:")
email.grid(row=2,column=0)

password = Label(text="Password:")
password.grid(row=3,column=0)



input1 = Entry(width=36)
input1.grid(row=1,column=1, columnspan=2)

input2 = Entry(width=36)
input2.grid(row=2,column=1,columnspan=2)


input3 = Entry(width=28)
input3.grid(row=3,column=1)

generate=Button(text="Generate Password")
generate.grid(row=3,column=2)

add=Button(text="Add", width=36)
add.grid(row=4,column=1,columnspan=2)
window.mainloop()