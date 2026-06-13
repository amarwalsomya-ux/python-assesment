a=490
per=a*100/600
print("percentage of student=",per)
if per>=60:
    print("first divsion")

elif per>=50 and per<60:
    print("second divison")

elif per>=40 and per<50:
    print("third division")

else:
    print("fail")
print("table")
while True:
    num=int(input("enter value from 2 to 50"))
    if 2<=num<=50:
            break
    else:
            print("invalid input")
print("\nMultiplication Table of", num)
for i in range(1,11):
    print(num, "x", i, "=", num * i)
print("palindrome number")
a=1331
r=int(str(a)[::-1])
print(r)
if(str(a)==str(r)):
    print("Palindrome")
else:
    print("Not a Palindrome")
    
    


