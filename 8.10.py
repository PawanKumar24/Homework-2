# Pawan Kumar
# ID: 2046222
string = str(input())
spaceless_string = string.replace(" ", "")
temp = spaceless_string[::-1]

if spaceless_string == temp:
    print(f'{string} is a palindrome')
else:
    print(f'{string} is not a palindrome')