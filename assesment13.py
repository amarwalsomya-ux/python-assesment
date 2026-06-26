class Tempreature:
    def __init__(self,celsius):
        self.celsius=celsius
    def to_fahrenheit(self):
        self.fahrenheit=(self.celsius*9/5)+32
        #print("celsius to faharenite:",fahrenheit)
    def to_kelvin(self):
        self.kelvin=self.celsius+273.15
        #print("celsius to faharenite:",kelvin)
    def output(self):
        print("tempreature to celsius",self.celsius,"°c")
        print("ctof:",self.fahrenheit,"°f")
        print("ctok:",self.kelvin,"°k")
t=Tempreature(50)
t.to_fahrenheit()
t.to_kelvin()
t.output()
print("simple and compound interset")
from tkinter import *
import csv

def simple():
    p = float(e1.get())
    r = float(e2.get())
    t = float(e3.get())

    si = (p * r * t) / 100
    result.config(text="Simple Interest = " + str(si))

    with open("interest.csv", "a", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Simple Interest", p, r, t, si])

def compound():
    p = float(e1.get())
    r = float(e2.get())
    t = float(e3.get())

    ci = p * (1 + r / 100) ** t - p
    result.config(text="Compound Interest = " + str(round(ci, 2)))

    with open("interest.csv", "a", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Compound Interest", p, r, t, round(ci, 2)])

root = Tk()
root.title("Interest Calculator")
root.geometry("350x250")

Label(root, text="Principal").pack()
e1 = Entry(root)
e1.pack()

Label(root, text="Rate").pack()
e2 = Entry(root)
e2.pack()

Label(root, text="Time").pack()
e3 = Entry(root)
e3.pack()

Button(root, text="Simple Interest", command=simple).pack(pady=5)

Button(root, text="Compound Interest", command=compound).pack(pady=5)

result = Label(root, text="")
result.pack()

root.mainloop()
class coffeeshop:
    def __init__(self,water,cofee,milk):
        self.water=water
        self.cofee=cofee
        self.milk=milk
    def make_latte(self):
        if self.water>=300 and self.cofee>=100 and self.milk>=200:
            print("latte is ready")
            print("water=",self.water,"ml")
            print("cofee=",self.cofee,"g")
            print("milk=",self.milk,"ml")
        else:
            print("not proper")
t=coffeeshop(300,100,200)
t.make_latte()
print("vechile")
class vechile:
    def __init__(self,name,max_Speed):
        self.name=name
        self.max_speed=max_Speed
    def display(self):
        print("name:",self.name)
        print("name:",self.max_speed)
class bus(vechile):
    def __init__(self,name,max_speed,seatingcapacity,reservation):
        vechile.__init__(self,name,max_speed)
        self.seatingcapacity=seatingcapacity
        self.reservation=reservation
    def display(self):
        vechile.display(self)
        print("seatingcapacity:",self.seatingcapacity)
        print("reservation:",self.reservation)

t= bus("volvo",189,65,"available")
t.display()






























