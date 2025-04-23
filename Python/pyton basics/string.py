############### Reverse String ######################
# solution 1
s = 'Nagesh Thakre'
rev = s[::-1]
print(rev)
rev_1 = ''

# solution 2
for char in s:
    rev_1 = char + rev_1
print(rev_1)

############### Check if a string is a palindrome #################

s = 'madAm'
s_rev = s[::-1]

if s.lower() == s_rev.lower():
    print('Palindrome')
else:
    print('Not Palindrome')

################## Count the vowels in a string #########################

s = 'Nagesh Rameshwar Thakre'
vowels = 'aeiou'
count = 0
for v in s.lower():
    if v in vowels:
        count += 1
print(count)


################ Check if two strings are anagrams ################
# sol 1

s1 = 'Silent'
s2 = 'Listen'

s11 = sorted(list(s1.lower()))
s22 = sorted(list(s2.lower()))

if s11 == s22:
    print('Anagrams')
else:
    print('Not Anagrams')


############ Remove all duplicates from a string #################3

s = 'jawaniaabbbcccdddeefffggghhhijklm'
p = list(s)
s1 = ''
for i in p:
    if i not in s1:
        s1 += i
    
print(s1)

################  Find the first non-repeating character #############
s = 'allavi nagesh Thakre'
d = {}
for i in s.lower():
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
        
for k, v in d.items():
    if d[k] == 1:
        print(k)
        break


############## Check if a string contains only digits ##################


s = '12344a'

try:
    v = int(s)
    print(f'{s} have only degits')
except Exception as e:
    print(f'{s} have other character apart from digit')



############### Capitalize the first letter of each word   ###############

s = 'nagesh rameshwar thakre'
print(s.title())


################# Find the longest word in a sentence #################

s = 'I love programmminggg, lets kabhikhushikabhigum'
l = s.split(' ')
l_1 = len(l[0])
for i in l:
    if l_1 <= len(i):
        l_1 = len(i)
        longest_word = i
print(l_1, longest_word)


############# Implement a basic string compression #################

# Input: "aaabbcc" → Output: "a3b2c2"
s = 'aaaaaabbbbbbbbbccccccdddddddeeerrffgjsk'
new_s = ''

d = {}

for c in s:
    if c not in d.keys():
        d[c] = 1
    else:
        d[c] += 1
print(d)

for k, v in d.items():
    new_s  = new_s + k + str(v)
print(new_s)


############  get the number from string  ###################


s = 'a1b2c3'
#output --> 1 2 3

for c in s:
    try:
        ss =  int(c)
        print(ss, end = ' ')
    except Exception as e:
        pass