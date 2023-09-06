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

# write a dict , keys as alphabets and values as ascil num

'''dict={}
for asci in range(ord("a"),ord("z")):
    char=chr(asci)
    dict[char]=asci
print(dict)'''


#write a dict program ,keys as vowels and asci as values

'''dict={}

for asci in range(ord("a"),ord("z")):
    char=chr(asci)
    if char in "aeiou":
        dict[char]=asci
print(dict)'''

#d= {"goa":20,"bengalure":30,"hyderbad":40,"delhi":50,"simla":60,"andhrapradesh":70}

'''for key in d:
    print(key)'''

'''for key in d:
    if key[0] not in "aeiou":
        print(key)'''


'''for key in d:
    value=d[key]
    print(key,value)'''


'''for value in d.values():
    print(value)'''




'''for key,value in d.items():
    if value>30:
        print(key)'''

'''for key ,value in d.items():
    if value <30 and key[-1] in "aeiou":
        print(key,value)'''

'''s="hello"
count=0

for i in s:
    count=count+1
print(count)'''

#wap add all the words from the sentence as key and count of "i" in the word value

#s="get busy  living or get busy dying"
'''d={}
words=s.split()

for word in words:
    d[word]=word.count("i")
print(d)'''


#counting "a "character in string

'''c="a"
count=0
for char in s:
    if char ==c:
        count+=1
print(count)'''


#occurence of a number of words

'''s= "see and saw went to see the sea"
word=s.split()

items=input("enter a item:")
count=0

for char in word:
    if char==items:
        count+=1
print(count)'''



s= "see and saw went see to see the sea"

'''
words=s.split()
d={}
for word in words:
    c=s.count(word)
    d[word]=c
print(d)'''

'''words=s.split()
d={}
for word in words:
    count=0
    for item in words:
        if item==word:
            count+=1
    d[word]=count
print(d)'''
# only add if the word is repeated

'''jakeer=s.split()
d={}
for jak in jakeer:
    count=0
    for shaik in jakeer:
        if jak==shaik:
            count+=1
    if count>1:
        d[jak]=count
print(d)'''



































































































































