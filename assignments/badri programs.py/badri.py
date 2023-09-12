#enumerate---it return a tuple containing a count from starting which
# is default 0,and value obtained from iterating over iterable

'''s={"a","b","c"}
obj=list(enumerate(s,100))
print(obj)'''

'''s="hello"
for index,char in enumerate(s,2):
    print(index,char)'''


#zip---



'''subject=["maths","phy","chem","bio","py"]
marks=[20,40,30,60,80,90]
attendance=[10,12,15,18,20]
obj=zip_longest(subject,marks,attendance)
print(tuple(obj))'''

#from itertools import zip_longest

'''from itertools import zip_longest
subject=["maths","phy","chem","bio","py"]

attendance=[10,12,15]
obj=list(zip_longest(subject,attendance,fillvalue="absent"))
print(obj)'''



# check prime number till N

'''
N=int(input("entyer a num:"))

number=2
count=0
while count<N:
    for i in range(2,number):
        if number%i==0:
            number+=1
            break
    else:
        print(number)
        number+=1
        count+=1'''





'''a=int(input("enter num:"))
out="prime"
for i in range(2,a):
    if a%i==0:
        out="not prime"
        break
print(out)'''



'''for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)'''


'''N=int(input("enter a num:"))
n1=0
n2=1
for i in range(1,N+1):
    print(n1)
    res=n1+n2
    n1=n2
    n2=res'''

#natural number


'''s=int(input("enter a num:"))
jack=0
l=[]
for i in range(1,s+1):
    jack+=1**2
    
    l.append(jack)

print(l)'''


'''km=int(input("enter a km:"))
rupee=0
for kilometer in range(1,km+1):
    if 1<=km<=90:
        rupee+=11
    elif 90<=km<=150:
        rupee+=10
    else:
        rupee+=9
print(rupee)'''
    


# natural num
'''n=int(input("enter a num:"))
s=0
for num in range(1,n+1):
    s+=num
print(s)'''
# wap in function collection and cal the length
'''def length(collection):
    count=0
    for item in collection:
        count+=1
    print(count)
length("hello")
length([1,2,3])'''

#wap 2 number as parameter and give sum

#formatting string:-
'''
string="hello {},your age is {}"

print(string.format("jack",22))
print(string.format("naim",28))
print(string.format(88,"jakeer"))'''


'''string="hello {name}, your age is {age}"

print(string.format(name="jack",age=33))
print(string.format(name="jakeer",age=77))
print(string.format(age=99,name="rizwan"))'''


#input=a2b3c1d4
#output=aabbbcdddd

'''def pattern (string):
    for index in range(len(string)):
        char=string[index]
        if char.isalpha():
            print(char*int(string[index+1]))
pattern ("a2b3c1d4")'''
'''
def pattern(j):
    a=[]
    n=[]
    for i in j:
        if i.isalpha():
            a+=[i]
        else:
            n+=[i]
    l=len(a)
    res=" "
    for i in range(l):
        alp=a[i]
        num=int(n[i])
        r=(alp*num)
        res+=r
    print(res)

j="a2b3c1d4"
pattern(j)'''


#replace the prime num into the $

#input=[2,3,4,5,6,7,8,9,10]
# output=[$,$,4,$,6,$,8,]

'''l=[2,3,4,5,6,7,8,9,10]

for index in range(len(l)):
    number=l[index]
    for num in range(2,number):
        if number%num==0:
            break
    else:
        l[index]="$"
print(l)'''




#wap to calculate the count of spl characters in string


'''def special(s):
    count=0
    index=0
    if index<len(s):
        char=s[index]
        if not char.isalnum():
            count+=1
        index+=1
        
    else:
        print(count)




s="www.python.org"
special(s)
'''
#input=[2,3,4,5,6,7,8,9,10]
# output=[$,$,4,$,6,$,8,]

'''l=[2,3,4,5,6,7,8,9,10]

for index in range(len(l)):
    number=l[index]
    for num in range(2,number):
        if number%num==0:
            break
    else:
        l[index]="$"
print(l)'''


# calculate the bill of order
'''menu={"veg loaded":120,"chess_loaded":180,"non_veg loaded":230}
additionals={"extra chess":20,"extra ketup":30}

a=input("enter pizza name:")
b=int(input("enter quantity:"))
c=input("enter a add on,type 1 else type 0:")

bill=0

if a in menu:
    b=menu[a]*b
    bill=bill+b

    if c=="1":
        d=input("enter add on:")
        if d in additionals:
            bill+=additionals
            print(f'total bill:{bill}')
        else:
            print("add on not found")
    else:

        print(f'total bill:{bill}')'''



'''userid="jakeerh61@gmail.com"
password="thenun2"
userinput1=input("enter a username:")
userinput2=input("enter a password:")
if userinput1==userid and userinput2==password:
    print("your data is valid successfully login")
       
else:
    print("redirect to signup page")'''


database={"jakeeer@gmail.com":"thenun2","virat@gmail.com":"thenun3","klrahul@gmail.com":"thenun4"}

username=input("enter a username:")
password=input("enter a  password:")

if username in database:
    database[username]==password

    print("move to next page interface as successful login")

else:
    print("data invaid move to previouse page interface as signup to new")


'''def login(database):
    username=input("enter a username:")
    password=input("enter a  password:")

    if username in database and database[username]==password:
        print("move to next page interface as successful login")
    else:
         print("data invaid move to previouse page interface as signup to new")

database={"jakeer@gmail.com":"thenun2","virat@gmail.com":"thenun3","klrahul@gmail.com":"thenun4"}

login(database)'''





















































































