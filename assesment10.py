class student:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def formula(self):
        self.p=self.length*self.breath
        self.a=2*self.length+self.breath
    def output(self):
        print("area of rectangle=",self.p)
        print("perimeter of rectangle=",self.a)
s1=student(12,2)
s1.formula()
s1.output()

print("circle")
class student:
    def __init__(self,r):
        self.r=r
    def diameter(self):
        self.d=2*self.r
    def area(self):
        self.a=22/7*self.r*self.r
    def perimeter(self):
        self.p=2*22/7*self.r
    def output(self):
        print("diameter of circle=",self.d)
        print("area of circle=",self.a)
        print("perimeter of circle=",self.p)
s1=student(12)
s1.diameter()
s1.perimeter()
s1.area()
s1.output()
print("\n")
print("product detail")
class product:
    def __init__(self):
        self.name="laptop"
        self.price=13000
        self.quantity=10
    def calculate(self):
        self.a=self.price*self.quantity
    def output(self):
        print("name of product=",self.name)
        print("price of product=",self.price)
        print("total value=",self.a)
s1=product()
s1.calculate()
s1.output()
print("\n")
print("password check")
class passwoard:
    def __init__(self,username,userpasswoard):
        self.username=username
        self.userpasswoard=userpasswoard
    def passwoard(self):
        self.inputpasswoard="abcd"
        if(self.inputpasswoard==self.userpasswoard):
            print("true")
        else:
            print("false")
    def output(self):
        print("username=",self.username)
        print("userpasswoard=",self.userpasswoard)
s1=passwoard("somya",545125)
s1.output()
s1.passwoard()


class Bank:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Withdraw successfully")
            print("Balance =", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Successfully deposited")
        print("Balance =", self.balance)


b1 = Bank("Customer", 12000, 1000)

while True:
    print("""
1. Deposit
2. Withdraw
3. Exit
""")

    c = int(input("Enter choice: "))

    if c == 1:
        amt = int(input("Enter deposit amount: "))
        b1.deposit(amt)

    elif c == 2:
        amt = int(input("Enter withdraw amount: "))
        b1.withdraw(amt)

    elif c == 3:
        print("Successfully exited")
        break

    else:
        print("Invalid choice")







