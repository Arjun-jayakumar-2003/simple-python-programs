def main():
    print("Simple calculator.")
    print("Choose operation.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("enter the operation(1/2/3/4): "))
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if choice == 1:
        print("The sum is ",add(num1 , num2))
    elif choice == 2:
        print("The difference is ",sub(num1 , num2))
    elif choice == 3:
        print("The product is ",mul(num1 , num2))
    elif choice == 4:
        print("The quotient is ",div(num1 , num2))
    else:
        print("Invalid input.")
def add(a , b):
    return a + b
def sub(a , b):
    return a - b
def mul(a , b):
    return a * b
def div(a , b):
    if b == 0:
        return "Error: division by zero"
    else:
        return a / b
if __name__ == "__main__":
    main()