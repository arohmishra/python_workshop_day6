import random 

guess_num = int(input("enter a number between 1-10 untill you get it right:"))
num = random.randint(1,10)

while num != guess_num:
    print("try again!")
    guess_num = int(input("enter a number between 1-10 :"))

print("well guessed!")