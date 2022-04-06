#Q1
arr=[1,8,7,1,0,5,0,4,8,4,0,3]
for i in list(set(arr)):
	if arr.count(i)>1:
		print(i,'->',arr.count(i))


#Q2
list1=["Hello","take"]
list2=["Dear","Sir"]
res=list1+list2
print(res)

#Q3
list1=['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']
list1[2][1][2]+=['h','i','j']
print(list1)

#Q4
keys=['Ten','Twenty','Thirty']
value=[10,20,30]
res={}
for i in range(3):
	res[keys[i]]=value[i]
print(res)

#Q5
dict1={'Ten':10,'Twenty':20,'Thirty':30}
dict2={'Thirty':30,'Fourty':40,'Fifty':50}
dict1.update(dict2)
print(dict1)

#Q6
sampleDict={
	'name':'Kelly','age':25,'salary':8000,'city':'New york'
}
sampleDict['location']=sampleDict.pop('city')
print(sampleDict)

#Q7
dictt={'HuEx':[1,3,4],'is':[7,6],'best':[4,5]}
res=[]
for e in dictt:
	res.append([e]+dictt[e])
print(res)