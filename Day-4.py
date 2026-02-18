regno="AP24110011615"
d=int(regno[len(regno)-1])
n=int(input("Enter no.of activity scores:"))
act_scores=[]
for i in range(n):
    a=int(input("Enter activity score:"))
    act_scores=act_scores+[a]
low_risk=[]
med_risk=[]
high_risk=[]
criti_risk=[]
ignored_count=0
valid_count=0
for i in range(n):
    if(act_scores[i]<0):
        ignored_count+=1
    else:
        valid_count+=1
        if(act_scores[i]<=30):
            low_risk=low_risk+[act_scores[i]]
        elif(act_scores[i]<=60):
            med_risk=med_risk+[act_scores[i]]
        elif(act_scores[i]<=100):
            high_risk=high_risk+[act_scores[i]]
        else:
            criti_risk=criti_risk+[act_scores[i]]
print("Input scores:",act_scores)
print("Low Risk:",low_risk)
print("Medium Risk:",med_risk)
print("High Risk:",high_risk)
print("Critical Risk:",criti_risk)
removed=0
print("Registration Number (d):",d)
print("After Personalized Filtering:")
removed=len(criti_risk)
criti_risk=[]
print("Low Risk:",low_risk)
print("Medium Risk:",med_risk)
print("High Risk:",high_risk)
print("Critical Risk:",criti_risk)
print("Total Valid Entries:",valid_count)
print("Ignored Entries:",ignored_count)
print("Removed due to personalization:",removed)