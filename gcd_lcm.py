def gcd(a , b):
    while b != 0:
        a , b = b , a % b
    return a
def lcm(a , b):
    return (a * b) // gcd(a , b)
def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    gcd_result = gcd(a , b)
    lcm_result = lcm(a , b)
    print("The greatest common divisor of ",a," and ",b," is ",gcd_result)
    print("The least common multiple of ",a," and ",b," is ",lcm_result)
if __name__ == "__main__":
    main()