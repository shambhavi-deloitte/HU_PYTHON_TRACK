arr=input().split()
temp=list(map(lambda w:[w.count('a'),w.count('A')],arr))
print(temp)
