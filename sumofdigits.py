def sum_of_digits(n):
    total_sum = 0
    while n > 0:
        digit = n % 10
        total_sum += digit
        n //= 10
    return total_sum
def main():
    number = int(input("Enter the number whoose digits sum is to be found: "))
    sum = sum_of_digits(number)
    print("The sum of the digits of the number ",number," is ",sum)
if __name__ == "__main__":
    main()
