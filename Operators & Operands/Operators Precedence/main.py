# Exponentiation
print("Exponentiation: 2 ** 3 =", 2 ** 3)  # Output: 8

# Unary operators
print("Complement: ~1 =", ~1)  # Output: -2
print("Unary Plus: +3 =", +3)  # Output: 3
print("Unary Minus: -3 =", -3)  # Output: -3

# Arithmetic operators
print("Multiply: 4 * 2 =", 4 * 2)  # Output: 8
print("Divide: 4 / 2 =", 4 / 2)  # Output: 2.0
print("Modulo: 5 % 2 =", 5 % 2)  # Output: 1
print("Floor Division: 5 // 2 =", 5 // 2)  # Output: 2

# Addition and Subtraction
print("Addition: 5 + 2 =", 5 + 2)  # Output: 7
print("Subtraction: 5 - 2 =", 5 - 2)  # Output: 3

# Bitwise shift
print("Right Shift: 8 >> 2 =", 8 >> 2)  # Output: 2
print("Left Shift: 1 << 2 =", 1 << 2)  # Output: 4

# Bitwise AND
print("Bitwise AND: 5 & 3 =", 5 & 3)  # Output: 1

# Bitwise OR and XOR
print("Bitwise OR: 5 | 3 =", 5 | 3)  # Output: 7
print("Exclusive OR: 5 ^ 3 =", 5 ^ 3)  # Output: 6

# Comparison operators
print("Less Than or Equal: 4 <= 5 is", 4 <= 5)  # Output: True
print("Greater Than: 5 > 3 is", 5 > 3)  # Output: True

# Equality operators
print("Equal: 5 == 5 is", 5 == 5)  # Output: True
print("Not Equal: 5 != 4 is", 5 != 4)  # Output: True

# Assignment operators
x = 10
x += 5
x *= 2
x **= 2
print("Assignment: x starts as 10, then becomes", x, "after += 5, *= 2, **= 2")  # Output: 900

# Identity operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("Identity (is): c is a is", c is a)  # Output: True
print("Identity (is not): a is not b is", a is not b)  # Output: True

# Membership operators
print("Membership (in): 1 in [1, 2, 3] is", 1 in [1, 2, 3])  # Output: True
print("Membership (not in): 4 not in [1, 2, 3] is", 4 not in [1, 2, 3])  # Output: True

# Logical operators
print("Logical (not): not True is", not True)  # Output: False
print("Logical (or): True or False is", True or False)  # Output: True
print("Logical (and): True and False is", True and False)  # Output: False
