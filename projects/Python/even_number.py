answer=0
even=0
odd=0
while(answer==0):
    number = int(input("Choose a number: "))
    if(number%2==0):
        print("This number is even")
        even=even+1
    else:
        print("This number is odd")
        odd=odd+1
    print(f"{even} even numbers and {odd} odd numbers have benn read")
    answer=int(input("Do you want to choose another number? \n 0=yes \n 1=no \n --> "))

