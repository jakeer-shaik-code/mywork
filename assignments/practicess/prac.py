#add the key to the dic

'''jack={}
for i in range(2):
    key=input("enter a key:")
    value=input("enter a value:")
    jack[key]=value
num={}
for j in range(2):
    k=input("enter a keys:")
    v=input("enter a values:")
    num[k]=v
jack.update(num)
print(jack)'''

#or

'''k=input("enter a keys:")
v=input("enter a values:")
add={k:v}
jack.update(add)
print(jack)'''


#7.Write a Python program to combine two dictionary by adding values for common keys.

'''jack={}

for i in range(2):
    key=int(input("enter a key:"))
    value=int(input("enter a value:"))
    jack[key]=value

jakeer={}
for j  in range(2):
    keys=int(input("enter a keys:"))
    values=int(input("enter a values:"))
    jakeer[keys]=values


for x,y in jakeer.items():
    if x in jack:
        jack[x]=jack[x]+jakeer[x]
    else:
        jack.update({x:y})

print(jack)'''




#9.Write a Python program to remove a key from a dictionary


'''
jack={}

for i in range(2):
    key=input("enter a key:")
    value=input("enter a value:")
    jack[key]=value

k=input("enter a removal key:")
del jack[k]
print(jack)'''




#6 sum all items in dictionary
'''jack={}
for i in range(3):
    key=input("enter name: ")
    value=int(input("enter age: "))
    six[key]=value

sum=0
for i in jack.values():
    sum=sum+i
print(sum)'''


#5.Write a Python program to create a dictionary from a string.



'''s=input("enter string : ")
five=dict()

for i in s:
    if i in five:
        pass
    else:
        five.update({i:s.count(i)})

print(five)'''


# 2.Write a Python script to check whether a given key already exists in a dictionary.

'''jack={}

for i in range(2):
    key=input("enter a key:")
    value=input("enter a value:")
    jack[key]=value
k=input("enter a k:")

if k in jack:
    print("key is exist")
else:
    print("not exist")
'''


# 3.Write a Python program to iterate over dictionaries using for loops

'''jack={}

for i in range(2):
    key=input("enter a key:")
    value=input("enter a value:")
    jack[key]=value

for i in jack.items():
    print(i)'''

# 4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
'''jack=dict()
for i in range(0,16):
    k=i
    v=i**2
    jack.update({k:v})

print(jack)'''
    
#write a function to count the upper case and lower case and space and spl char

# def countingupperlower(num):
#     uppercase=0
#     lowercase=0
#     space_count=0
#     spl_character=0
#     for i in num:
#         if i.isupper():
#             uppercase+=1
#         elif i.islower():
#             lowercase+=1
#         elif i.isspace():
#             space_count+=1
#         else:
#             spl_character+=1
#     print(uppercase)
#     print(lowercase)
#     print(space_count)
#     print(spl_character)



# my_string=input("enter a string:")
# countingupperlower(my_string)
    


#write a function  program to remove the duplicate in the list
'''
def removeduplicate(num):
    list=[]
    for i in num:
        if i not in list:
            list.append(i)
    print(i)
l=[2,3,3,4,5,4,2,1,8,7,6,5,8,7,32]
removeduplicate(l)'''


#



















































