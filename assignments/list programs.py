# write a program to merge a list

s=int(input("enter list:"))

list1=[]
for i in range(s):
    char=int(input("value of index"+str(i)+":"))
    list1.append(char)

s=int(input("enter list:"))
list2=[]
for i in range(s):
       char=int(input("value of index"+str(i)+":"))
       list2.append(char)
list1.extend(list2)
print(list1)









#sum of the list
'''
s=int(input("enter asize of list:"))
add=[]
for i in range(s):
    element=int(input("value of index"+str(i)+":"))
    add.append(element)
print(sum(add))'''



#print even numbers
'''
s=int(input("enter list:"))
add=[]
for i in range(s):
    element=int(input("value of index"+str(i)+":"))
    if element%2==0:
        add.append(element)
print(add)'''

#print odd number in list

'''s=int(input("enter list:"))
add=[]
for i in range(s):
    element=int(input("value of index"+str(i)+":"))
    if element%2!=0:
        add.append(element)
print(add)'''


#print the delete element of given index from list

'''i=int(input("enter a list:"))
s=int(input("index to be deleted:"))
list3=[]

for i in range(i):
    element=int(input("value of index"+str(i)+":"))
    list3.append(element)
for i in range(i):
    if i==s:
        list3.remove(list3[i])
print(list3)'''

    
#delete any element from list

'''
i=int(input("enter a list:"))
s=int(input("character to be deleted:"))
list4=[]

for i in range(i):
    element=int(input("value of index"+str(i)+":"))
    list4.append(element)
for i in list4:
    if i==element:
        list4.remove(s)
print(list4)'''

#insert element at given location
'''
s=int(input("enter a list size:"))
jak=int(input("enter where to insert:"))
value=int(input("enter what to insert:"))
list=[]
for i in range(s):
    char=int(input("enter value of"+str(i)+":"))
    list.append(char)
list.insert(jak,value)
print(list)'''

#insert element at last

'''s=int(input("enter a list size:"))
value=int(input("character to be insert:"))
list1=[]
for i in range(s):
    char=int(input("enter value of"+str(i)+":"))
    list1.append(char)
list1.append(value)
print(list1)
'''


#check size of two list
'''
first=input("enter list:")

second=input("enter list:")

if len(first)==len(second):
    print("both size same")
else:
    print("size not same")'''





















