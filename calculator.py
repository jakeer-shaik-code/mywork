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


#########################3shopping cart############################

class ShoppingCart:
    def __init__(self):
        self.items_list = []
        self.prices = []
        self.menu()
    
    def menu(self):
        while True:
            print("Welcome to Shopping Cart Program!")
            print()
            print("Please select one of the following:\n" "1. Add Items\n" "2. View Cart\n" "3. Remove Items\n" "4. Compute Total\n" "5. quit\n")           
            action = input("Please enter the action: ")
            print()          
            if(action == "1"):
                self.add_items()
            elif(action == "2"):
                self.view_cart()
            elif(action == "3"):
                self.remove_items()
            elif(action == "4"):
                self.compute_total()
            elif(action == "5"):
                self.quit()
            else:
                print("select any one of the following options")
            
    def add_items(self):
        Item = input("What item would you like to add: ")
        self.items_list.append(Item)
        price = float(input(f"what is the price of '{Item.capitalize()}': "))
        self.prices.append(price)
        
        print(f"'{Item.capitalize()}' has been added to the cart Successfully.\n")
        
    def view_cart(self):
        print("The Items in your Cart are: \n")
        for i in range(len(self.items_list)) and range(len(self.prices)):
            item = self.items_list[i]
            price = self.prices[i]
            items = (f'{i+1}. {item.capitalize()} - {float(self.prices[i])}')
            print(items)
            print()
    
    def remove_items(self):
        index = int(input("What item would you like to remove: "))
        self.items_list.pop(index-1)
        self.prices.pop(index-1)
        print("The selected item removed successfully")
        
    def compute_total(self):
        total = 0
        for i in range(len(self.items_list)):
            total += float(self.prices[i])
        print(f"The total price of the items in the shopping cart is {total}")
               
    def quit(self):
        print("Please visit us Again and spent some money here!")  
        print()
            
        
ShoppingCart()

































