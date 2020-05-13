# Orignal Solution

def smallestDivisor(n):
    # if divisible by 2 
    if (n % 2 == 0): 
        return 2; 
  
    # iterate from 3 to sqrt(n) 
    i = 3;  
    while(i * i <= n): 
        if (n % i == 0): 
            return i; 
        i += 2; 
  
    return n;

queryCount = int(input())
hashmap = {}
for i in range(queryCount):
    query = input().split(' ')
    n = int(query[0])
    k = int(query[1])
    fn = 0
    for i in range(k):
        if n in hashmap:
            fn = hashmap[n]
        else:
            fn = smallestDivisor(n)
            hashmap[n] = fn
        n = n + fn
    print(n)
    
    


# Optmized Solution
# After finding first smallest divisor, n will be n+smallest divisor, and thus for succeeding numbers
# the smallest divisor remains the same, thus we just add twice of the  
t=int(input())
for i in range(t):
	n,k=map(int,input().split())
	ans=0
	for i in range(2,n+1):
		if(n%i==0):
			ans=i
			break;
	print(n+ans+(k-1)*2)