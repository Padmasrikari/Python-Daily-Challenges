regno="AP24110011615"
name="Padmasrikari"
l=len(name)
PLI=l%3
n=int(input("Enter number of resource requests:"))
req=[]
total_valid=0
low_demand=[]
moderate_demand=[]
high_demand=[]
invalid_requests=[]
for i in range(n):
    v=int(input("Enter the resource request value:"))
    req+=[v]
print(req)
for r in req:
    if(r<0):
        print(r,"->Invalid request")
        invalid_requests+=[r]
    else:
        total_valid+=1
        if(r==0):
           print(r,"->No demand")
        elif(r<=20):
            print(r,"->Low demand")
            low_demand+=[r]
        elif(r<=50):
            print(r,"->Moderate demand")
            moderate_demand+=[r]
        elif(r>50):
            print(r,"->High demand")
            high_demand+=[r]
print("Low Demand:",low_demand)
print("Moderate Demand",moderate_demand)
print("High Demand:",high_demand)
print("Invalid requests:",invalid_requests)
print("Number of valid requests:",total_valid)
print("Name:",name,"Length:",l)
print("Personalized Rule(PLI):",PLI)
if(PLI==0):
    print("Applied Rule:A->Low demand requests are removed")
    l=len(low_demand)
    low_demand=[]
    print("Low Demand:",low_demand)
    print("Moderate Demand",moderate_demand)
    print("High Demand:",high_demand)
    print("Invalid requests:",invalid_requests)
    print("Removed due to personalization:",l)
elif(PLI==1):
    print("Applied Rule:B->High demand requests are removed")
    l=len(high_demand)
    high_demand=[]
    print("Low Demand:",low_demand)
    print("Moderate Demand",moderate_demand)
    print("High Demand:",high_demand)
    print("Invalid requests:",invalid_requests)
    print("Removed due to personalization:",l)
else:
    print("Applied Rule:C->Kept only Moderate demand requests")
    l=len(low_demand)+len(high_demand)+len(invalid_requests)
    low_demand=[]
    high_demand=[]
    invalid_requests=[]
    print("Low Demand:",low_demand)
    print("Moderate_demand",moderate_demand)
    print("High Demand:",high_demand)
    print("Invalid requests:",invalid_requests)
