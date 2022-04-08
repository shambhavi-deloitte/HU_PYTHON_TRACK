import csv

movie_timings_seats={}

def calculating_timings(ip_title):
	data=single_movie_info[ip_title];all_timings=[]
	length=data[1];nos=data[7];fs=data[8];it=data[9];gap=data[10]
	time_split=length.split()
	h=time_split[0].split('hr')[0];m=time_split[1].split('mins')[0]
	total_minutes=int(m)+int(h)*60
	if 'AM' in fs:
		fs_split=fs.split('AM')
		if ':' in fs_split[0]:
			fs_h=int(fs_split[0].split(':')[0])
			fs_m=int(fs_split[0].split(':')[1])
	else:
		fs_split=fs.split('PM')
		if ':' in fs_split[0]:
			fs_h=int(fs_split[0].split(':')[0])
			fs_m=int(fs_split[0].split(':')[1])
	total_delay_time=0
	total_delay_time+=int(it.split('mins')[0])
	total_delay_time+=int(gap.split('mins')[0])
	total_delay_time+=total_minutes
	temp=total_delay_time
	all_timings.append([fs_h,fs_m])
	for i in range(int(nos)-1):
		total_delay_time=temp
		while total_delay_time>60:
			if fs_h==11:
				fs_h=0
			else:
				fs_h+=1
			total_delay_time-=60
		fs_m+=total_delay_time
		if fs_m>60:
			if fs_h==11:
				fs_h=0
			else:
				fs_h+=1
			fs_m-=60
		all_timings.append([fs_h,fs_m])
	return all_timings

info_names=['Genre','Length','Cast','Director','Admin Rating','Language','Timings',
	'Number of Shows in a day','First Show','Interval Time','Gap Between Shows','Capacity']

u_fields=['USERNAME','EMAIL','PHONE','AGE','PASSWORD']
users_data=[];uname_pass={'admin':'admin'}
file_name="C:\\Users\\shampriya\\Desktop\\user_data.csv"
with open(file_name,'r') as csvfile:
	csvreader=csv.reader(csvfile)
	next(csvreader)
	for row in csvreader:
		if row!=[]:
			users_data.append(row)
			uname_pass[row[0]]=row[4]


movies_info_names=['Title','Genre','Length','Cast','Director','Admin Rating','Language','Timings',
	'Number of Shows in a day','First Show','Interval Time','Gap Between Shows','Capacity']
all_movies_info=[]
single_movie_info={}
file_name="C:\\Users\\shampriya\\Desktop\\movies_data.csv"
with open(file_name,'r') as csvfile:
	csvreader=csv.reader(csvfile)
	fields=next(csvreader)
	for row in csvreader:
		try:
			if row[0]!='' and row!=[]:
				all_movies_info.append(row)
				single_movie_info[row[0]]=row[1:]
				if len(row)==14:
					movie_timings_seats[row[0]]=[calculating_timings(row[0]),int(row[12]),row[13]]
				else:
					movie_timings_seats[row[0]]=[calculating_timings(row[0]),int(row[12]),'']
		except:
			continue

def update_user_info():
	file_name="C:\\Users\\shampriya\\Desktop\\user_data.csv"
	with open(file_name,'w') as csvfile:
		csvwriter=csv.writer(csvfile)
		csvwriter.writerow(u_fields)
		csvwriter.writerows(users_data)

def update_movies_data():
	file_name="C:\\Users\\shampriya\\Desktop\\movies_data.csv"
	with open(file_name,'w') as csvfile:
		csvwriter=csv.writer(csvfile)
		csvwriter.writerow(movies_info_names)
		csvwriter.writerows(all_movies_info)

