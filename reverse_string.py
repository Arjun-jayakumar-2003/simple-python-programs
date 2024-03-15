def reverse_string(s):
     cleaned_string = ''.join(char for char in s if char.isalpha())
     return cleaned_string[::-1]
def main():
     s = input("Enter the string to be reversed: ")
     r = reverse_string(s)
     print(f"The reversed string of the given string {s} is {r}.")
if __name__ == "__main__":
     main()