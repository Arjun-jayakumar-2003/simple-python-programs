def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary
def main():
    decimal = int(input("Enter the decimal number: "))
    binary = decimal_to_binary(decimal)
    print("The converted binary number is ",binary)
if __name__ == "__main__":
    main()
    