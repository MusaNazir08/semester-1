# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

flt = read_numbers()

if flt == []:
    sys.exit("Error: no numbers provided")

maxFlt = max(flt)
minFlt = min(flt)
mean = sum(flt)/len(flt)
#median
flt.sort()

n = len(flt)

if n%2 == 1:
    median = flt[n // 2]
else:
    median = (flt[n // 2 - 1] + flt[n // 2]) / 2
    
print(f"Minimum = {minFlt}")
print(f"Maximum = {maxFlt}")
print(f"Mean = {mean}")
print(f"Median = {median}")