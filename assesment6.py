def function():
    a=10
    b=20
    c=10
    if a>b and a>c:
        print("a is greater")
    elif b>a and b>c:
        print("b is greater")
    else:
        print("c is greater")
function()
def distinct_list(list1):
    distinct_list=[]
    for i in list1:
        if i not in distinct_list:
            distinct_list.append(i)
    return distinct_list
list1=[1,2,3,4,5,2,3,4]
print(distinct_list(list1))
def multiply(list1):
    result=1
    for i in list1:
        result=result*i
    return result
list1=[1,2,3,3]
print(multiply(list1))
print("reverse string")
a='somya'
for i in range(-1,-6,-1):
    print(a[i],end="")
print("\n")
print("even")
def even(list1):
    even=[]
    for i in list1:
        if i%2==0:
            even.append(i)
    return even
list1=[1,2,3,4,5,6,7,8]
print(even(list1))
print("prime number")
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(prime(11))
print("upper and lower")
def count_case(str1):
    upper_count = 0
    lower_count = 0

    for i in str1:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1

    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)

count_case("Hello World")
print("\n")
print("factorial")
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
num = 5
print("Factorial of", num, "is", factorial(num))
print("number falls")
def numberfalls(n):
    if 10 <= n <= 50:
        return " is between 10 and 50"
    else:
        return "number is not between 10 and 50"

print("25",numberfalls(25))
print("5",numberfalls(5))





