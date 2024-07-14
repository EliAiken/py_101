# What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

# This will print the following list: [{"first": 42}, {"second": "value2"}, 3, 4, 5]
# The reason being is that the copy() function makes a shallow copy of the original
# list, which will allow nested objects to be mutated if changed in the copied list.
# Thus, making changes to my_list2 will ultimately change my_list1 to the result above.

# LS ANSWER:

# There are two kinds of copy operations when working with lists: a deep copy and 
# a shallow copy.

# A deep copy makes a duplicate of every item in an existing list. In particular, 
# it creates completely new instances of any nested objects in the source. If we 
# performed a deep copy on my_list1, using a deepcopy() function we would have 
# two different lists and four separate dictionaries.

# We'll only have 3 integers, however, due to optimizations performed by Python 
# with immutable values. We'll talk about what that is in a later course.

# A shallow copy only makes a duplicate of the outermost values in an object. 
# If we perform a shallow copy on my_list1, we end up with two different lists, 
# but we still only have one occurrence each of { first: 42 } and { second: 'value2' }. 
# In this case, both my_list1[0] and my_list2[0] point to the same dictionary 
# in memory. Likewise, my_list1[1] and my_list2[1] point to the { second: 'value2' } 
# dictionary.

# The copy() function performs shallow copies. 

# my_list1[0] and my_list2[0] point to the same dictionary, { first: "value1" }. 
# Thus, when we replace the value of the first property by using my_list2[0]['first'], 
# the change shows up in my_list1 as well.