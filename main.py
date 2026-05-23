print("hello world")
print(" Here , all topics for a data analysis")
#  first Python code & Comments
print("Hello World!")  # This prints a message to the screen

# Variables and Data Types
name = "Vandana"       # String (Text)
age = 17            # Integer (Whole number)
price = 99.99        # Float (Decimal number)
is_coding = True     # Boolean (True/False)

# Typecasting (Converting one type to another)
x = "5"
y = "10"
print(int(x) + int(y))  # Output: 15 (Converted strings to integers to add them)

# Taking User Input
user_name = input("Enter your name: ")
print("Welcome", user_name)

# String Slicing
fruit = "Mango"
print(fruit[0:3])  # Output: Man (Starts at index 0, goes up to but not including 3)
print(len(fruit))  # Output: 5 (Length of the string)

# String Methods
text = "  hey harry!  "
print(text.upper())        # "  HEY HARRY!  " (Converts to uppercase)
print(text.strip())        # "hey harry!" (Removes extra spaces from sides)
print(text.replace("hey", "hi")) # "  hi harry!  " (Replaces words)

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

# Calling the function with different values
calculate_gmean(9, 8)
calculate_gmean(4, 5)

# Introduction to Lists
marks = [75, 82, 94, 65]
print(marks[2])  # Output: 94 (Index starts at 0)

# List Methods
marks.append(99)   # Adds 99 to the end of the list
marks.sort()       # Sorts the list in ascending order
marks.reverse()    # Reverses the order of items
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

# Introduction to Dictionaries
student_info = {
    "name": "Harry",
    "age": 25,
    "city": "New York"
}
print(student_info["name"])
print(student_info.get("age"))
# Dictionary Methods
student_info["age"] = 26  # Updates the age
student_info["country"] = "USA"  # Adds a new key-value pair
print(student_info)

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

ep1.update (ep2)
ep1.clear()
ep1.pop(122)
del ep1[123]
print(ep1)

# File Handling

# Open a file in read mode
with open('example.txt', 'r') as file:
   content = file.read()
   print(content)
   # Open a file in write mode
with open('example.txt', 'w') as file:
   file.write("Hello, World!")
   # Open a file in append mode
with open('example.txt', 'a') as file:
   file.write("\nAppending a new line.")
  
# Create a file named 'marks.txt' with the following content:

# Open the file in read mode
with open('marks.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break # Stop when the file ends

          
m1 = 70,80,90
m2 = 65,75,85
m3 = 50,60,70
        # Split the line by commas to get individual marks
m1 = line.split(",")[0]
m2 = line.split(",")[1]
m3 = line.split(",")[2]
print(f"Student Marks: {m1}, {m2}, {m3.strip()}")

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



  

   #  Lambda Functions
double = lambda x: x * 2
print(double(5))  # Output: 10

   # Filter, Reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
   # is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (Values are equal)
print(a is b)  # False (Different objects in memory)
   

# 1. Create the decorator function
def greet_decorator(original_function):
    def modified_function():
        print("Hello! Good Morning.") # Extra behavior before
        original_function()           # Running the actual function
        print("Thanks for using this function.\n") # Extra behavior after
    return modified_function

# 2. Use the decorator using the @ symbol
@greet_decorator
def hello():
    print("I am Harry.")

@greet_decorator
def main_work():
    print("I am writing code.")

# 3. Call the functions
hello()
main_work()

class Employee:
  def __init__(self, name, base_salary):
      self.name = name
      self._salary = base_salary # Internal variable

  # GETTER: Allows us to read the salary like a property, not a method
  @property
  def total_salary(self):
      return self._salary

  # SETTER: Allows us to safely update the salary with conditions
  @total_salary.setter
  def total_salary(self, new_salary):
      if new_salary < 0:
          print("Error: Salary cannot be negative!")
      else:
          self._salary = new_salary

# Using the class
emp = Employee("Rohan", 50000)

# Calling the Getter (Notice: No brackets () used here)
print(f"{emp.name}'s salary is: {emp.total_salary}") 

# Calling the Setter to change the value
emp.total_salary = 60000
print(f"Updated salary: {emp.total_salary}")

# Testing validation
emp.total_salary = -1000 # Prints error message

# Parent Class
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_details(self):
        print(f"The Employee ID is {self.id} and Name is {self.name}")

# Child Class (Inherits from Employee)
class Programmer(Employee):
    def show_language(self):
        print("The default language is Python")


# 1. Creating an object of the Parent Class
e1 = Employee("Harry", 400)
e1.show_details()

# 2. Creating an object of the Child Class
e2 = Programmer("Lovish", 412)
e2.show_details()    # Works because Programmer inherited this from Employee!
e2.show_language()   # Works because this belongs to Programmer
