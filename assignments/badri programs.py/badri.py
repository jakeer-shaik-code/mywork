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
    
































