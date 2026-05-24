#  first Python code & Comments
print("Hello World!")  # This prints a message to the screen

# Variables and Data Types
name = "Vandana"       # String (Text)
age = 17            # Integer (Whole number)
price = 99.99        # Float (Decimal number)
is_coding = True     # Boolean (True/False)
print(type(name))

# Typecasting (Converting one type to another)
x = "5"
y = "10"
print(x + y)        # Output: 510 (Strings are concatenated)
print(int(x) + int(y))  # Output: 15 (Converted strings to integers to add them)

# Taking User Input
user_name = input("Enter your name: ")
print("Welcome", user_name)

# String Slicing
fruit = "Mango"
print(fruit[0:3])  # Output: Man (Starts at index 0, goes up to but not including 3)
print(len(fruit))  # Output: 5 (Length of the string)

# String Methods
text = "  hey vandana!  "
print(text.upper())        # "  HEY VANDANA!  " (Converts to uppercase)
print(text.lower())        # "  hey vandana!  " (Converts to lowercase)
print(text.capitalize())   # "  hey vandana!  " (Capitalizes the first letter)
print(text.count("v"))     # 1 (Counts occurrences of "v")
print(text.endswith("!"))   # True (Checks if the string ends with "!")
print(text.find("Vandana"))   # 5 (Finds the starting index of "harry")
print(text.isalnum())      # False (Checks if all characters are alphanumeric)
print(text.isalpha())      # False (Checks if all characters are alphabetic)
print(text.islower())      # False (Checks if all characters are lowercase)
print(text.isprintable())    # True (Checks if all characters are printable)
print(text.isspace())      # False (Checks if all characters are whitespace)
print(text.istitle())      # False (Checks if the string is a title)
print(text.startswith("hey")) # True (Checks if the string starts with "hey")
print(text.swapcase())     # "  HEY VANDANA!  " (Swaps uppercase and lowercase)
print(text.title())        # "  Hey Vandana!  " (Capitalizes the first letter of each word)
print(text.split(" "))     # ['', 'hey', 'Vandana!', ''] (Splits the string by spaces)
print(text.strip())        # "hey Vandana!" (Removes extra spaces from sides)
print(text.rstrip())       # "  hey Vandana!" (Removes extra spaces from the right)
print(text.lstrip())       # "hey Vandana!  " (Removes extra spaces from the left)
print(text.replace("hey", "hi"))     # "  hi Vandana !  " (Replaces words)      


# If, Else
age = int(input("Enter your age: "))

if age >= 18:
    print("You can drive!")
else :
    print("you can't drive.")

# Short Hand If Else
a = 10
b = 20
print("A") if a > b else print("B")  


# If, else ,elif
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A (Excellent)")
elif marks >= 80:
    print("Grade: B (Good)")
elif marks >= 70:
    print("Grade: C (Average)")
else :
    print("Grade: D (Needs Improvement)")

# For Loop and Range
print("Count 1 to 5:")
for i in range(1, 6):  # Starts at 1, stops before 6
    print(i)

# While Loop
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count = count - 1  # Reduces count so loop eventually stops

# For Loop with Else
for i in range(5):
     print(i)
else:
     print("Loop completed!")
  
# Break and Continue
for number in range(1, 6):
    if number == 3:
        continue  # Skip 3 and move to the next number
    if number == 5:
        break     # Stop the loop completely when hitting 5
    print("Number:", number)

# Defining a simple function
def calculate_gmean(a, b):
    mean = (a * b) / (a + b)
    print("The geometric mean is:", mean)
    return mean
def is_greater(a, b) :
    if(a>b):
        print("First number is greater")
        return True
    else :
        print("Second number is greater")
        return False
def is_lesser(a, b) :
    pass
def average(*numbers) :
    sum = 0
    for i in numbers :
        sum = sum + i
    return sum / len(numbers)

# Calling the function with different values
calculate_gmean(9, 8)
is_greater(4, 5)
is_lesser(4, 5)
c = average(5, 6, 7, 1)
print(c)


# Introduction to Lists
marks = [75, 82, 94, 65]
print(marks[2])  # Output: 94 (Index starts at 0)

# List Methods
marks.append(99)   # Adds 99 to the end of the list
marks.sort()       # Sorts the list in ascending order
marks.reverse()    # Reverses the order of items
marks.insert(2, 88) # Inserts 88 at index 2
marks.pop(1)       # Removes the item at index 1
marks.remove(65)    # Removes the first occurrence of 65
marks.clear()       # Removes all items from the list
marks.extend([70, 80, 90])  # Adds multiple items to the list
marks[0] = 100  # Updates the first item to 100
marks[1:3] = [200, 300]  # Updates items from index 1 to 2
marks[1:3] = [200, 300, 400]  # Updates items from index 1 to 2 and adds a new item
marks[1:3] = []  # Removes items from index 1 to 2
print("Updated List:", marks)


# Tuples (Use parenthesis instead of square brackets)
coordinates = (10, 20, 30)
# coordinates[0] = 50  <-- This will cause an ERROR because you cannot change a tuple!

# Tuple Operations
# To change a tuple, you must convert it to a list first, change it, and convert it back:
temp_list = list(coordinates)
temp_list.append(40)
coordinates = tuple(temp_list)
print("Updated Tuple:", coordinates)

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Combined Tuple:", combined_tuple)


# Introduction to Dictionaries
student_info = {
    "name": "Rohan",
    "age": 25,
    "city": "New York"
}
print(student_info["name"])
print(student_info.get("age"))
# Dictionary Methods
student_info["age"] = 26  # Updates the age
student_info["city"] = "USA"  # Adds a new key-value pair
print(student_info)
# let we have data of 2 employees
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

ep1.update (ep2)
#ep1.clear()
ep1.pop(122)
del ep1[123]
print(ep1)

# File Handling

# Open a file in read mode
# before running this code make sure that you have created a file named myfile.txt in the same directory as this Python file.
f = open('myfile.txt', 'r')
print(f)
text = f.read()
print(text)
f.close()
# Open a file in write mode
f = open('myfile.txt', 'w')
f.write("Hello, World!")
f.close()
# Open a file in append mode
f = open('myfile.txt', 'a')    
f.write("\nAppending a new line.")
f.close()

# Using 'with' statement (automatically closes the file)

with open('myfile.txt', 'r') as file:
   content = file.read()
   print(content)
   # Open a file in write mode
with open('myfilee.txt', 'w') as file:
   file.write("Hello, World!")
   # Open a file in append mode
with open('myfile.txt', 'a') as file:
   file.write("\nAppending a new line.")
  
# Create a file named 'myfile.txt' with the following content:

# Open the file in read mode
with open('myfile.txt', 'r') as f:
    # use a loop to read the file line by line
    for line in f:
        print(line.strip(","))
        
    while True:
        line = f.readline()
        if not line:
            break # Stop when the file ends
        print(line.strip(","))

# let we have marks of 3 students

m1 = 70,80,90
m2 = 65,75,85
m3 = 50,60,70
        
print(f"Student Marks: {m1}, {m2}, {m3}")

lines_list = ['Line 1\n', 'Line 2\n', 'Line 3\n']
# Open file in write mode ('w')
with open('myfile.txt', 'w') as f:
 f.writelines(lines_list) 
      # This automatically writes all items of the list into the file
  
 # Exception Handling
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")
  
   #  Custom Errors
age = int(input("Enter your age: "))
if age < 18:
          raise ValueError("You are underage!")
else:
          print("You are eligible.")



  

   