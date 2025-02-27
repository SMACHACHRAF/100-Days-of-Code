print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 #initialisation de bill
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
    photo=input("do want to have a  photos ! type yes or no ")
    if photo =="yes":
    #add 3$ to there bill
        bill = bill + 3 #bill += 3
    print(f"your final bill to pay is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
