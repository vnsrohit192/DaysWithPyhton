from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def Password_Generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

 

   
    pswd_letters=[choice(letters) for i in range(randint(8,10))]
    pswd_number=[choice(numbers) for j in range(randint(2,4))]
    pswd_spl_syml=[choice(symbols) for k in range(randint(2,4))]
    
    password_list=pswd_letters+pswd_number+pswd_spl_syml
    shuffle(password_list)

  

    password="".join(password_list)    
    password_input.insert(0,password)
    pyperclip.copy(password)
   
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=web_input.get()
    email=mail_input.get()
    password=password_input.get()
    new_data={website:{"email":email,
                   "password":password}}

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="opps",message= f"please fill the all entry ")
    else:
        try:
            with open("data.json","r") as file:    
              data=json.load(file)
            
        except FileNotFoundError:
            with open("data.json","w") as file:
              json.dump(new_data,file,indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as file:
                json.dump(data,file,indent=4)
        finally:
            web_input.delete(0,END)
            password_input.delete(0,END)

           

def find_password():
    website=web_input.get()
    try:
        with open("data.json",) as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="website",message=" file does not exist")
    else:            
        if website in data:
           email=data[website]["email"]
           password=data[website]["password"]
           messagebox.showinfo(title="website",message=f"password found \n website:{website}\n password:{password}")
        else:
            messagebox.showinfo(title="website",message="sorry, no such website found ")            

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("password genertor")
window.config(padx=50, pady=50)

canvas=Canvas(width=200, height=200,  highlightthickness=0)
lock_image=PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_image)
canvas.grid(column=1, row=0)


       
website_label=Label(text="Website:")
website_label. grid(column=0, row=1)
email_label=Label(text="email/username:")
email_label. grid(column=0, row=2)
password_label=Label(text="password:")
password_label. grid(column=0, row=3)

gen_pass_button=Button(text="generate password",command=Password_Generator )
gen_pass_button. grid(column=2, row=3)
add_button=Button(text="add", width=43, command=save)
add_button. grid(column=1, row=4, columnspan=2)
search_button=Button(text="search",width=15,command=find_password)
search_button.grid(column=2,row=1)

web_input=Entry(width=25)
web_input.grid(column=1, row=1)
web_input.focus()
mail_input=Entry(width=52)
mail_input.grid(column=1, row=2, columnspan=2)
mail_input.insert(0,"gela.3487@gmail.com")
password_input=Entry(width=25)
password_input.grid(column=1, row=3)




window.mainloop()