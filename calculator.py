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

######################################## calculator using oops#################################

class Calculator:
    def __init__(self):
        print("CALCULATOR")
        self.display()
        
    
    def display(self):
        print(''' Select Which operations do you need
        1.Addition
        2.Subtarction
        3.Multipliaction
        4.Divison
        Press 1 for Add , 2 for sub, 3 for Mul, 4 for Div''')
        
        n = int(input("Enter the value:"))
        self.numbers = list(map(int,input("Enter number of values:").split()))
        if(n == 1):
            self.add(self.numbers)
        elif(n == 2):
            self.sub(self.numbers)
        elif(n == 3):
            self.mul(self.numbers)
        elif(n == 4):
            self.div(self.numbers)    
        else:
            print("select one")
              

    def add(self,numbers):
        print(f'Sum of numbers is {sum(numbers)}')
        

    def sub(self,numbers):
        output = self.numbers[0]
        for i in self.numbers[1:]:
           result -= i  
        print(f'Subtraction of numbers is {output}')
           

    def mul(self,numbers):
        output = 1
        for i in self.numbers[0:]:
            result *= i 
        print(f'Multipliaction of numbers is {output}') 
         

    def div(self,numbers):
        output = self.numbers[0]
        for i in self.numbers[1:]:
           result /= i  
        print(f'Division of numbers is {output}')
                 
              
c = Calculator()
print("come again")






































