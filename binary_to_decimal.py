def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        if digit == '1':
            decimal += 2 ** power
        power -= 1
    return decimal
def main():
    binary = input("Enter the binary number: ")
    decimal = binary_to_decimal(binary)
    print("The converted decimal number is ",decimal)
if __name__ == "__main__":
    main()
    