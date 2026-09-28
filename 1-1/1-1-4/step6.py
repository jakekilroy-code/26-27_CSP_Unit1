#   a114_divisible.py

# get two numbers from user
num1 = int(input("Please input a number"))
num2 = int(input("Please input another number"))
# loop while the numbers are not divisible (the remainder is not 0)
while num1 % num2 != 0:
    # inform user of result
    print("Those numbers are not divisible evenly")

    # gather user input again
    num1 = int(input("Please input a number"))
    num2 = int(input("Please input another number"))

# Inform the user they succeeded
print("Those numbers are divisible")
