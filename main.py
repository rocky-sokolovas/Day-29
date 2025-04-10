from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import json
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
    new_data={site:{
        "email":email,
        "password":password
        }}
    if len(site)==0 or len(password)==0:
        messagebox.showerror(title="Oops",message="All values should be filled in")
    else:
        try:
            with open("./passwords.json","r") as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open("./passwords.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("./passwords.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            url_entry.delete(0,END)
            pass_entry.delete(0,END)
# ------------------------- SEARCH FUNCTION --------------------------- #

def search():
    site=url_entry.get()
    try:
        with open("./passwords.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No data",message="There are no passwords saved.")
    else:
        if site in data:
            messagebox.showinfo(title=site,message=f"Email: {data[site]["email"]}\nPassword: {data[site]["password"]}")
        else:
            messagebox.showinfo(title="No Website found",message="This website is not found, try a different name")



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
logo_image=PhotoImage(file="./logo.png")
url_label=Label(text="Website:")
email_label=Label(text="Email:")
pass_label=Label(text="Password:")
url_entry=Entry(width=23)
email_entry=Entry(width=40)
pass_entry=Entry(width=23)
search_btn=Button(text="Search",width=15,command=search)
gen_pass_btn=Button(text="Generate Password",command=gen_password)
add_btn=Button(text="Add",width=36,command=save)
canvas=Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,100,image=logo_image)

canvas.grid(row=0,column=1)
url_label.grid(row=1,column=0)
email_label.grid(row=2,column=0)
pass_label.grid(row=3,column=0)
url_entry.grid(row=1,column=1)
search_btn.grid(row=1,column=2)
email_entry.grid(row=2,column=1,columnspan=2)
pass_entry.grid(row=3,column=1)
gen_pass_btn.grid(row=3,column=2)
add_btn.grid(row=4,column=1,columnspan=2)
url_entry.focus()
email_entry.insert(0,"rockys1991@gmail.com")


window.mainloop()
