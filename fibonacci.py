def fibonacci(n):
    fib_sequence = [0 , 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
    return fib_sequence[:n]
def main():
    num = int(input("Enter the term till to print the fibonacci series: "))
    fibonacci_sequence = fibonacci(num)
    print("Fibonacci series till ",num," is ",fibonacci_sequence)
if __name__ == "__main__":
    main()