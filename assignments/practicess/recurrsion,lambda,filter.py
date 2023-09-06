# Recuursion 
# wap to extract uppercase vowel character in string

'''def vowel(s,i=0,out=""):
    if i >len(s):
        return out
    if i%2==1 and s[i] in "AEIOU":
        out+=s[i]
    return vowel(s,i+1,out)
s="HAPPY DIWALI"
print(vowel(s))'''

# recurrsion to find factorial of the given number

'''def fact(n,i=1,out=1):
    if i>n:
        return out
    out*=i
    return fact (n,i+1,out)
n=int(input("enter a number:"))
print(fact(n))'''



#lambda:-

# define a function which can take a string and retur last character in string

'''last=lambda string:string[-1]
print(last("hello"))'''


# function add two numbers

# normal fun
#def add(n1,n2):
#    return n1+n2
#lambda
#add =lambda n1,n2:n1+n2

# fliter
# wap to get odd number


'''odd= lambda n: n%2==1
l=[1,2,3,4,5,6,7]
res= filter(odd,l)
print(list(res))'''


# eligible ages  for votes

'''def func(x):
    if x >=18:
        return True
    else:
        return False
age=[10,18,33,55,88,16]
adults=list(filter(func,age))
print(adults)'''












































