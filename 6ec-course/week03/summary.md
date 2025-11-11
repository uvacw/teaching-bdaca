# Summary of Week 1's Content
Major topics include: data types, loops and conditional statements, and functions and methods.

## Data types

**An overview of the most common data types in Python**
| Type       | Examples             |
|------------|----------------------|
| Text       | `str`                |
| Numeric    | `int`, `float`       |
| Sequence   | `list`, `tuple`      |
| Mapping    | `dict`               |
| Set        | `set`                |
| Boolean    | `bool`               |

Function to check data type: `type()`

It is very intuitive to understand `int` and `float`, so I'll only give examples and explain the remaining data types.

### Strings (`str`)
```python
my_text = "Hello world."
next_text = 'It is fun to learn Python.'
print(type(my_text)) # Check the data type
print(type(next_text)) # Save as above
```

Both `"` and `'` can be used to denote strings. If the apostrophe character is part of the string, use `"`:
```python
example = "It's fun to learn Python."
```

### Boolean (`bool`)
```python
a = True
b = False
print(type(a)) # Check the data type
print(type(b)) # Same as above
# Note that type() function only takes 1 argument, call it separately for each object you want to check
```

### Set (`set`)
It's a collection of *unique* items.

```python
fruit = {"apple", "banana", "cherry"}
print(type(fruit)) # Check the data type
```

You can try to assign the same item multiple times to a set, but the printed results only the item once.
```python
# Example
fruit = {"apple", "apple", "banana", "cherry"}
print(fruit)
```

You can turn a list into a set:
```python
my_list = [1, 2, 3, 4, 5, 1, 3, 3, 1]

my_set = set(my_list)
print(my_set) # Output: {1, 2, 3, 4, 5}
``` 

More examples of how you can play around with set:
```python
s1 = {1, 3, 1, 88, 66}
s2 = {8, 6, 20, 7, 66}

s1.union(s2) # Output: {1, 3, 6, 7, 8, 20, 66, 88}

s1.intersection(s2) # Output: {66}
```

### List (`list`)
You can have a list of strings/integers/floats, or a mix of them.
```python
travel_list = ["Tokyo", "Paris", "Beijing", "New York"]
age_list = [22, 21, 25, 23]
random_list = ["Tony", 22, 8.5, "hello"]
```

Items in a list stay in a fixed order. So you can retrieve specific items by:
```python
travel_list[0] # Get the first entry which is "Tokyo"
travel_list[:1] # Same output as above (stop at and not include the second entry)

travel_list[-1] # Get the last entry which is "New York"
travel_list[1:3] # Start and include from the second entry and stop and not include the fourth entry (so "Paris", "Beijing")
```
List items in Python are indexed, and the first item has index [0] (which is different from R). 

In the code above, `travel_list[1:3]` used the **slicing** operation to extract multiple items in a *list* at once. Note that this operation works for *strings* and *tuples*. *Set* do not support slicing because they are unordered, and *dictionaries* cannot be sliced either as they have the key functionality (Python101).

Suppose there is a list named `n`, you can slice the list as:
```python
n[start:stop] # Elements from start to 'stop - 1'
n[start:] # Elements from start to the end of the list
n[:stop] # Elements from the beginning to 'stop - 1'
n[:] # Copy of the whole list (alternative: list.copy())
```
*Note*: When slicing, the stop point of the slice is **not** included.

There are two ways to add item(s) to a list.

Example 1 shows how you can extend a list by using the `.extend()` method:
```python
my_first_list = ["one", "two", "three"]
my_second_list = ["four", "five"]

my_first_list.extend(my_second_list)
print(my_first_list) # Output: ['one', 'two', 'three', 'four', 'five']
```

Example 2 shows how you can append a list by using the `.append()` method:
```python
my_first_list = ["one", "two", "three"]
my_second_list = ["four", "five"]

my_first_list.append(my_second_list)
print(my_first_list) # Output: ['one', 'two', 'three', ['four', 'five']]
```

