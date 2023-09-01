#sum of intergers in string
'''
st=input("enter a string:")
s=[]
for i in st:
    if i.isdigit():
        s=s+[int(i)]
print(sum(s))'''


#write a program to find , it is anagram or not
'''st1=input("enter a string:")
st2=input("enter a string:")
s=[]

for i in st2:
    s=s+[i]

count=0
if len(st1)==len(st2):
    for i in st1:
        if i in s:
            if st1.count(i)==st2.count(i):
                count=count+1
        else:
            pass
if count==len(st2):
    print("anagram")
else:
    print("not anagram")'''

#print a program to count the alphabet, and digits and spl characters 

'''s=input("enter a string:")

alphabet=0
digit=0
spl_character=0

for i in s:
    if i.isalpha():
        alphabet=alphabet+1
    elif i.isdigit():
            digit=digit+1
    else:
         spl_character=spl_character+1
print("alphabets=",alphabet,"digit=",digit,"specical characters=",spl_character)
'''

# write a program to remove character from string

'''s=input("enter a string:")
ch=input("removal character")
method=s.replace(ch," ")
print(method)'''

# write palindrome program

'''st1=input("enter a string:")
st2=st1[::-1]
if st1==st2:
    print("palindrome")
else:
    print("not palindrome")
'''
#write a program to find vowel or consonent
'''
vowels="a,e,i,o,u,A,E,I,O,U"
s=input("enter a string:")

for s in vowels:
    print("vowels")
else:
    print("consonents")'''

#write a program replace string space with character

'''s=input("enter a string:")
ch=" "
method=s.replace(ch,"-")
print(method)'''


#remove repeated values
'''
st=input("enter a string:")
li=[]
set=set()
for i in st:
    if st.count==1:
        li=li+[i]
    else:
        set.add(i)
method=li+list(set)
print(method)'''
#remove the repeated valuies

'''st=input("enter a string:")
b=[]
i=0
while i<len(st):
    if st[i] not in b:
        b=b+[st[i]]
    i+=1
print(b)'''
        

#write a program to sort the alpha followed by the numeric

'''st=input("enter a string:")
alpha=[]
digit=[]

for i in st:
    if i.isdigit():
        digit=digit+[i]
    elif i.isalpha():
        alpha=alpha+[i]
result=alpha+digit

final="".join(result)
print(final)
'''



















































