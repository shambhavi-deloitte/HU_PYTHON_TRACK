def fibonnaci(n):
	f,s=0,1
	while f<n:
		yield f
		f,s=s,f+s
n=5
gObj=fibonnaci(n)
for i in range(n):
	print(gObj.__next__())
