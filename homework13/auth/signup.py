def signup():
    print('true')
    users_list = []
    users = []
    users_attributes = []
    with open(r'C:\Users\Professional\PycharmProjects\homework6.py\homework13\auth\users.txt',) as file:
        for key,value in enumerate(file):
            if key == 0:
                users_attributes = (str(value).strip().split(','))
            else:
                users_list.append(str(value).strip().split(','))
        for elem in users_list:
            users.append(dict(zip(users_attributes,elem)))
    email = input('email')
    password = input('password')
    name = input('first name')
    last_name = input('last name')
    for user in users:
        if user['email'] == email:
            raise Exception('User already exist')

    with open(r'C:\Users\Professional\PycharmProjects\homework6.py\homework13\auth\users.txt','a') as file:
        file.write('\n')
        file.write(f"""{email},{password},{name},{last_name}""")

def name():
    print("Grigor Manukyan")