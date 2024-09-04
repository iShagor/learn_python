# Write a hello world program
Here’s a simple "Hello, World!" program in Python:

```python
print("Hello, World!")
```

When you run this code, it will output:

```
Hello, World!
```
# Python run from the command line
To run a Python script from the command line, follow these steps:

### 1. **Create the Python Script:**
   - Open a text editor (e.g., Notepad, VS Code, or any other code editor).
   - Write the "Hello, World!" program and save it with a `.py` extension, such as `hello_world.py`.

   ```python
   print("Hello, World!")
   ```

### 2. **Open the Command Line:**
   - On **Windows**: Press `Win + R`, type `cmd`, and press Enter.
   - On **macOS/Linux**: Open the Terminal from your applications or use a shortcut (`Cmd + Space` and type "Terminal" on macOS).

### 3. **Navigate to the Script’s Directory:**
   Use the `cd` command to change the directory to where your Python script is saved. For example:

   ```bash
   cd path\to\your\script
   ```

   Replace `path\to\your\script` with the actual path to the directory where `hello_world.py` is saved.

### 4. **Run the Python Script:**
   - If Python is installed and added to your system’s PATH, you can run the script by typing:

   ```bash
   python hello_world.py
   ```

   - On some systems, you might need to use `python3` instead of `python`:

   ```bash
   python3 hello_world.py
   ```

### 5. **See the Output:**
   After running the command, you should see the following output:

   ```
   Hello, World!
   ```

That's it! You've successfully run a Python script from the command line.
# Run from PyCharm
To run a Python script from PyCharm, follow these steps:

