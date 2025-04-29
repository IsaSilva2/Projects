import string

print("Hi there.\n\nI need some information to learn the codes. So I'm gonna ask you some questions.\nLet's begin!")

a = input("\nWhat is your name? ")
b = input("How old are you? ")

print(a + " " + b)

print("\nAt this point I'm gonna double the number you choose")

n1 = int(input("Enter a number: "))
double = n1 * n1

print(f"\nYour number is {double}")

print("\nNow, I'm gonna calculate the value of the area of the square. So, please choose a number.")

n2 = float(input("Enter the number here: "))
square = n2 ** 2

print(f"\nThe value of the are of the square is {square}")

print("\nI need your name to be spelled correctly, BUT I'm gonna use a code for that. So, please wrtie your name ")

name = input("Enter your full name:\n")

print("\nThis is your name spelled correctly:")
print(f"{name}".title())

print("\n\nFinally, I'm gonna count the characters and the letters of your name.")

numname = len(name)

print(f"\nYour name has {numname} characters")

'''
Um bônus
'''
letters = [c for c in name if c.isalpha()]

print(f"\nAnd the total of letters in your name is:", len(letters))