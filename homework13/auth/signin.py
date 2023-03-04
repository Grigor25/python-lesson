def signin():
    users_list = []
    users = []
    users_attributes = []
    with open(r'C:\Users\Professional\PycharmProjects\homework6.py\homework13\auth\users.txt') as file:
        for key,value in enumerate(file):
            if key == 0:
                users_attributes = (str(value).strip().split(','))
            else:
                users_list.append(str(value).strip().split(','))
        for elem in users_list:
            users.append(dict(zip(users_attributes,elem)))
    email = input('email')
    password = input('password')
    for user in users:
        if user['email'] == email and user['password'] == password:
            first_name,last_name = user['first_name'],user['last_name']
            print(f"""Hello {first_name} {last_name}""")
            break
    else:
       raise Exception('Inavlid email or password')
