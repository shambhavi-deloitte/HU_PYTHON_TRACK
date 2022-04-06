file=open("C:\\Users\\shampriya\\Desktop\\a.txt","r+")
data=file.read()
splitted_data = data.split()
m=0
for d in splitted_data:
	m=max(m,len(d))
print(m)
