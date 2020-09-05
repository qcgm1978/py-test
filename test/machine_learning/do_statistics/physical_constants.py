from math import log10, floor
from scipy.constants import codata

def most_significant_digit(x):
    e = floor(log10(x))
    return int(x*10**-e)

# count how many constants have each leading digit
count = [0]*10
d = codata.physical_constants
for c in d:
    (value, unit, uncertainty) = d[ c ]
    x = abs(value)
    count[most_significant_digit(x)] += 1
count=count[1:]
total = sum(count)


