n=int(input())    #get the input
fact=1
i=1
if(n==0):
    fact=1
for i in range(1,n+1):
    fact=fact*i #formula
print(fact)
