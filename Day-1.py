full_name=input("Enter Full name:")
email=input("Enter your E-mail ID:")
mobile_num=input("Enter Mobile number:")
age=int(input("Enter your age:"))
valid=True
if(full_name[0]==" " or full_name[len(full_name)-1]==" "):
    valid=False
elif(full_name.count(" ")<1):
    valid=False
if(email.count("@")<1 or email.count(".")<1):
    valid=False
elif(email[0]=="@"):
    valid=False
if(len(mobile_num)!=10):
    valid=False
elif((mobile_num.isdigit()==False)):
     valid=False
elif(mobile_num[0]=="0"):
    valid=False
if(age<18 or age>60):
    valid=False
if valid:
    print("User profile is VALID")
else:
    print("User profile is INVALID")
