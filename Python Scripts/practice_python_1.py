from datetime import date

name = raw_input("What's your name?: ")

age = int(input("How old are you?: "))

year = date.today().year + 100 - age

print(name +  " will turn 100 years old in "+ str(year))

"""Extra 2: Add on to the previous program by asking the user for another number 
and printing out that many copies of the previous message."""

num = raw_input("Plese write number: ")

print(name +  " will turn 100 years old in "+ str(year)*int(num))

"""Extra 3: Print out the messaage that many times on separate lines."""

print(name +  " will turn 100 years old in "+ str(year)+"\n")*int(num)