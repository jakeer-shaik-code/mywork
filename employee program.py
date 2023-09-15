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

# multiple employe at  same time
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





