from palindrome import is_palindrome
user_input = input("Enter the string whose palindrome is to be found: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrone.")
