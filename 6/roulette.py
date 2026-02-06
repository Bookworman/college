print("Wellcome to the casino Royal")
num = int(input("Enter a number a number of your slot: "))
if num == 0:
    print("It's green, take your L")
elif ((num % 2 == 0) and (1 <= num <= 10 or 19 <= num <= 28)) or ((num % 2 == 1) and (11 <= num <= 18 or 29 <= num <= 36)) :
    print("It's black, like my coffe")
elif ((num % 2 == 1) and (1 <= num <= 10 or 19 <= num <= 28)) or ((num % 2 == 0) and (11 <= num <= 18 or 29 <= num <= 36)) :
    print("It's red, sunshine is coming")
else :
    print("Whoops,is ball went on the floor? or how did ya get this number")