def factorial(n):
    if n < 0:
        print("entered number is negative can't find it's factorial.")
    elif n == 0:
        return 1
    else:
        total = 1
        for i in range(1 , n + 1):
            total *= i
        return total
def main():
    number = int(input("Enter the number whoose factorial is to be found: "))
    sum = factorial(number)
    print("the factorial of ",number," is",sum)
if __name__ == "__main__":
    main()