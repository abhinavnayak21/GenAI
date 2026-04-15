# main.py

#Task 1 imports
import math_utils
from math_utils import square

#math_utils
print("Add:", math_utils.add(10, 5))
print("Subtract:", math_utils.subtract(10, 5))
print("Square:", square(4))


# Task 2 import
import string_utils

print("Capitalized:", string_utils.capitalize_words("hello world"))
print("Reversed:", string_utils.reverse_string("python"))
print("Word count:", string_utils.word_count("learn python easily"))


#Task 4 imports (package)
import shop_package.discount as disc
from shop_package.billing import calculate_total

# Test discount functions
print("Apply discount:", disc.apply_discount(1000, 10))
print("Flat discount:", disc.flat_discount(500))

# Test billing functions
total = calculate_total([100, 200, 300])
print("Total:", total)

# Using tax (via package import from __init__)
from shop_package import apply_tax
print("Total with tax:", apply_tax(total))