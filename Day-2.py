student_id=input("Enter Student ID:")
email=input("Enter email ID:")
password=input("Enter Password:")
referral=input("Enter Referral Code:")
valid=True
if(student_id[:3]!="CSE"):
   valid=False
elif(student_id[3]!='-'):
   valid=False
elif(student_id[4:7].isdigit()==False):
   valid=False
if(email.count('@')!=1 or email.count('.')<1):
   valid=False
elif(email[0]=='@' or email[len(email)-1]=="@"):
   valid=False
elif(email[len(email)-4:]!=".edu"):
   valid=False
if(len(password)<8):
   valid=False
elif(password[0]<'A'or password[0]>'Z'):
   valid=False
elif(password.count('0')+password.count('1')+password.count('2')+password.count('3')+password.count('4')+password.count('5')+password.count('6')+password.count('7')+password.count('8')+password.count('9')<1):
   valid=False
if(referral[:3]!="REF"):
   valid=False
elif(len(referral)!=6):
   valid=False
elif(referral[3:5].isdigit()==False):
   valid=False
elif(referral[5]!="@"):
   valid=False
if(valid):
   print("APPROVED")
else:
   print("REJECTED")
