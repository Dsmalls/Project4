import math

print("ceiling(4.4) = ", math.ceil(4.4))
print("floor(4.4) = ", math.floor(4.4))
print("fabs(-4.4) = ", math.fabs(-4.4))

# Factorial = 1 * 2 * 3 * 4
print("factorial(4) = ", math.factorial(4))

# Receive a float and return an int
print("trunc(4.2) = ", math.trunc(4.2))

# Return x^y
print("pow(2,2) = ", math.pow(2,2))

# Defining a base and 10^3 = 1000
print("log(1000, 10) = ", math.log(1000,10))

from decimal import Decimal as D

sum = D(0)
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum -= D("0.03")
print('====================================================')




#============Exceptions Examples========================
while True:

    try:
        number = int(input("Please enter a number here : "))
        break

    except ValueError:
        print("Number wasn't entered")

    except:
        print("An unknown error occurred")

print("Thank you for entering a number")
print('======================================')

secret_number = 7

while True:
    guess = int(input("Guess the number between 1 and 10 : "))

    if guess == secret_number:
        print("You guessed correctly")
        break