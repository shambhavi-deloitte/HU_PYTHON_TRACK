n=int(input())
k=n-1
for i in range(0,n):
	for j in range(0,k):
		print(end=' ')
	k-=1
	for j in range(0,i+1):
		print("* ",end='')
	print()
k=1
for i in range(n-2,-1,-1):
	for j in range(0,k):
		print(end=' ')
	k+=1
	for j in range(0,i+1):
		print("* ",end='')
	print()