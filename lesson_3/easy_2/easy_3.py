# Programmatically determine whether 42 lies between 
# 10 and 100, inclusive. Do the same for the values 100 and 101.

print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))

# LS ANSWER:

42 in range(10, 101)          # True
100 in range(10, 101)         # True
101 in range(10, 101)         # False

# Note: In Python, the range object includes the start value but 
# excludes the end value. So, range(10, 101) include both 10 and 100 but not 101.