while True:
	print('\n\n1. Login\n2. Register new account\n3. Exit\n\n')
	choice1=int(input())
	if choice1==3:
		break
	elif choice1==1:
		uname=input('User: ')
		upass=input('Password: ')
		if (uname in uname_pass) and (uname_pass[uname]==upass):
			if uname=='admin':
				while True:
					print('\n1. Admin Login:\n******Welcome Admin******\n')
					print('1. Add New Movie Info\n2. Edit Movie Info')
					print('3. Delete Movies\n4. Logout')
					choice2=int(input())
					if choice2==4:
						break
					elif choice2==1:
						m_info=[]
						print('Add new Movie:\n')
						m_info.append(input('Title: '))
						if m_info[0] in single_movie_info:
							print('Invalid Movie!!!')
						else:
							for i in movies_info_names[1:]:
								m_info.append(input(i+': '))
							all_movies_info.append(m_info)
							single_movie_info[m_info[0]]=m_info[1:]
							update_movies_data()
							print('Movie Added ...')
					elif choice2==2:
						print('\nUpdate Movie:')
						ip_title=input('Title: ')
						if ip_title in single_movie_info:
							m_info=[];m_info.append(ip_title)
							for i in movies_info_names[1:]:
								m_info.append(input(i+': '))
							single_movie_info[ip_title]=m_info[1:]
							for i in range(len(all_movies_info)):
								if all_movies_info[i][0]==ip_title:
									all_movies_info[i]=m_info
							update_movies_data()
							print('Movie Updated ...')
						else:
							print('Invalid Title!!!')
					elif choice2==3:
						print('Delete Movie:\n')
						ip_title=input('Title: ')
						if ip_title in single_movie_info:
							for i in range(len(all_movies_info)):
								if all_movies_info[i][0]==ip_title:
									all_movies_info.pop(i)
							single_movie_info.pop(ip_title)
							update_movies_data()
							print('Movie Deleted ...')
						else:
							print('Invalid Title!!!')

			else:
				while True:
					print('\n******Welcome to BookMyShow******* \n')
					print('\n******Welcome '+uname+' ******\n')
					i=1
					for m in single_movie_info:
						print(str(i)+'.',m);i+=1
					print(str(i)+'. Logout')
					choice3=int(input('Enter movie: '))
					if choice3==i:
						break
					elif choice3<i:
						ip_title=list(single_movie_info.keys())[choice3-1]
						print(list(single_movie_info.keys()))
						print('\nTitle: ',ip_title)
						for i in range(0,5):
							print(info_names[i],': ',single_movie_info[ip_title][i])
						temp_t=''
						for i in movie_timings_seats[ip_title][0]:
							temp_t+='-'.join(map(str,i))+str(' ')
						print('Timings: ',temp_t)
						if movie_timings_seats[ip_title][2]!='':
							print('User Rating:',movie_timings_seats[ip_title][2])
						print('1. Book Tickets')
						print('2. Cancel Tickets')
						print('3. Give User Rating')
						choice4=int(input())
						if choice4==1:
							fetched_timings=movie_timings_seats[ip_title][0]
							for i in range(len(fetched_timings)):
								print(str(i+1)+'. '+'-'.join(map(str,fetched_timings[i])))
							remaining_seats=movie_timings_seats[ip_title][1]
							choice5=int(input('Select Timings: '))
							print('Timing: ','-'.join(map(str,fetched_timings[choice5-1])))
							print('Remaining Seats: ',remaining_seats)
							choice6=int(input('Enter Number of seats: '))
							if choice6<=remaining_seats:
								remaining_seats-=choice6
								print('Thanks for booking.')
								movie_timings_seats[ip_title][1]=remaining_seats
								single_movie_info[ip_title][-1]=remaining_seats
								for i in all_movies_info:
									if i[0]==ip_title:
										i[12]=remaining_seats
								update_movies_data()
							else:
								print(choice6,' seats are not available!!!')

						elif choice4==2:
							num_of_ctickets=int(input('Number of seats you want to cancel: '))
							movie_timings_seats[ip_title][1]+=num_of_ctickets
							single_movie_info[ip_title][-1]+=num_of_ctickets
							for i in all_movies_info:
								if i[0]==ip_title:
									i[12]+=num_of_ctickets
							update_movies_data()

						elif choice4==3:
							print('Please enter rating for the',ip_title,'movie: ')
							rating=int(input())
							movie_timings_seats[ip_title][2]=rating
							for i in all_movies_info:
								if i[0]==ip_title:
									if len(i)==13:
										i+=[rating]
									else:
										i[13]=rating
							update_movies_data()
		else:
			print('Invalid Credintials !!!')
	elif choice1==2:
		name=input('Name:')
		email=input('Email:')
		phone=int(input('Phone:'))
		age=int(input('Age:'))
		password=input('Password:')
		if name in uname_pass:
			print('Error')
		else:
			users_data.append([name,email,phone,age,password])
			uname_pass[name]=password
			update_user_info()