The major difference between these two list methods is that `.extend()` adds each item of an iterable to the list, whereas `.append()` adds a single item or any object.

**Reminder**: don't name your list `list`.

### Dictionary (`dict`)
A collection of paired keys and values. Duplicates are not allowed.

*Note*: In Python 3.6 and earlier versions, dictionaries are *unordered*. However, starting from Python version 3.7, dictionaries are *ordered*. 

```python
age_dict = {'Zeus': None, 
          'Denis': 99, 
          'Alice': 18, 
          'Rebecca' : 20}

print(age_dict) # Print all keys and their values
print(age_dict["Zeus"]) # Print the value (age) of Zeus
```

Similar to `list`, the values in dictionary items can be of any data type:
```python
random_dict = {
  "brand": "Coca-Cola",
  "diet": False,
  "year": 2025,
  "colors": ["red", "while"]
}
```

An example showing how you can add a key to a dictionary:
```python
age_dict = {'Zeus': None, 
          'Denis': 99, 
          'Alice': 18, 
          'Rebecca' : 20}

age_dict['Liam'] = 44
print(age_dict) # Output: {'Zeus': None, 'Denis': 99, 'Alice': 18, 'Rebecca': 20, 'Liam': 44}
```

You can also change the value of an existing key:
```key
age_dict = {'Zeus': None, 
          'Denis': 99, 
          'Alice': 18, 
          'Rebecca' : 20}

age_dict['Alice'] = 19
print(age_dict) # Output: {'Zeus': None, 'Denis': 99, 'Alice': 19, 'Rebecca': 20}
```

### Tuple (`tuple`)
Similar to `list` but it's *immutable* (i.e., cannot be changed).
```python
grades = (8, 8, 7.5, 7, 9)
```

### Bonus sections (`np.arrary` and `defaultdict`)
#### `np.arrary`
A list-like datatype provided by the `numpy` package optimized for efficient mathematical operations (from the slides by Dr. Anne Kroon for the BDACA1). It allows for efficient storage and manipulation of numerical data, making it essential for scientific and mathematical computing - cruicial for performing vectorized operations (Datacamp).

Some examples from the Datacamp:
```python
import numpy as np

# Basic Array Creation
arr1 = np.array([1, 2, 3, 4, 5]) # Create a one-dimensional NumPy array

# Multi-dimensional Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]]) # Create a two-dimensional array from a nested list, effectively forming a matrix

# Array with Specified Data Type
arr3 = np.array([1.5, 2.5, 3.5], dtype=np.int32) # Create a one-dimensional array converting floats to integers

# Using 'ndmin' to Add Dimensions
arr = np.array([1, 2, 3], ndmin=2) # Create a two-dimensional array
```

#### `defaultdict`
A dictionary that does not raise an error but returns the “empty” value of its datatype (0 for int, "" for str) if you try access a non-existing key (from the slides by Dr. Anne Kroon for the BDACA1). It saves you from manually checking for missing keys and avoid `KeyError`.

This example from GeeksforGeeks shows how a defaultdict automatically creates missing keys with a default empty list:
```python
from collections import defaultdict

d = defaultdict(list) # Define the data type here

d['fruits'].append('apple')
d['vegetables'].append('carrot')
print(d) # Output: defaultdict(<class 'list'>, {'fruits': ['apple'], 'vegetables': ['carrot']})
print(d['juices']) # Output: []
```

Anne shared in class that `defaultdict` is great for storing results and counting things. Here's an example she showed us in her live coding lecture:
```python
from collections import defaultdict

my_dict = defaultdict(int) # Define the data type here

words = ['data', 'python', 'analyis', 'nlp', 'data', 'data']

for word in words:
    my_dict[word]+=1

print(my_dict) # Output: defaultdict(<class 'int'>, {'data': 3, 'python': 1, 'analyis': 1, 'nlp': 1})
```

