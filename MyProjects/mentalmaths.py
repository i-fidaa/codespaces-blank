import random
correct = True
score = 0
while correct :
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    product = number1 * number2
    print(f"{number1} x {number2}")
    answer = int(input(""))
    if answer == product :
        print("Correct!")
        score += 1
    else:
        correct = False #or break
        print(f"Incorrect! The correct answer was {product}")
        print(f"Score: {score}")