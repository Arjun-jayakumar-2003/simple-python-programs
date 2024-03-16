def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    armstrong_sum = 0
    for digit_str in num_str:
        digit = int(digit_str)
        armstrong_sum += digit ** num_len
    if armstrong_sum == num:
        return True
    else:
        return False
def main():
    number = int(input("Enter the number to be checked to see if it is armstrong number: "))
    if is_armstrong(number):
        print("Entered number is armstrong number.")
    else:
        print("Entered number is not armstrong number.")
if __name__ == "__main__":
    main()
