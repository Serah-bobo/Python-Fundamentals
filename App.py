import random
#variables
#float
a= 3.5
#boolean
is_true= True
#number
age= 22
#string
name= "   Serah"
#string methods
#taking length
print(len(name))
#index
print(name[0])
#slicing
print (name[0:4])
print (name[:4])
#formatted string
print(f"my name is {name} and my age is {age}")
#methods
print(name.upper())
print(name.lower())
print(name.title())
#strip is used to trim any white spaces
print(name.strip())
#find() to find string of a character
#replace() a character
#in find a char
print("ah" in name)
#complex numbers
x= a+2j
#exponential
print(3**2)
#number methods
d=2.9
print(round(d))
print(round(d))
#primitive data types are simple and predefined example numbers,strings,boolean
#conditional statements
#if-elif-else
marks=40
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade E")
#loops
#for loop iterates over a sequence of known iterations
#while loop repeat it as long is true iterations not known
# Generate a random number between 1 and 20
number_to_guess = random.randint(1, 10)
guess = 0  # initialize with a number that is not equal to number_to_guess
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 20. Try to guess it!")

# Loop until the user guesses correctly
while guess != number_to_guess:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")

print("Congratulations! You guessed the number", number_to_guess, "in", attempts, "tries.")
#even number
count= 0
for i in range(1,10):
    if i % 2 == 0:
        count +=1
        print(i)
print(f"we have {count} even numbers")