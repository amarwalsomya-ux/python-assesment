def kaprekar(num):
    while num != 6174:
        a = int("".join(sorted(str(num).zfill(4))))
        b = int("".join(sorted(str(num).zfill(4), reverse=True)))

        num = b - a
        print(b, "-", a, "=", num)

    print("Kaprekar Constant =", num)

n = int(input("Enter a 4-digit number: "))
kaprekar(n)
