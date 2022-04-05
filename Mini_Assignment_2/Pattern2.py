n=int(input())
for i in range(n):
	print('* ',end='')
print()
k=2
for i in range(n-2):
	for j in range(k):
		print(' ',end='')
	k+=2
	print('* ',end='')
	for j in range((n*2)-k-2):
		print(' ',end='')
	print('*')
for j in range(k):
	print(' ',end='')
print('*')