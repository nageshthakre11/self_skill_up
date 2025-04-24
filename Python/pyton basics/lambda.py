# add 10 to given number 
add_10 = lambda x: x + 10
print(add_10(51))

# get square of number 
square_number =  lambda x: x**2
print(square_number(10))


# number is even or not 
is_even = lambda x: True if x%2==0 else False
print(is_even(11))

# get max number 
max_number = lambda x,y: max(x,y)
print(max_number(100,11))


# get max number alternate solution  
max_number = lambda x,y: x if x > y else y
print(max_number(x,y))


# map in lambda function
# Use a lambda function inside the map() function to convert a list of numbers into their cubes.
numbers = [1, 2, 3, 4, 5]
qubes_list = list(map(lambda x: x**3, numbers))
qubes_tuple = tuple(map(lambda x: x**3, numbers))
print(qubes_list, '\n', qubes_tuple)


# filter in lambda function
# get list / tuple of even number
numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even_num = list(filter(lambda x: x % 2 ==0, numbers))
even_num = tuple(filter(lambda x: x % 2 ==0, numbers))
print(even_num)


# reduce function in lambda 
# get sum or multiplication of values present in list
from functools import reduce
numbers = [4, 5, 6, 7, 9]
total_sum = reduce(lambda x, y: x + y, numbers)
multi = reduce(lambda x, y: x*y, numbers)
print(total_sum)
print(multi)

# sorted in lambda function 
# sort the tuple based on second element
pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pair = sorted(pairs, key = lambda x: x[1])
print(sorted_pair)



# Given a dictionary of employees with their salaries, use a lambda function to sort the dictionary by salary in descending order.
employees = {"Alice": 5000000, "Bob": 70000, "Charlie": 60000}
l = sorted(employees.items(), key = lambda x: x[1], reverse = True)
print(l)


# Use a lambda function to find the longest word in a list of strings.
# Example: ["apple", "banana", "cherry", "blueberry"] → "blueberry"
Example = ["apple", "banana", "cherry", "blueberry"]
k = max(Example, key = lambda x: len(x))
print(k)