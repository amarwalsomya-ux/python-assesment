print("tuple program")
t = ("somya", "dev", "amarwal")
print(3 * t)

a = ("apple", "mango", "orange")
print("1 tuple value =", a)

b = ("banana", "grapes", "guava")
print("2 tuple value =", b)

c = ("watermelon", "muskmelon")
print("3 tuple value =", c)

d = a + b + c
print("after concatenation of tuple =", d)

print()
print("using if")
if "apple" in a:
    print("valid or exist")
else:
    print("invalid or not exist")

print()
print("calculation of number")
number = (12, 14, 18, 1,19, 10, 87, 89)

sum = 0
h = number[0]
l = number[0]
result = 0

for i in number:
    sum = sum + i

print("sum of number =", sum)

for i in number:
    if i > h:
        h = i
    if i < l:
        l = i

print("highest number =", h)
print("lowest number =", l)

print()

for i in number:
    if i < 10:
        result = result + i

print("sum of number less than 10 =", result)
print()
s={"cat","dog","bird","fish"}
len=0
for i in s:
   len=len+1
print("number of element in a set =",len)
print()
print("combining two sets")
a={12,14,18,19,21}
b={21,22,24,26,78}
c=a.union(b)
print("union of number=",c)
common=a & b
print("common number=",common)
d=a^b
print("different number from and b=",d)
update=a.update(b)
print("update of number a=",a)
