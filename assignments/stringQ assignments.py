
'''input_string=input("enter a string:")
char_to_remove=input("enter the character to remove:")      
s=input_string.replace(char_to_remove,"")
print("new string",s)'''


#write a program to check the given string is palindrome or not
#
'''n=101
s=str
reverse=s[::-1]
if(s==reserve):
    print("yes it is palindrome")
else:
    print(" its not palindrome")'''

#write apython program to check given character is vowel or consonant

'''vowels=["a","e","i","o","u"]

num=input("enter word:")

for num in vowels:
    print("it is vowels")
else:
    print("its is consonent")'''


#write a python program to replace a string space with given character 

'''string="pythonchamp"
char_to_remove=""
newstring=""
string.replace(char_to_remove,"-")
print(newstring)'''
'''
s= "python champ"
replacing_string="-"
s1=s.replace(" ",replacing_string)
print(s1)'''


#write a python program to count alphabets ,digits ans spl charcters in stringg
'''
j=input("enter a string:")
alphabet=0
digit=0
specialcharater=0
for i in j:
    if i.isalpha():
        alphabet+=1
    elif i.isdigit():
        digit+=1
    else:
        specialcharater+=1
print("alphabet=",alphabet,"digit=",digit,"special character=",specialcharater)'''


#write a program to remove all the blank space in the given string

'''string="orange colour"
new_string= string.replace(" ","")
print(new_string)'''

#write a python program to find sum of integers in the string


'''str=input("enter a string:")
sum=0
for i in str:
    if i.isdigit():
        sum=sum+int(i)
print("sum=",sum)'''


#write a python program to remove the repeated character from string

'''s=input("enter a string:")
b=[]
i=0
while i<len(s):
    if s[i] not in b:
        b=b+[s[i]]
    i+=1
    print(b)
'''

#write  a  python program to count occurence of given character in string

'''count=0
my_string="programiz"
my_char="r"

for i in my_string:
    if i==my_char:
        count+=1
print(count)'''

#write a program t sort the character of string and first alphabet symbol followed by numeric values
'''
string=input("enter a string:")
alpha=[]
digit=[]
for c in string:
    if c.isalpha():
        alpha.append(c)
    else:
        digit.append(c)
result=''.join(sorted(alpha)+sorted(digit))
print(result)'''























