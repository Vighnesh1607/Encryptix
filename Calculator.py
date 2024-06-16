def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Cannot divide by 0"
    return a // b
try:
  while True:
    print("Options :")
    print("Enter 1. for adition")
    print("Enter 2. for substraction")
    print("Enter 3. for Multiplication")
    print("Enter 4. for division")
    print("Enter 5. Exit")

    user_input = input(":")

    if user_input == "5":
       break

    if user_input in ("1","2","3","4"):
        num1 = float(input("Enter first number :"))
        num2 = float(input("Enter second number :"))

        if user_input == "1" :
            print("result:",add(num1,num2))

        elif user_input == "2" :
            print("result:",substract(num1,num2))

        elif user_input == "3" :
            print("result:",multiply(num1,num2))

        elif user_input == "4" :
            print("result:",divide(num1,num2))

        else:
            print("Invalid input...")
except:
    print("Please enter valid number ")

        


