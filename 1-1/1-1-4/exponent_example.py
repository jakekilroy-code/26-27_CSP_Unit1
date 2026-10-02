#variable to hold solution
product = 1

#Get user input for the base and the exponent
base = int(input("what is the base of your problem? "))
exponent = int(input("what is the exponent? "))

#write a loop to run exponent times and multiply by the base
for l in range(exponent):
    product *= base
print(product)