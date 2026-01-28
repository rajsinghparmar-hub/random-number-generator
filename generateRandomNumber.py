import random as ran

def generate_randomNumber():
    return ran.randint(1000, 99999)
    
    
while True:
    print("New number: ", generate_randomNumber())
    
    choice = input("Run again: you need to type small n to exit the program(y/n)")
    if choice == "n":
        break