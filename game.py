import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("Guess the number!"))
    if user == number:
        print("Congratulations!!")
        print(f"You have guessed the correct number, the number is {number}")
        break
if user != number:
    print(f"Oh no! Your guess is incorrect, the number is {number}")
