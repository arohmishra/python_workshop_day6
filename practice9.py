num = int(input("enter the number:"))

if num >= 1500 and num <=2700:
    if num % 7 ==0 and num % 5 ==0:
       print(f"{num} is diviseible by 7 and multiple of 5.")
    elif  num % 7 ==0 and num % 5 !=0:
        print(f"{num} is divisible by 7 but not a multiple of 5")
    elif  num % 7 !=0 and num % 5 ==0:
        print(f"{num} is not divisible by 7 but a multiple of 5")
    else:
        print(f"{num} is neither divisible by 7 nor a multiple of 5")
else:
    print(f"{num} is not in the required range") 
