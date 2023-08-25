#1 . write a  program to Add key to dictionary 

# dis={}

# old_key=input("enter key:")
# old_value=input("enter  value:")
# new_key=input("enter key:")
# new_value=input("enter value:")

# dis[old_key]=old_value
# dis[new_key]=new_value

# print(dis)




#2 .write a program to check is dict already has a key
# dis={}
# for i in range(3):
#     key=input("enter keys: ")
#     value=input("enter values: ")
#     dis[key]=value
# k=input("Enter key :")

# if k in dis:
#     print("Key already exits")
# else:
#     print("Key doesnt exist.")


#3 write program to iterate over dictionary.
# dis={}
# for i in range(3):
#     key=input("enter keys: ")
#     value=input("enter values: ")
#     dis[key]=value

# for i in dis.items():
#     print(i)

#our=dict()
#4 create dictionaries using keys from (1-15) and values are squares.

# num=dict()
# for i in range(1,16):
#     n=(i)
#     s=i**2
#     num.update({n: s})
# print(num)


#5 count occurances of string and fill it in dictionary
# s=input("enter string : ")
# num=dict()
# for i in s:
#     if i in num:
#         pass
#     else:
#         num.update({i: s.count(i)})
# print(num)



#6 sum all items in dictionary
# num={}
# for i in range(3):
#     key=input("enter name: ")
#     value=int(input("enter age: "))
#     num[key]=value
# sum_of_age=0
# for i in num.values():
#     sum_of_age=sum_of_age+i

# print(sum_of_age)

##7 combine values of 2  dictinaries if keys are common
# dic1={}
# for i in range(3):
#     key=input("enter key:")
#     value=input("enter value: ")
#     dic1[key]=value
# dic2={}
# for k in range(0,5):
#     key=input("enter key: ")
#     value=input("enter value:")
#     dic2[key]=value
# for x,y in dic2.items():
#     if x in dic1:
#         dic1[x]=dic1[x]+dic2[x]
#     else:
#         dic1.update({x:y})


# print(dic1)


#8 access dictionary key elemnet by indexing
# num={}
# for k in range(3):
#     key=input("enter keys")
#     value=input("enter values")
#     num[key]=value
# print(num)


 

#9 remove key from dictionary
# dic={}
# for k in range(4):
#     key=input("enter keys")
#     value=input("enter values")
#     dic[key]=value
# item=input("Enter item to be removed: ")
# del dic[item]
# print(dic)

#10 merge two python dictionaries
# dic1={}
# for k in range(4):
#     key=input("enter keys: ")
#     value=input("enter values: ")
#     dic1[key]=value
# dic2={}
# for k in range(4):
#     key=input("enter keys: ")
#     value=input("enter values: ")
#     dic2[key]=value
# dic1.update(dic2)
# print(dic1)













































