import numpy as np

decimal_number = int(input("Enter a decimal number: "))

binary = np.binary_repr(decimal_number)
print(f"Binary representation: {binary}")

octal = np.base_repr(decimal_number, base=8)
print(f"Octal representation: {octal}")

hexadecimal = np.base_repr(decimal_number, base=16)
print(f"Hexadecimal representation: {hexadecimal}")
