import random

print("Welcome to the password generator!")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v", "w", "x", "y", "z"]

symbols = ["!", "@", "#", "$", "%", "&", "*"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

password = ""

numOfLetters = int(input("How many letters would you like: "))

for i in range(0, numOfLetters):
    val = random.choice(letters)
    password += val

numOfSymbols = int(input("How many symbols would you like: "))

for i in range(0, numOfSymbols):
    val = random.choice(symbols)
    password += val

numOfNumbers = int(input("How many numbers would you like: "))

for i in range(0, numOfNumbers):
    val = random.choice(numbers)
    password += val

print("Password: {}".format(password))