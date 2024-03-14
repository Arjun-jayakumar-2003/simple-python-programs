def sum_of_natural_numbers(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total
def main():
    number = int(input("Enter the natural number til sum is to be found"))
    sum = sum_of_natural_numbers(number)
    print("The sum of the first natural numbers tll ",number," is ",sum)
if __name__ == "__main__":
    main()