query = input()
mx = query[0]
for i in range(len(query)):
    mx = max(mx, query[i]) 
result = ''
for i in range(len(query)):
    if mx == query[i]:
        result = result + query[i]
print(result)