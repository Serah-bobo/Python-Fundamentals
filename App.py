'''
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
guess = 0
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
'''
#lists are pordered mutable collections
'''
fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # apple
print(fruits[0:2])#returns upto -1 index
fruits.append("mango") # add item at end
fruits.insert(1, "peach")
print(fruits)
fruits.remove("banana")# remove item
print(len(fruits))     # length
print(fruits[1:3])     # slicing
fruits[0] = "kiwi"     # modify
fruits.pop()#remove and end
print(fruits)
print("mango" in fruits) # check existence
#finding largest number in a list
largest_number=[20,35,0,140,67,89,900]
max=largest_number[0]
for number in largest_number:
    if number > max:
        max=number
print(max)
#2D lists are lists within a list
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])#it prints 2 first row  second index
for row in matrix:
    for column in row:
        print(column)
#sort
numbers=[2,1,6,9,0,3,2,1,5,70]
#numbers.sort()
#numbers.reverse()
#print(numbers)
#remove duplicates
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        print(uniques)

#tuples are lists that are immutable
grades=("A","A","B","C","D","E","F")
print(grades.count("A"))
print(grades[0])
#sets are unordered unique collection meaning no specific index and dont allow duplicates
number_set={1,3,4,5,6,7,8,9}
print(number_set)
number_set.add(10)       # add item
number_set.remove(3)    # remove item
print(len(number_set))  # length
print(2 in number_set)  # check if item exists

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # Union {1, 2, 3, 4, 5}
print(a & b)   # Intersection {3}
print(a - b)   # Difference {1, 2}
#dictionaries store data in key-value pair
student = {
    "name": "Serah",
    "age": 22,
    "course": "Python"
}
print(student["name"])         # Access value
student["age"] = 23            # Update value
student["grade"] = "A"         # Add new key-value
print(student)
student.pop("course")          # Remove key
print(student.keys())          # All keys
print(student.values())        # All values
print(student.items())         # Key-value pairs
print("age" in student)        # Check key existence
'''
#contact book
contacts = {}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == "2":
        if contacts:
            print("\n--- All Contacts ---")
            for name, phone in contacts.items():
                print(name, ":", phone)
        else:
            print("No contacts found.")

    elif choice == "3":
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print("Found:", search_name, "->", contacts[search_name])
        else:
            print("Contact not found.")

    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print(delete_name, "deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-5.")
