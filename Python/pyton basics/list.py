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
