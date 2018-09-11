

"""
Odd and Even

num = raw_input("Please enter a number: ")

num = int(num)

if num % 2 == 0:
    print "Your number is even!"
else:
    print "Your number is odd!" """
    
"""Extra 2: If the number is a multiple of 4, print a different message."""
num = raw_input("Please enter a number: ")

num = int(num)
if num % 4 == 0:
    print "Your number is a multiple of 4."
elif num % 2 == 0:
    print "Your number is even!"
else:
    print "Your number is odd!"
    
"""Extra 3: Ask the user for two numbers, if one number divides into the other,
print a message, if not, print a different message."""

check = int(raw_input("Please enter a check number: "))
num = int(raw_input("Please enter another number: "))

if num % check == 0:
    print (str(check) +" divides into " + str(num) +".")
else:
    print (str(check) +" doesn't divide into " + str(num)+".")
