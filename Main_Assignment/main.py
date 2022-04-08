import csv

info_names = ['Genre', 'Length', 'Cast', 'Director', 'Admin Rating', 'Language', 'Timings',
              'Number of Shows in a day', 'First Show', 'Interval Time', 'Gap Between Shows', 'Capacity']
movies_data = {}
u_fields = ['USERNAME', 'EMAIL', 'PHONE', 'AGE', 'PASSWORD']
users_data = [];
uname_pass = {'admin': 'admin'}
file_name = "C:\\Users\\shampriya\\Desktop\\user_data.csv"
with open(file_name, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        if row != []:
            users_data.append(row)
            uname_pass[row[0]] = row[4]


def update_user_info():
    file_name = "C:\\Users\\shampriya\\Desktop\\user_data.csv"
    with open(file_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(u_fields)
        csvwriter.writerows(users_data)


while True:
    print('1. Login\n2. Register new account\n3. Exit')
    choice1 = int(input())
    if choice1 == 3:
        break
    elif choice1 == 1:
        print('1. Login\n')
        uname = input('User: ')
        upass = input('Password: ')
        if (uname in uname_pass) and (uname_pass[uname] == upass):
            if uname == 'admin':
                while True:
                    print('1. Admin Login:\n******Welcome Admin******\n')
                    print('1. Add New Movie Info\n2. Edit Movie Info')
                    print('3. Delete Movies\n4. Logout')
                    choice2 = int(input())
                    if choice2 == 4:
                        break
                    else:
                        if choice2 == 1:
                            m_info = {}
                            print('Add new Movie:\n')
                            title = input('Title: ')
                            for i in info_names:
                                m_info[i] = input(i + ': ')
                            movies_data[title:m_info]
                        elif choice2 == 2:
                            print('Enter Title:\n')

            else:
                while True:
                    print('2. User Login:\n')
                    print('******Welcome ' + uname + ' ******\n')
                    i = 1
                    for m in movies_data:
                        print(str(i) + '.', m);
                        i += 1
                    print(str(i) + '. Logout')
                    choice3 = int(input(''))
                    if choice3 == i:
                        break
                    else:
                        print(choice3, 'movie')
        else:
            print('Invalid Credintials !!!')
    elif choice1 == 2:
        name = input('Name:')
        email = input('Email:')
        phone = int(input('Phone:'))
        age = int(input('Age:'))
        password = input('Password:')
        if name in uname_pass:
            print('Error')
        else:
            users_data.append([name, email, phone, age, password])
            uname_pass[name] = password
            update_user_info()
