# In the previous problem, our first answer added 'Dino' to the list like this:

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
more_names = ["Dino", "Hoppy"]
flintstones.extend(more_names)

#How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? 
# Replace the call to append with another method invocation.

print(flintstones)

# LS ANSWER:

flintstones.extend(["Dino", "Hoppy"])