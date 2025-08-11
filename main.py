from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    with open("data.txt", "w") as f:
        output1=input1.get()
        output2=input2.get()
        output3=input3.get()
        f.write(output1)
        f.write(output2)
        f.write(output3)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
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
input1.focus()
input2 = Entry(width=36)
input2.grid(row=2,column=1,columnspan=2)
input2.insert(0,"anujacharya877@gmail.com")


input3 = Entry(width=28)
input3.grid(row=3,column=1)

generate=Button(text="Generate Password")
generate.grid(row=3,column=2)

add=Button(text="Add", width=36,command=save)
add.grid(row=4,column=1,columnspan=2)
window.mainloop()