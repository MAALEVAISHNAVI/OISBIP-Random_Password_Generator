import string
import random

len = int(input("Enter length of password: "))

print("""Choose the character set :
          1.Digits
          2.Letters
          3.Special characters
          4.Exit""")

PasswordList=""

while (True):
    choice = int(input("Enter your choice: "))

    if (choice == 1):
        PasswordList += string.digits
    elif (choice == 2):
        PasswordList += string.ascii_letters
    elif (choice == 3):
        PasswordList += string.punctuation
    elif (choice == 4):
        break
    else:
        print("Please select a valid option!")

Password = []

for i in range (len):
    RandomPassword = random.choice(PasswordList)
    Password.append(RandomPassword)

print("Random Password is " + "".join(Password))

