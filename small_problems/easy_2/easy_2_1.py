# Create a function that takes 2 arguments, a list and a dictionary. 
# The list will contain 2 or more elements that, when joined with 
# spaces, will produce a person's name. The dictionary will contain 
# two keys, "title" and "occupation", and the appropriate values. 
# Your function should return a greeting that uses the person's full 
# name, and mentions the person's title.

my_lst = ['Eli', 'M', 'Aiken']
my_dct = {'title': 'Master', 'occupation': 'SLP'}

def greetings(lst, dct):
    name = ' '.join(lst)
    title = dct.get('title')
    occupation = dct.get('occupation')
    return (f'Hello, {name}! Nice to have a {title} {occupation} around.')

print(greetings(my_lst, my_dct))

# LS ANSWER: 

def greetings(name, status):
    return(f"Hello, {' '.join(name)}! Nice to have a "
           f"{status['title']} {status['occupation']}"
           "around.")

# We use the join method to change the list into a full name with 
# appropriate spacing. For the dictionary, we access the items by 
# their keys.

# Finally, we use f-string formatting to combine everything into 
# a single string, resulting in a concise and readable way to 
# format the final output.

# Note that the parentheses on the return are necessary here. 
# Without them, Python won't deal with the continuation lines 
# correctly.