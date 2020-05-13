# Orignal Solution

# queryCount = int(input())
# hashmap = {}
# for i in range(queryCount):
#     numOfModels = int(input())
#     query = input().split(' ')
#     models = [int(x) for x in query]
#     maxModels = -1
#     for i in range(numOfModels):
#         if(i==0):
#             current = models[i]
#             # As single model is also a beautiful model
#             count = 1
#             for j in range(i+1,numOfModels):
#                 if( models[j] % current == 0 and models[j] > current):
#                     current = models[j]
#                     count+=1
#             if( count > maxModels ):
#                 maxModels = count
 #   print(maxModels)
    
# DP Solution

for _ in range(int(input())):
    n=int(input())
    dp=[1]*(n+1)
    l=list(map(int,input().split()))
    for i in range(1,n+1):
        j=2*i
        while j<=n:
            if l[j-1]>l[i-1]:
                dp[j]=max(dp[j],1+dp[i])
            j+=i
    print(max(dp))