You can also use a regular `dict` to replicate the previous output. Compare the code and see which approach you prefer:
```python
my_dict = {} # Create an empty dictionary

words = ['data', 'python', 'analysis', 'nlp', 'data', 'data']

for word in words:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

print(my_dict) # Output: {'data': 3, 'python': 1, 'analyis': 1, 'nlp': 1}
```

## Loops and conditional statements
### `for`-Loops
The most common types of loops are *for*, *while*, and *repeat*, but we will be mostly concerned with the `for`-loops (van Atteveldt et al., 2022). The general syntax of `for`-loops is:
```python
for item in iterable:
    # Code goes here (must be indented!)
```

An *iterable* is a fancy word for something that can be iterated over, such as strings, lists, tuples (Python101). Here are some examples:
```python
numbers = [1,5,7,10,2,4,6]
for num in numbers:
    print(num+1)
```

You can loop over dictionaries:
```python
age_dict = {'Zeus': None, 
          'Denis': 99, 
          'Alice': 18, 
          'Rebecca' : 20}

# Check the keys in this dictionary
for k in age_dict:
    print(k)

# Check the values in this dictionary
for v in age_dict.values():
    print(v)

# Check the pairs of keys and values in this dictionary
for k,v in age_dict.items():
    print(k,v)
```

### Bonus: List comprehensions
List comprehensions are another way of writing `for`-loops in a single line of code. They're generally faster and can be used for more compact representation of simple interations yielding more readable code (Python101). The general syntax of list comprehensions is:
```python
result_list = [expression for item in iterable]
```

A simple example from the BDACA1 course:
```python
my_numbers = [2,1,6,5]
my_squarednumbers = [x**2 for x in my_numbers]
```

It is equivalent to:
```python
my_numbers = [2,1,6,5]
my_squarednumbers = []

for x in my_numbers:
    my_squarednumbers.append(x**2)
```

### `while`-Loops
A `while` loop is a loop that continues until some condition is no longer satisfied (Python101). The general syntax of `while`-loops is:
```python
while condition: 
    # Code goes here (must be indented!)
```

Here's an example:
```python
a = 1

while a <=5:
    a += 1 # The same as: a = a + 1
    print(a) # The output will print integers from 2 to 6
```

### `if`/`elif`/`else`-Statements
The general syntax is:
```python
if condition:
    statement1
elif other_condition:
    statement2
else:
    statement3
```

*Note*: Your computer only executes the code block if a condition is met.

A simple example:
```python
x=5

if x <10:
   print(f"The number is smaller than 10")
elif x > 20:
   print(f"The number is greater than 20")
else:
   print("No previous condition is met")
```
In this example, the output shows: The number is smaller than 10.

### 'try'/'except'-Statements
When you have a code block sometimes runs correctly and sometimes not, you should use 'try'/'except' instead of `if`/`elif`/`else`. The general syntax is:
```python
try:
    statement1
except:
    statement2
```

An example from the BDACA1 course:
```python
mylist = ["5", 3, "whatever", 2.2]
myresults = []
for x in mylist:
    try:
        myresults.append(int(x))
    except:
        myresults.append(None)
print(myresults) # Output: [5, 3, None, 2]
```

## Functions and methods
### Built-in functions
Built-in functions are predefined by Python developers for users to use. They take an input and return something else. For example, `int(32.43)` returns the integer 32; `len("Hello")` returns the integer 5 (BDACA1).

