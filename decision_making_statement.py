"""# if else statement
acutal_password="lumbini"
password=input("enter your password:")
if password == acutal_password:
    print("Access Granted")
else:
    print("Access Denied")    
"""
"""# prob.2  if else
user_name="aakriti"
R_password="Poudel"
user=input("enter your user name:")
password=input("enter your password:")
if user==user_name and password==R_password:
    print("Access Granted")
else:
    print("Accessed Denied")    
"""
# Nested if else statement
num = int(input("enter a number to check if it is divisible by 2 and 3:"))  
print(num)
if(num%2==0):
    if(num%3==0):
        print(f"number{num} is divisible by both 2 and 3")
    else:
        print(f"the number{num} is divisible by 2 ")
else:
    print("the number is not divisible by 2 and 3")
