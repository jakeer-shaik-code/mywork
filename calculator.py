#1.write a program to create a calculator using functions (sum,sub,mul,div).
'''def mul(a,b):
    print(a*b)

def sum(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def div(a,b):
    print(a/b)

a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
calculate = int(input("enter your choice number: "))
if (calculate == 1):
    sum(a,b)
elif (calculate== 2):
    sub(a,b)
elif (calculate == 3):
    mul(a,b)
elif (calculate == 4):
    div(a,b)
else:
    print("enter the valid choice number")'''




#Variable length arguments. 
#2. Write a program to enter employee details and also filter the stored employee  details  with name and empid and designation and email. 
'''Employees = {}
def add_employee():
    name = input("enter the employee name: ")
    empid = input("enter the employee id: ")
    email = input("enter the employee email id: ") 
    designation = input("enter the employee designation: ")
    Employees[name] = {'empid':empid, 'emailid':email, 'designation':designation}
    print("employee details added successfully")

def fliter_details():
    designation = input("enter fliter designation: ")
   
    for key , value in Employees.items():
        if (value['designation'] == designation):
            print(key,value)
            
no_of_employees = int(input("enter number of employees: "))
for i in range(no_of_employees):
    add_employee()
print(Employees) 


fliter_details()'''




















