def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
def main():
    num=int(input("Enter the number to check if it is prime or not: "))
    if is_prime(num):
        print("The entered number ",num," is prime.")
    else:
        print("The entered number ",num," is not prime.")
if __name__ == "__main__":
    main()
