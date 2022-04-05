n=int(input())
k=n-1
for j in range(0,k):
	print(end=' ')
print('*')
k-=1
for i in range(1,n-1):
	for j in range(0,k):
		print(end=' ')
	k-=1
	print('* ',end='')
	for j in range(1,i):
		print("  ",end='')
	print('* ',end='')
	print()
for i in range(2*n-1):
	print('*',end='')