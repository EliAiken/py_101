# What will the following code output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

# This will print "hello there" because str1 is still pointing to the "hello there"
# location in memory. The reassignment of str2 did not reassign str1.

# LS ANSWER:

# The output is hello there. In Python, strings are immutable so there 
# is no way to change the value of str1 unless we reassign it. When we 
# do str2 = str1 we are pointing the variable str2 to the same memory 
# location as the original string. Once we reassign str2 again, on line 3, 
# it just changes what str2 variable points to, and doesn't affect 
# variable str1.