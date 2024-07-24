# Alyssa was asked to write an implementation of a rolling buffer. 
# You can add and remove elements from a rolling buffer. However, 
# once the buffer becomes full, any new elements will displace the 
# oldest elements in the buffer.

# She wrote two implementations of the code for adding elements to the buffer:

# Is there a difference between these implementations, other than 
# the way she is adding an element to the buffer?

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# My Answer: Yes there is a difference. In the 1st function, the 
# buffer.append method will add the new_element to the end of the
# buffer list. In the the 2nd function, the buffer + new_element 
# approach will simply add the string of new_element to the string
# of buffer. This will not add to the list length of the rolling
# buffer.

# LS ANSWER:
# Yes, there is a difference. The first function (add_to_rolling_buffer1) 
# mutates the original list represented by buffer. The second function 
# (add_to_rolling_buffer2) does not mutate the original list, but instead 
# creates a new list and assigns it to buffer, whose value ultimately gets 
# returned by the function.