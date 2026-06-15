ya=[12,37,8,9,67,2,3,5,4,8,8,9,90,89,88]
sum=0
for i in a:
    sum=sum+i
print("Addition of number=",sum)
b=[10, 11, 102, [1, 2], [3, 4, 5], [6, 7]] 
print("list value =",b[4][2])
c=["Laptop", "Mouse", "Monitor", "Keyboard"]
if "Tablet" in c:
    print("valid or exist")
else: 
    print("invalid or not exist")
List=[5, 20, 15, 20, 25, 50, 20]
print(List.remove(20))
print(List)
l={"name":"somya","age":20,"city":"jaipur"}
print(l["name"],l["age"],l["city"],sep="-") 
person = {
    "name": "ABC",
    "address": {
        "city": "Jaipur"
    }
}
print(person["name"])
print(person["address"]["city"])
