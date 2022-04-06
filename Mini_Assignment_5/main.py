arr=[-1000,500,-600,700,5000,-9000,-17500]
res=map(lambda i:abs(i),list(filter(lambda i:i<0,arr)))
print(list(res))

import functools
lis=[1,2,3,4]
res=functools.reduce(lambda a, b:a*b, lis)
print(res)

lst1=['Netflix','Hulu','Sling','Hbo']
lst2=[198,166,237,125]
res=dict(zip(lst1,lst2))
print(res)