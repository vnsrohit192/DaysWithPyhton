
import datetime as dt
import smtplib
import pandas as pd
import random

curr=dt.datetime.today()
today_tuple=(curr.month,curr.day)

b_data=pd.read_csv("birthdays.csv")
dict_data={(data_row["month"],data_row["day"]):data_row for(index,data_row) in b_data.iterrows()}

if today_tuple in dict_data:
        
    birthday_person_details=dict_data[today_tuple]
    Name=birthday_person_details["name"]    
    letters=("letter_1.txt","letter_2.txt","letter_3.txt",)
    selected_letter=random.choice(letters)
    with open(f"letter_templates/{selected_letter}","r") as f:
        r=f.read()
    replaced=r.replace("[NAME]",Name)

    my_mail="rohit.vns516@gmail.com"
    password="my_password"    

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_mail,password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=birthday_person_details["email"],
            msg=f"Subject:happy birthday\n\n{replaced}")
        connection.close()

  
