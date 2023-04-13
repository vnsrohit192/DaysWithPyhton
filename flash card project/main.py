from tkinter import*
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
new_data={}

try:
    data=pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    new_data=original_data.to_dict(orient="records")
else:      
    new_data=data.to_dict(orient="records")



def next_card():
    global current_card ,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(new_data)
    canvas.itemconfig(title_canvas, text="french",fill="black")
    canvas.itemconfig(french_canvas,text=current_card["French"],fill="black")
    canvas.itemconfig(card_baground, image=front_card)
    flip_timer=window.after(3000,func=flip_crad)

def flip_crad():
    canvas.itemconfig(title_canvas,text="English",fill="white") 
    canvas.itemconfig(french_canvas,text= current_card["English"], fill="white")
    canvas.itemconfig(card_baground,image=back_card)  





def del_data():
   
    removed_item=new_data.remove(current_card)
    print(len(new_data))
    data=pandas.DataFrame(new_data)
    data.to_csv("data/word_to_learn.csv",index=False)
    next_card()
    



window=Tk()
window.title("flash_card_game")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_crad)

canvas=Canvas( width=800,height=526)
front_card=PhotoImage( file="images\card_front.png")
back_card=PhotoImage(file="images/card_back.png")
card_baground=canvas.create_image(400,263, image=front_card)
title_canvas=canvas.create_text(400,150,text="french",font=("areal",20,"italic"))
french_canvas=canvas.create_text(400,263,text="hello",font=("areal",40,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)


wrong_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0, command=next_card)
wrong_button.grid(column=1,row=1)
right_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_image,highlightthickness=0,command=del_data)
right_button.grid(column=0,row=1)

next_card()


window.mainloop()