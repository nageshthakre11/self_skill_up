
# square of number from 1 to 10
l = [i**2 for i in range(1,11)]
print(l)


# list of even number from 1 to 20 
l = [i for i in range(1,21) if i%2 == 0]
print(l)


# Convert a list of strings to uppercase
l = ['nagesh','thakre']
upper_l = [i.upper() for i in l]
print(upper_l)


# Create a list of tuples where each tuple contains a number and its square for numbers from 1 to 10.
tupple_list = [(i,i*i) for i in range(1,11)]
print(tupple_list)


# Generate a list of all numbers from 1 to 50 that are divisible by both 3 and 5.
l = [i for i in range(1,51) if i % 3 == 0 and i % 5 == 0]
print(l)


# Given a list of words, create a new list containing only words that have more than 4 letters.
l = ["apple", "is", "good",'new','sal','pink','salman','sharukh','nikil']
new_l = [i for i in l if len(i) >= 4]
print(new_l)


# Flatten a nested list using list comprehension.
l = [[1, 2, 3], [4, 5], [6, 7, 8]]
new_l = [k for i in range(len(l)) for k in l[i]]
print(new_l)


# Advanced Level:
# Generate a list of prime numbers between 1 and 50 using list comprehension.
l = [i for i in range(2,51) if all (i % k != 0 for k in range(2,int(i**0.5)+1))]
print(l)

# Create a dictionary from a list using dictionary comprehension, 
# where keys are numbers from 1 to 5 and values are their cubes.
d = {i:i**3 for i in range(1,6)}
print(d)


# Given two lists, generate a list of all possible pairs using list comprehension.
list1 = [1, 2]  
list2 = ['a', 'b']  
# Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
p = [(i,k) for i in list1 for k in list2]
print(p)