Check out the [Python documentation](https://docs.python.org/3/library/functions.html) for a full list of built-in functions. You can also choose your preferred language and Python version.

Here are some of the most commonly used functions (from the BDACA1):
```python
print(x) # something you should definitely know
len(x) # returns the length of x
int(x) # convert x to an integer
str(x) # convert x to a string
sum(x) # get the sum of x
```

**f-string** is a handy function which allows you to handle expressions and calculations within strings.
```python
a = 5
b = 8
print(f'Multiplication: a * b = {a} * {b} = {a*b}')
```

### Methods
Similar to functions, but directly associated with an object. For example, `"SCREAM".lower()` returns the string "scream" (BDACA1).

Here are some examples of string methods:
```python
my_string = "Hi! How are you?"

# Note that you need to print() the following code seperately to return their output (I skipped them in this block)
my_string.lower() # return lowercased string (you need to save it to a new object for later use)

my_string.upper() # return uppercased string (same as above)

my_string.split() # split on spaces and return a list ['Hi!', 'How', 'are', 'you?']

my_string.replace("Hi", "Hey") # replace the old string "Hi" with the new string "Hey" and return "Hey! How are you?"

my_string.count("H") # count the number of occurences of the substring "H" inside the string and return 2 (this method is case sensitive, so "h" returns 0)
```

*Tip*: Type a `.` after an object and press **Tab** to see all its available methods and properties.

### Define your own functions
A function is a block of code that is first defined, and thereafter can be called to run as many times as needed (Python101). The general syntax of a function is:
```python
def function_name(arg):
    # Function code goes here
    # You can have multiple lines of code
    return value # You can return one or more values
```

An example of writing a simple function (from the BDACA1):
```python
my_list = [4, 99,5, 21]
results = [] # Define an empty list to store the results

# Define the function here which only takes 1 argument        
def return_values(x):
    if x < 10:
        return "SMALLER THAN 10"
    elif x > 20:
        return "LARGER THAN 20"
    else:
        return None

# Apply the function to the list and store the results in the predefined empty list
for x in my_list:
    results.append(return_values(x))

print(results) # Output: ['SMALLER THAN 10', 'LARGER THAN 20', 'SMALLER THAN 10', 'LARGER THAN 20']
```

You can also use a list comprehension to get the same results:
```python
my_list = [4, 99,5, 21]

# Define the function here
def return_values(x):
    if x < 10:
        return "SMALLER THAN 10"
    elif x > 20:
        return "LARGER THAN 20"
    else:
        return None

results = [return_values(x) for x in my_list] # Apply the function to the list and store the results in a new list
print(results) # Output: ['SMALLER THAN 10', 'LARGER THAN 20', 'SMALLER THAN 10', 'LARGER THAN 20']
```

Another example from Anne's live coding lecture:
```python
random_list = ['5', 'aliijog', 10, 11]
my_results = []

# Define the function here
def convert_to_int(x):
    try:
        return int(x)
    except:
        return None

# Apply the function to the result and store it in the predefined new list
for e in random_list:
    my_results.append(convert_to_int(e))

print(my_results) # Output: [5, None, 10, 11]
```

Similar to the previous example, you can also do it in a list comprehension:
```python
random_list = ['5', 'aliijog', 10, 11]

# Define the function here
def convert_to_int(x):
    try:
        return int(x)
    except:
        return None

my_results = [convert_to_int(x) for x in random_list] # Apply the function to the result and store it in a new list
print(my_results) # Output: [5, None, 10, 11]
```

As you see, list comprehensions can save more lines of code, but it is up to you to choose which approach you prefer.

## References
- [Computational Analysis of Communication](https://cssbook.net/) (an open-access book written by Prof. Dr. Wouter van Atteveldt, Prof. Dr. Damian Trilling, and Dr. Carlos Arcila)
- Slides and code from the [BDACA1](https://github.com/uvacw/teaching-bdaca/tree/main/6ec-course) course
- [W3School](https://www.w3schools.com/python/python_datatypes.asp)
- [Python101](https://github.com/Python-Crash-Course/Python101/tree/master)
- [Datacamp](https://www.datacamp.com/doc/numpy/array)
- [GeeksforGeeks](https://www.geeksforgeeks.org/python/defaultdict-in-python/)







