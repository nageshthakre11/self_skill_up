# Remove Duplicates from a List
nums = [1, 3, 2, 1, 3, 4, 2]   

l = []
for u in nums:
    if u not in l:
        l.append(u)       
print(l)


# Flatten a Nested List
l = [9, 7, 8, [1, 2], [3, 4], [5]]
new_list = []

for i in l:
    if isinstance(i, list):
        new_list.extend(i)
    else:
        new_list.append(i)
print(new_list)


################# Find the Most Frequent Element #########################

items = [4, 2, 2, 3, 3, 3, 4,4,4,4,4]
x = 0

for i in items:
    if x < items.count(i):
        x = items.count(i)
        num = i 
        
print(num, x)


############### Rotate a List by k Positions #######################

l = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

new_l = list(range(len(l)))
k = 2

for i in range(len(l)):
    new_l[i] = l[(i + k) % len(l)]
    
print(new_l)
    

# Chunk a List into Smaller Lists

l =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]

k  = 4

list_len = len(l)

if list_len % k == 0:
    slice_range = int(list_len / k)
else:
    slice_range = int((list_len // k) + 1)
    
start = 0
end = slice_range
    
for i in range(k):
    print(l[start:end])
    start = end
    end = end + slice_range





# Intersection of Two Lists

l = list(range(10))
l1 = list(range(5,16))
new_l = list()
print(l,'\n', l1)

for i in l:
    if i in l1 and i not in new_l:
        new_l.append(i)
        
print(new_l)




#  Find Pair with Given Sum target
target = 12

l = list(range(1, 12, 2))
print(l)
new_l = []
for i in range(len(l)-1):
    for j in range(i, len(l)):
        if l[i] + l[j] == target:
            t = (l[i],l[j])
            new_l.append(t)
print(new_l)



#######################################

nums = [4, 1, 9, 7, 3, 9]
# sort te list without function 
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        #print(nums[i], nums[j])
        if nums[i] < nums[j]:  # < for decreseing, > for increseing 
            nums[i], nums[j] = nums[j], nums[i]
            
# sorted list with removing the duplicate records       
x = [4, 1, 9, 7, 3, 9]
print(list(set(x)))


#########################################################

# Remove duplicates from a list while maintaining order

input_list = [1, 2, 2, 3, 1, 4]
new_list = []
for i in range(len(input_list)):
    if input_list[i] not in new_list:
        new_list.append(input_list[i])
print(new_list)  

###############################################################################

# Rotate a list to the right by k steps
nums = [11, 12, 13, 14, 15,12,43, 54, 65]   
new_list = [0 for i in range(len(nums))]
k = -2

for i in range(len(nums)):
    new_list[i] = nums[(i+k) % len(nums)]
print(new_list)

##################################################################################

 
list1 = [1, 2, 3] 
list2 = [2, 3, 4] 
# common element → [2, 3]

common_element = [ i for i in list1 if i in list2]
print(common_element)
####################################################################


# flattern the nested list 
nested = [1, [2, [3, 4], 5], 6] 

# output needed → [1, 2, 3, 4, 5, 6]

def flattern_list(nested):
    new_list = []
    for i in nested:
        if isinstance(i, list):
            new_list.extend(flattern_list(i))
        else: 
            new_list.append(i)
    return new_list
    
print(flattern_list(nested))

#######################################################

# count the freq of elements
input = ['apple', 'banana', 'apple', 'orange']
d = {}

for i in input:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)

####################################
# find key with maximum value 
d = {'a': 5, 'b': 9, 'c': 2} 

listed_keys = list(d.keys())
max_value = d[listed_keys[0]]

for i in d.keys():
    if d[i] > max_value:
        max_value = d[i]
        max_key = i
print(max_key, max_value)

####################################

# revert the dictonary 
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

new_d = {}
for k,v in d.items():
    new_d[v] = k
print(new_d)

####################################################################

# Merge two dictionaries. If same key, sum the values
d1 = {'a': 1, 'b': 2}
d2 = {'a': 3, 'c': 5}

for k in d1.keys():
    if k in d2.keys():
        d2[k] += d1[k]
    else: 
        d2[k] = d1[k]
        
print(d2)
################################################################


# group items by keys in list 

data = [
    {"name": "Alice", "dept": "IT"},
    {"name": "Bob", "dept": "HR"},
    {"name": "Charlie", "dept": "IT"},
]

# output → {'IT': ['Alice', 'Charlie'], 'HR': ['Bob']}

d = {}

for i in data:
    d[i['dept']] =[]
    
for i in data:
    d[i['dept']].append(i['name'])
    
print(d)

#####################################################


