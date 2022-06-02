import random
print("welcome to the Game\n")
print("Guess the number")
rnum=random.randint(1,100)
count=10
while count:
    count=count-1
    unum=int(input("enter the number\n"))
    if rnum==unum:
        print("you won")
        print(f"your score:{count}")
        break
    elif rnum>unum:
        print("too small")
    else:
        print("too large")
else:
    print("you loose")