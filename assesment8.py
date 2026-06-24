from tkinter import *
import csv
root = Tk()
root.title("GUI form")
root.geometry("350x250")


Label(root, text="Name").place(x=20, y=80)
name_entry = Entry(root, width=30)
name_entry.place(x=120, y=80)


Label(root, text="Email").place(x=20, y=120)
email_entry = Entry(root, width=30)
email_entry.place(x=120, y=120)


Label(root, text="Number").place(x=20, y=160)
number_entry = Entry(root, width=30)
number_entry.place(x=120, y=160)


def submit():
    name = name_entry.get()
    email = email_entry.get()
    number = number_entry.get()

    print("Name:", name)
    print("Email:", email)
    print("Number:", number)
    with open("somya.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, number])
    print("data saved succesfully")

Button(root, text="Submit", command=submit).place(x=150, y=200)

root.mainloop()
