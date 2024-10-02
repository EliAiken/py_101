name = 'Joe' 

def print_me(string):
    print(string)

print_me(name)

# ------------------------------------------------------------ #

# What does this print and why?

# What does this print and why?

lst1 = [0, 1, 2, 3]
lst2 = lst1.append(4)

if lst2:
    print("Hi Eli!!")
    print(lst2)
else:
    print(lst1)

# ------------------------------------------------------------ #

# What does this print and why? What concept does this demonstrate?

def addition(number1, number2):
    number1 += number2

x = 1
y = 2

addition(x, y)
print(f"x is {x}, y is {y}")

def addition(lst1, lst2):
    lst1 += lst2

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

addition(numbers1, numbers2)
print(f"x is {numbers1}, y is {numbers2}")

# ------------------------------------------------------------ #
# What does this print and why? What concept does this demonstrate?

word = 'hello'

another_word = word[:]
print(another_word)
print(id(word) == id(another_word))


lst = [1, 2, 3, 4]
another_lst = lst[:]
print(id(lst) == id(another_lst))

# ------------------------------------------------------------ #

def function1():
  x = 10

  def function2():
      y = 20
      print(x)

  function2()
  print(x)
  print(y)

function1()
print(x)
print(y)

# ------------------------------------------------------------ #

var = 10

def function2():
    var += 20
    print(var)

function2()

# ------------------------------------------------------------ #

def scope_test():
    if True:
        greeting = 'Hello'
    else:
        goodbye = 'Ciao'

    print(greeting) # Hello
    print(fdsa) # NameError
    print(goodbye) #UnboundLocalError

scope_test()

# ------------------------------------------------------------ #

string = "Weiß"
casefolded = string.casefold()
print(casefolded) # Weiss

# ------------------------------------------------------------ #

# Swapcase

sentence = 'ß'
sentence2 = sentence.swapcase().swapcase()
print(sentence2)

# ------------------------------------------------------------ #

# Explain what's going on here:

greeting = 'Hi!'

def the_steve_buscemi_greeting():
    greeting = 'How do you do, fellow kids?'
    print(greeting)

the_steve_buscemi_greeting() 
print(greeting)

# ------------------------------------------------------------ #

# Explain what's going on here:

greeting = 'Hi!'

def the_steve_buscemi_greeting():
    greeting = 'How do you do, fellow kids?'
    
    def func2():
        greeting = 'Tschüss'
        print(greeting)
    
    func2()
    print(greeting)

the_steve_buscemi_greeting() 
print(greeting)

# ------------------------------------------------------------ #

# Explain what's going on here:

greeting = "Hello"

def greet(greeting):
    greeting = greeting + "world"
    return greeting

print(greet(greeting))
print(greeting)

# ------------------------------------------------------------ #

# Explain what's going on here:

greeting = "Hello"

def greet(greeting):
    greeting += "world"
    return greeting

print(greet(greeting))
print(greeting)

# ------------------------------------------------------------ #


# Explain what's going on here:

greeting = ["Hello"]

def greet(greeting):
    greeting + ["world"]
    return greeting

print(greet(greeting))
print(greeting)

# ------------------------------------------------------------ #

# Explain what's going on here:

greeting = ["Hello"]

def greet(greeting):
    greeting += ["world"] # ["Hello", "world"]
    return greeting

print(greet(greeting)) # An object reference to the variable 'greeting' is passed into the function greet
print(greeting)

# ------------------------------------------------------------ #

# Variable Scope

def salutation():
    greeting = 'Hello'
    print(greeting)

salutation()
print(greeting)

# ------------------------------------------------------------ #

# Variable Shadowing

count = 5

def func1():
    count = 10  
    print(count)

count = [1, 2, 3]
func1()
print(count)

# The code prints 10 and [1, 2, 3]. Inside func1, the variable count is defined locally 
# with the value 10, which shadows the global count. This means the function uses its 
# local version of count instead of the global one, demonstrating variable shadowing. 
# When the global count is printed outside the function, it shows [1, 2, 3], because 
# the global count was reassigned to a list before calling the function. The local 
# variable inside func1 does not affect the global variable due to the scope isolation 
# provided by variable shadowing.

# ------------------------------------------------------------ #

# List Mutability

def func2(lst):
    lst[0] = 'x'  
    print(lst)

numbers = [10, 20, 30]
func2(numbers)
print(numbers)

# The program prints ['x', 20, 30] twice. This occurs because lists are mutable objects 
# in Python, meaning that changes to them affect the original list directly. When the 
# function func2 is called with numbers as an argument, it modifies the first element 
# of the list to 'x'. Since lst inside func2 refers to the same list object as numbers, 
# the modification is reflected in the original list. Therefore, when the list numbers 
# is printed after the function call, it shows the modified list ['x', 20, 30].

# ------------------------------------------------------------ #

# What is the difference between these 2 programs?

greeting = ["Hello"]

def greet():
    greeting += [" world"]
    print(greeting)

greet()
print(greeting)

# greeting has not been assigned in the local scope of the function, therefore it could not be
# used to modify the global variable greeting without the `global` keyword being used. The
# function attempted to find the greeting variable within the local scope, but could not find
# it, so an error was thrown (UnboundLocalError).

#   #   #   #   #   #   #   #   #

greeting = ["Hello"]

def greet(greeting):
    greeting += ["world"]
    print(greeting)

greet(greeting)
print(greeting)

# When greet(greeting) is called, the global list greeting is passed as an argument to 
# the function. Lists in Python are mutable, and when they are passed as arguments to 
# functions, the function receives a reference to the original list (object), not a copy 
# of it.

# Since greeting is not being assigned a new value (i.e., the variable name itself is 
# not being reassigned), but rather its contents are being modified, the function does 
# not need the global keyword. The global keyword is only necessary if you want to reassign 
# a new value to the global variable within the function.

# ------------------------------------------------------------ #

# What does this code output and why?

def function1():
  x = 10

  def function2():
      y = 20
      print(x)

  function2()
  print(x)

function1()
print(x)
print(y)

# ------------------------------------------------------------ #

# What does this code output and why?

x = 5
y = 15

def function1():
  x = 10

  def function2():
      y = 20
      print(x)

  function2()
  print(x)

function1()
print(x)
print(y)

# ------------------------------------------------------------ #

# Variable Scope

name = 'Eli'

def my_function():
    print(name)
    name = 'Jon'

my_function()

# ------------------------------------------------------------ #
