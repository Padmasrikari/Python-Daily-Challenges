r=int(input("Enter last 2 digits of your roll number:"))
s=0
while(r!=0):
    s+=r%10
    r=r//10
n=int(input("Enter number of students:"))
marks=[]
for i in range(n):
    m=int(input("Enter marks:"))
    marks=marks+[m]
valid_count=0
fail_count=0
for i in range(n):
    mark=marks[i]
    cat=""
    if(mark<0 or mark>100):
        cat="Invalid"
    else:
        valid_count+=1
        if(mark>=90):
            cat="Excellent"
        elif(mark>=75):
            cat="Very Good"
        elif(mark>=60):
            cat="Good"
        elif(mark>=40):
            cat="Average"
        else:
            cat="Fail"
            fail_count+=1
    print(mark,"->",cat)
    if(marks[i]+s<=100):
        marks[i]+=s
print("Total Valid students:",valid_count)
print("Total Failed students:",fail_count)
print(marks)
