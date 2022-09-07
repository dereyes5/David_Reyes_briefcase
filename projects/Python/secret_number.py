import random
random_number=random.randint(1,10)
print("Guess the secret number")
user_number=0;
while(user_number!=random_number):
    user_number=int(input("Choose a number: "))
    if(user_number>=0 and user_number<=11):
        if (user_number==random_number):
            print(f"Well done, the random number was {random_number}")
        else:
            print(f"No, {user_number} wasn't the secret number ")
    else:
        print(f"Number: {user_number} must be between 1 and 10")