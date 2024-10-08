# Write a function that takes a positive integer, n, as an argument and 
# prints a right triangle whose sides each have n stars. The hypotenuse 
# of the triangle (the diagonal side in the images below) should have one 
# end at the lower-left of the triangle, and the other end at the upper-right.

def triangle(number):
    for n in range(number + 1):
        print((' ' * (number - n)) + ('*' * n))

triangle(9)


# LS ANSWER:

def triangle(height):
    for num in range(1, height + 1):
        spaces = height - num
        stars = num
        print(f'{" " * spaces}{"*" * stars}')
