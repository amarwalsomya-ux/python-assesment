print("file mode")
import csv

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        mobile = input("Enter Mobile Number: ")
        email = input("Enter Email: ")

        contact = [name, mobile, email]

        file = open("address_book.csv", "a", newline="")
        writer = csv.writer(file)
        writer.writerow(contact)
        file.close()

        print("Contact added successfully.")

    elif choice == 2:
        file = open("address_book.csv", "r")
        reader = csv.reader(file)

        print("\nName\tMobile\tEmail")
        for row in reader:
            print(row[0], "\t", row[1], "\t", row[2])

        file.close()

    elif choice == 3:
        print("Program exited.")
        break

    else:
        print("Invalid choice.")
