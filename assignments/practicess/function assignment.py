
# 1.Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

'''def counting_upper_lower_cases(string):
    upper_char=0
    lower_char=0
    for i in string:
        if i.isupper():
            upper_char+=1
        elif i.islower():
            lower_char+=1
        else:
            pass
    print(upper_char)
    print(lower_char)


stri=input("enter a input:")
counting_upper_lower_cases(stri)'''

# 2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def remove_repeated(s):
    my_list=[]
    for i in s:
        if i not in my_list:
            my_list.append(i)
    print(my_list)

list=[1,2,3,3,3,3,4,5]
remove_repeated(list)
# 3.Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog".

'''def pangram(s):
    s=s.replace(" ","")
    s=s.lower()
    alphabets="abcdefghijklmnopqrstuvwxyz"
    j=0
    for i in s:
        if i in alphabets:
            j+=1
    if(j==len(alphabets)):
        print("pangram")
    else:
        print("not pangram")

pangram_child="The quick brown fox jumps over the lazy dog"
pangram(pangram_child)

o/p:- not pangram'''

# 4.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included).
'''def squarevalues(a,b):
    jack=[]
    for i in range(a,b):

        j=i**2
        jack.append(j)
    return (jack)

print(squarevalues(1,11))'''



# 5.Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 

'''def sum_num(list):
    add=0
    for i in list:
        add=add+i
    print(add)
list=(8, 2, 3, 0, 7)
sum_num(list)'''

# 6.write a function to find sum of given values, pass values has variable number of arguments to function.

def sum_of_values(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_of_values(1,2,3,4,5))














