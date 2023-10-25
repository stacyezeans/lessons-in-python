#Function to add two numbers
def add(x,y):
    return x + y
#Function to subtract two numbers
def subtract(x,y):
    return x - y
#Function to multiply two numbers
def multiply(x,y):
    return x * y
#Function to divide two numbers
def divide(x,y):
    if y==0:
        return "cannot divide by zero"
    return x/y
#Main function
def main():
    print("select operation:")
    print("1. Add")
    print("2. Subtract")
    print ("3. Multiply")
    print("Divide")

    choice = input("Enter choice(1/2/3/4):")
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    if choice == '1':
        result = add(num1, num2)
    elif choice =='2':
        result = subtract (num1, num2)
    elif choice == '3':
        result = multiply(num1, num2) 
    elif choice == '4':
        result = divide(num1, num2)
    else:
        result ="Invalid input"

    print("Result: ", result)
    --name-- =="--main--":
    main()
    
              