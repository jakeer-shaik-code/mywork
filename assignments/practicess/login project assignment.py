#1st method- to find single data
'''userid="jakeerh61@gmail.com"
password="thenun2"
userinput1=input("enter a username:")
userinput2=input("enter a password:")
if userinput1==userid and userinput2==password:
    print("your data is valid successfully login")
       
else:
    print("redirect to signup page")'''




# 2nd method - to find multiple data 


'''database={"jakeeer@gmail.com":"thenun2","virat@gmail.com":"thenun3","klrahul@gmail.com":"thenun4"}

username=input("enter a username:")
password=input("enter a  password:")

if username in database:
    database[username]==password

    print("move to next page interface as successful login")

else:
    print("data invaid move to previouse page interface as signup to new")'''


# 3rd method - to find multiple data with functions


'''def login(database):
    username=input("enter a username:")
    password=input("enter a  password:")

    if username in database and database[username]==password:
        print("move to next page interface as successful login")
    else:
         print("data invaid move to previouse page interface as signup to new")

database={"jakeer@gmail.com":"thenun2","virat@gmail.com":"thenun3","klrahul@gmail.com":"thenun4"}

login(database)'''