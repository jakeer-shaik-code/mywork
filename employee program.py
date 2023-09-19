# general form(single employee)-functions 
'''def details():
    empdetails={}
    name=input("enter a empname:")
    domain=input("enter a domain:")
    empid=input("enter a empid:")
    email=input("enter a email:")
    empdetails["name"]=name
    empdetails["domain"]=domain
    empdetails["empid"]=empid
    empdetails["mail"]=email
    print(empdetails)
details()'''

#multiple employee details-

'''def details():
    empdetails={}
    num_of_employee=int(input("enter a num:"))
    for i in range(num_of_employee):
        name=input("enter a empname:")
        domain=input("enter a domain:")
        empid=input("enter a empid:")
        email=input("enter a email:")
        empdetails["name"]=name
        empdetails["domain"]=domain
        empdetails["empid"]=empid
        empdetails["mail"]=email
        print(empdetails)

details()'''

# multiple employe at same time
'''
def details():
    empdetails={}
    num_of_employee=int(input("enter a num:"))
    for i in range(num_of_employee):
        name=input("enter a empname:")
        domain=input("enter a domain:")
        empid=input("enter a empid:")
        email=input("enter a email:")
        empdetails["name"+str(i)]=name
        empdetails["domain"+str(i)]=domain
        empdetails["empid"+str(i)]=empid
        empdetails["mail"+str(i)]=email
    print(empdetails)

details()'''


########################################


##single employee
'''empdetails={}
def employee():

    num_of_emp=int(input("enter a num:"))
    for i in range(num_of_emp):
        domain=input("enter a domain:")
        name=input("enter a empname:")
        empid=input("enter a empid:")
        email=input("enter a email:")   
        empdetails[domain]={"name":name,"domain":domain,"empid":empid,"email":email}
def employeeoverview():
    domain=input("enter a specific domain:")
    s= empdetails.get(domain)
    for key,values in s.items():
        print(f"{key}:{values}")

employee()
employeeoverview()'''
## multiple employees
'''
def output():
    employee_list={}
    py_list=[]
    dev_list=[]
    test_list=[]
    num_of_employees=int(input("enter s employee:"))
    for i in range(num_of_employees):
        domain=input("enter a domain:")
        name=input("enter a empname:")
        empid=input("enter a empid:")
        email=input("enter a email:") 
        employee_details={"name":name,"empid":empid,"email":email}
        if domain=="python":
            py_list=py_list+[employee_details]
            employee_list["python"]=py_list
        elif domain =="devops":
            dev_list=dev_list+[employee_details]
            employee_list["devops"]=dev_list
        elif domain =="testing":
            test_list=test_list+[employee_details]
            employee_list["testing"]=test_list
    
    specific_domain=input("enter a specific domain:")
    print(employee_list.get (specific_domain))

output()'''


