from math_operations.addition import add as direct_add
from math_operations import add as package_add

print("Direct module import:", direct_add(10, 20))
print("Package-level import:", package_add(10, 20))

import math_operations

print("Package imported again")

import sys

print("Is math_operations cached?",
      "math_operations" in sys.modules)