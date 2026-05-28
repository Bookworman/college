
print("is's super secret program with password(4590)")
password = int(input("enter password: "))
if password == 4590:
    print("whoah, from first try? you're boring")
else:
    while True:
        password = int(input("nah,try again: "))
        if password == 4590:
            print("yay, you've finally made it")
            break