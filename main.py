from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_password():
    nr_letters = randint(8, 10) 
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    pass_letters=[choice(letters) for _ in range(nr_letters)]
    pass_symbols=[choice(symbols) for _ in range(nr_symbols)]
    pass_numbers=[choice(numbers) for _ in range(nr_numbers)]

    password_list=pass_letters+ pass_numbers+pass_symbols

    shuffle(password_list)
    password="".join(password_list)

    pass_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site=url_entry.get()
    email=email_entry.get()
    password=pass_entry.get()
    if site=="" or password=="":
        messagebox.showerror(title="Oops",message="All values should be filled in")
    else:
        is_ok= messagebox.askokcancel(title=site,message=f"These are the details entered:\n Email: {email}\nPassword: {password}\n Press okay to save")
        if is_ok:    
            with open("./passwords.txt","a") as data:
                data.write(f"{site} | {email} | {password}\n")
                url_entry.delete(0,END)
                pass_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
logo_image=PhotoImage(file="./logo.png")
url_label=Label(text="Website:")
email_label=Label(text="Email:")
pass_label=Label(text="Password:")
url_entry=Entry(width=40)
email_entry=Entry(width=40)
pass_entry=Entry(width=23)
gen_pass_btn=Button(text="Generate Password",command=gen_password)
add_btn=Button(text="Add",width=36,command=save)
canvas=Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,100,image=logo_image)

canvas.grid(row=0,column=1)
url_label.grid(row=1,column=0)
email_label.grid(row=2,column=0)
pass_label.grid(row=3,column=0)
url_entry.grid(row=1,column=1,columnspan=2)
email_entry.grid(row=2,column=1,columnspan=2)
pass_entry.grid(row=3,column=1)
gen_pass_btn.grid(row=3,column=2)
add_btn.grid(row=4,column=1,columnspan=2)
url_entry.focus()
email_entry.insert(0,"rockys1991@gmail.com")


window.mainloop()
