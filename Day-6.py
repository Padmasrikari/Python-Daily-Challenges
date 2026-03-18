transaction_amounts=[]
n=int(input("Enter no.of transactions:"))
for i in range(n):
    t=int(input("Enter amount:"))
    transaction_amounts.append(t)
categories={
    "invalid":[],
    "normal":[],
    "large":[],
    "high_Risk":[]
    }
for t in transaction_amounts:
    if(t<=0):
        categories["invalid"].append(t)
    elif(t<=500):
        categories["normal"].append(t)
    elif(t<=2000):
        categories["large"].append(t)
    else:
        categories["high_Risk"].append(t)
valid=[t for t in transaction_amounts if t>0]
frequency=len(valid)
sum=0
for t in valid:
    sum+=t
freq_transaction=False
if(frequency>5):
    freq_transaction=True
large_spending=False
if(sum>5000):
    large_spending=True
sus_transaction=False
if(len(categories["high_Risk"])>=3):
    sus_transaction=True
if(freq_transaction and sus_transaction):
    risk="High"
elif(freq_transaction):
    risk="Moderate"
else:
    risk="Low"
summary=(frequency,sum)
print("Summary(tuple):",summary)
print("Valid:",valid)
print("Invalid:",categories["invalid"])
print("Normal:",categories["normal"])
print("Large:",categories["large"])
print("High Risk:",categories["high_Risk"])
print("Risk:",risk)
        
