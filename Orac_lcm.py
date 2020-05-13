# Brute force

import math
def get_lcm(n1,n2):
  #find gcd
  gcd = math.gcd(n1,n2)
  
  #formula 
  result = (n1*n2)/gcd
  return result

def get_gcd(lcm_list):
    result = lcm_list[0]
    for i in range(2,len(lcm_list)):
        result = math.gcd(result,lcm_list[i])
    return result 
  
n = int(input())
query = input().split(' ')
elements = [int(x) for x in query]

lcm_list = []
for i in range(n):
    for j in range(i+1,n):
        lcm_list.append(int(get_lcm(elements[i],elements[j])))
print(get_gcd(lcm_list))

# Optimized

from math import *;

a=int(input());
b=list(map(int,input().split()))
l=(b[0]*b[1])//gcd(b[0],b[1])
g=gcd(b[0],b[1])
for i in b[2:]:
    g1=gcd(i,g)
    l=gcd(l,(i*g)//g1)
    g=g1
print(l)