### 1. **Install PyCharm:**
   If you don't already have PyCharm installed, you can download it from [JetBrains' official site](https://www.jetbrains.com/pycharm/download/) and install it.

### 2. **Create a New Project:**
   - Open PyCharm.
   - Click on "New Project."
   - Choose the location for your project and specify the Python interpreter (PyCharm usually auto-detects this).
   - Click "Create" to start a new project.

### 3. **Create a Python Script:**
   - In your new project, right-click on the `project_name` in the Project tool window (usually on the left side).
   - Select `New` > `Python File`.
   - Name your file, for example, `hello_world.py`.

   ```python
   print("Hello, World!")
   ```

### 4. **Run the Script:**
   - Right-click on the `hello_world.py` file in the Project tool window.
   - Select `Run 'hello_world'`.
   - Alternatively, you can click on the green play button in the top right corner of PyCharm's window.

### 5. **See the Output:**
   - The output will appear at the bottom of the PyCharm window in the Run tool window.

   ```
   Hello, World!
   ```

This is how you can run a Python script in PyCharm.
# Declar Variable
In Python, declaring a variable is straightforward because you don't need to specify the data type explicitly. You simply assign a value to a variable name, and Python automatically determines the type based on the value. Here’s how you can declare variables in Python:

### Examples:

```python
# Declare an integer variable
number = 10

# Declare a floating-point variable
price = 99.99

# Declare a string variable
greeting = "Hello, World!"

# Declare a boolean variable
is_sunny = True
```

### How It Works:

- **`number = 10`**: Here, `number` is a variable that holds an integer value of `10`.
- **`price = 99.99`**: The variable `price` holds a floating-point number.
- **`greeting = "Hello, World!"`**: The variable `greeting` stores a string.
- **`is_sunny = True`**: The variable `is_sunny` stores a boolean value.

### Printing Variables:

You can print the value of a variable using the `print()` function:

```python
print(number)      # Output: 10
print(price)       # Output: 99.99
print(greeting)    # Output: Hello, World!
print(is_sunny)    # Output: True
```

This is how you declare and use variables in Python!

# Use Declared variable in the program
Here's an example of how to declare variables in Python and use them in a simple program:

```python
# Declare variables
name = "Alice"
age = 25
height = 5.6  # in feet
is_student = True

# Use variables in the program
print("Name:", name)
print("Age:", age)
print("Height:", height, "feet")
print("Is a student:", is_student)

# Perform operations using variables
age_next_year = age + 1
height_in_cm = height * 30.48  # 1 foot = 30.48 cm

print("Next year,", name, "will be", age_next_year, "years old.")
print(name, "is", height_in_cm, "cm tall.")
```

### Explanation:

- **Variable Declaration:**
  - `name` is a string variable.
  - `age` is an integer variable.
  - `height` is a floating-point variable.
  - `is_student` is a boolean variable.

- **Using Variables:**
  - The `print()` function displays the value of each variable.
  - You can also perform operations using these variables. For example, `age_next_year` is calculated by adding 1 to `age`, and `height_in_cm` is calculated by converting `height` from feet to centimeters.

### Output:
When you run the program, it will produce the following output:

```
Name: Alice
Age: 25
Height: 5.6 feet
Is a student: True
Next year, Alice will be 26 years old.
Alice is 170.688 cm tall.
```

This example shows how to declare variables, use them in print statements, and perform operations with them in a Python program.
# Build-in Data types
Python has several built-in data types that are used to store different kinds of data. Here’s a list of the most common built-in data types along with examples of how they are used:

### 1. **Numeric Types:**
   - **`int`**: Represents integers (whole numbers).
   - **`float`**: Represents floating-point numbers (numbers with decimal points).
   - **`complex`**: Represents complex numbers (numbers with a real and an imaginary part).

   **Examples:**
   ```python
   x = 10           # int
   y = 3.14         # float
   z = 2 + 3j       # complex
   ```

### 2. **Sequence Types:**
   - **`str`**: Represents a sequence of characters (strings).
   - **`list`**: Represents an ordered collection of items (which can be of different types).
   - **`tuple`**: Represents an ordered, immutable collection of items.

   **Examples:**
   ```python
   text = "Hello, World!"  # str
   numbers = [1, 2, 3, 4, 5]  # list
   coordinates = (10.5, 20.3)  # tuple
   ```

### 3. **Mapping Type:**
   - **`dict`**: Represents a collection of key-value pairs.

   **Example:**
   ```python
   student = {
       "name": "Alice",
       "age": 25,
       "is_student": True
   }
   ```

### 4. **Set Types:**
   - **`set`**: Represents an unordered collection of unique items.
   - **`frozenset`**: Represents an immutable version of a set.

   **Examples:**
   ```python
   unique_numbers = {1, 2, 3, 4, 5}  # set
   frozen_numbers = frozenset([1, 2, 3, 4, 5])  # frozenset
   ```

### 5. **Boolean Type:**
   - **`bool`**: Represents a value of `True` or `False`.

   **Examples:**
   ```python
   is_valid = True  # bool
   has_access = False  # bool
   ```

### 6. **Binary Types:**
   - **`bytes`**: Represents immutable sequences of bytes.
   - **`bytearray`**: Represents mutable sequences of bytes.
   - **`memoryview`**: Allows direct access to an object's byte-oriented data without copying it.

   **Examples:**
   ```python
   data = b"Hello"  # bytes
   buffer = bytearray(5)  # bytearray
   view = memoryview(buffer)  # memoryview
   ```

### 7. **None Type:**
   - **`NoneType`**: Represents the absence of a value.

   **Example:**
   ```python
   result = None  # NoneType
   ```

### Summary:

Python provides these built-in data types to handle a wide variety of data in your programs. Each type serves a specific purpose and has its own set of operations that can be performed. Understanding these data types is fundamental to working with Python effectively.

# Arithemtic Operators

Python provides several arithmetic operators that allow you to perform basic mathematical operations. Here’s a list of the most common arithmetic operators along with examples:

### 1. **Addition (`+`)**
   - Adds two numbers.

   **Example:**
   ```python
   x = 10
   y = 5
   result = x + y  # 15
   ```

### 2. **Subtraction (`-`)**
   - Subtracts the second number from the first.

   **Example:**
   ```python
   x = 10
   y = 5
   result = x - y  # 5
   ```

### 3. **Multiplication (`*`)**
   - Multiplies two numbers.

   **Example:**
   ```python
   x = 10
   y = 5
   result = x * y  # 50
   ```

### 4. **Division (`/`)**
   - Divides the first number by the second, resulting in a floating-point number.

   **Example:**
   ```python
   x = 10
   y = 5
   result = x / y  # 2.0
   ```

### 5. **Floor Division (`//`)**
   - Divides the first number by the second, but instead of returning a floating-point number, it returns the largest integer less than or equal to the division result.

   **Example:**
   ```python
   x = 10
   y = 3
   result = x // y  # 3
   ```

### 6. **Modulus (`%`)**
   - Returns the remainder of the division between two numbers.

   **Example:**
   ```python
   x = 10
   y = 3
   result = x % y  # 1
   ```

### 7. **Exponentiation (`**`)**
   - Raises the first number to the power of the second number.

   **Example:**
   ```python
   x = 2
   y = 3
   result = x ** y  # 8
   ```

### Examples Combined in a Program:

```python
a = 15
b = 4

# Addition
print("Addition:", a + b)  # 19

# Subtraction
print("Subtraction:", a - b)  # 11

# Multiplication
print("Multiplication:", a * b)  # 60

# Division
print("Division:", a / b)  # 3.75

# Floor Division
print("Floor Division:", a // b)  # 3

# Modulus
print("Modulus:", a % b)  # 3

# Exponentiation
print("Exponentiation:", a ** b)  # 50625
```

### Output:
```
Addition: 19
Subtraction: 11
Multiplication: 60
Division: 3.75
Floor Division: 3
Modulus: 3
Exponentiation: 50625
```

These arithmetic operators are fundamental tools in Python and are used in a wide range of applications, from simple calculations to complex algorithms.

# Assignment Operators
Assignment operators in Python are used to assign values to variables. They combine arithmetic or other operations with assignment. Here’s a list of assignment operators and how they work:

### 1. **Simple Assignment (`=`)**
   - Assigns the value on the right to the variable on the left.

   **Example:**
   ```python
   x = 10  # x is now 10
   ```

### 2. **Add and Assign (`+=`)**
   - Adds the value on the right to the variable on the left and then assigns the result to the variable on the left.

   **Example:**
   ```python
   x = 10
   x += 5  # Equivalent to: x = x + 5; x is now 15
   ```

### 3. **Subtract and Assign (`-=`)**
   - Subtracts the value on the right from the variable on the left and then assigns the result to the variable on the left.

   **Example:**
   ```python
   x = 10
   x -= 3  # Equivalent to: x = x - 3; x is now 7
   ```

### 4. **Multiply and Assign (`*=`)**
   - Multiplies the variable on the left by the value on the right and then assigns the result to the variable on the left.

   **Example:**
   ```python
   x = 10
   x *= 2  # Equivalent to: x = x * 2; x is now 20
   ```

### 5. **Divide and Assign (`/=`)**
   - Divides the variable on the left by the value on the right and then assigns the result to the variable on the left. The result is a float.

   **Example:**
   ```python
   x = 10
   x /= 2  # Equivalent to: x = x / 2; x is now 5.0
   ```

### 6. **Floor Divide and Assign (`//=`)**
   - Performs floor division on the variable on the left by the value on the right and then assigns the result to the variable on the left.

   **Example:**
   ```python
   x = 10
   x //= 3  # Equivalent to: x = x // 3; x is now 3
   ```

### 7. **Modulus and Assign (`%=`)**
   - Takes the modulus of the variable on the left with the value on the right and then assigns the result to the variable on the left.

   **Example:**
   ```python
   x = 10
   x %= 3  # Equivalent to: x = x % 3; x is now 1
   ```

### 8. **Exponentiate and Assign (`**=`)**
   - Raises the variable on the left to the power of the value on the right and then assigns the result to the variable on the left.

   **Example:**
   ```python
   x = 2
   x **= 3  # Equivalent to: x = x ** 3; x is now 8
   ```

### 9. **Bitwise AND and Assign (`&=`)**
   - Performs a bitwise AND operation on the variable on the left with the value on the right and then assigns the result to the variable on the left.

   **Example:**
   ```python
   x = 10  # In binary: 1010
   x &= 7  # In binary: 0111; x is now 2 (binary: 0010)
   ```

### 10. **Bitwise OR and Assign (`|=`)**
   - Performs a bitwise OR operation on the variable on the left with the value on the right and then assigns the result to the variable on the left.

   **Example:**
   ```python
   x = 10  # In binary: 1010
   x |= 7  # In binary: 0111; x is now 15 (binary: 1111)
   ```

### 11. **Bitwise XOR and Assign (`^=`)**
   - Performs a bitwise XOR operation on the variable on the left with the value on the right and then assigns the result to the variable on the left.

   **Example:**
   ```python
   x = 10  # In binary: 1010
   x ^= 7  # In binary: 0111; x is now 13 (binary: 1101)
   ```

### 12. **Bitwise Left Shift and Assign (`<<=`)**
   - Shifts the bits of the variable on the left to the left by the number of places specified on the right and then assigns the result to the variable on the left.

   **Example:**
   ```python
   x = 10  # In binary: 1010
   x <<= 2  # x is now 40 (binary: 101000)
   ```

### 13. **Bitwise Right Shift and Assign (`>>=`)**
   - Shifts the bits of the variable on the left to the right by the number of places specified on the right and then assigns the result to the variable on the left.

   **Example:**
   ```python
   x = 10  # In binary: 1010
   x >>= 2  # x is now 2 (binary: 10)
   ```

### Example Program Using Assignment Operators:

```python
x = 5

x += 3  # x is now 8
x -= 2  # x is now 6
x *= 4  # x is now 24
x /= 3  # x is now 8.0
x //= 2  # x is now 4.0
x %= 3  # x is now 1.0
x **= 2  # x is now 1.0
```

### Output:
```
Final value of x: 1.0
```

These operators allow you to perform operations on variables and update them in place, which can simplify your code and make it more concise.

# Comparison Operators
Comparison operators in Python are used to compare two values and return a boolean result (`True` or `False`). Here’s a list of the common comparison operators and how they work:

### 1. **Equal to (`==`)**
   - Checks if the values of two operands are equal.
   
   **Example:**
   ```python
   x = 10
   y = 10
   result = (x == y)  # True
   ```

### 2. **Not equal to (`!=`)**
   - Checks if the values of two operands are not equal.
   
   **Example:**
   ```python
   x = 10
   y = 5
   result = (x != y)  # True
   ```

### 3. **Greater than (`>`)**
   - Checks if the value on the left is greater than the value on the right.
   
   **Example:**
   ```python
   x = 10
   y = 5
   result = (x > y)  # True
   ```

### 4. **Less than (`<`)**
   - Checks if the value on the left is less than the value on the right.
   
   **Example:**
   ```python
   x = 10
   y = 15
   result = (x < y)  # True
   ```

### 5. **Greater than or equal to (`>=`)**
   - Checks if the value on the left is greater than or equal to the value on the right.
   
   **Example:**
   ```python
   x = 10
   y = 10
   result = (x >= y)  # True
   ```

### 6. **Less than or equal to (`<=`)**
   - Checks if the value on the left is less than or equal to the value on the right.
   
   **Example:**
   ```python
   x = 10
   y = 15
   result = (x <= y)  # True
   ```

### Example Program Using Comparison Operators:

```python
a = 7
b = 10

print("a == b:", a == b)  # False
print("a != b:", a != b)  # True
print("a > b:", a > b)    # False
print("a < b:", a < b)    # True
print("a >= b:", a >= b)  # False
print("a <= b:", a <= b)  # True
```

### Output:
```
a == b: False
a != b: True
a > b: False
a < b: True
a >= b: False
a <= b: True
```

These comparison operators are essential for making decisions and controlling the flow of a program. They are commonly used in conditional statements like `if`, `elif`, and `while` to execute different code based on the conditions.

# How to write comments

In Python, comments are used to explain and annotate your code. They are ignored by the Python interpreter and are only for the benefit of people reading the code. Python supports two types of comments:

### 1. **Single-Line Comments**

Single-line comments start with the `#` symbol. Everything following the `#` on that line is considered a comment.

**Example:**
```python
# This is a single-line comment
x = 10  # This is an inline comment
```

### 2. **Multi-Line Comments**

Python does not have a specific syntax for multi-line comments like some other programming languages. However, you can use a multi-line string (triple quotes) as a comment. Although this is technically a string literal, it is often used as a multi-line comment when not assigned to a variable.

**Example:**
```python
"""
This is a multi-line comment.
It spans multiple lines.
"""
x = 10
```

Alternatively, you can use multiple single-line comments to achieve the same result:

**Example:**
```python
# This is a multi-line comment.
# It spans multiple lines.
# Each line starts with a hash symbol.
x = 10
```

### Usage of Comments:

- **Inline Comments**: Use these to explain a specific part of the code right next to the code itself. They should be concise and placed on the same line as the code they refer to.

  **Example:**
  ```python
  total = 5 + 3  # Adding 5 and 3 to get the total
  ```

- **Block Comments**: Use these to describe larger sections of code. They are generally placed above the code block they are describing and can be either single-line or multi-line comments.

  **Example:**
  ```python
  # This section of code calculates the average of a list of numbers.
  # It first computes the sum of all numbers and then divides by the count.
  numbers = [10, 20, 30]
  total = sum(numbers)
  average = total / len(numbers)
  ```

Comments are crucial for making your code more readable and maintainable, especially for others who might work with your code or for yourself when revisiting it later.