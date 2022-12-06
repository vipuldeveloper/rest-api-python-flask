users = [
    (0, "vipul", "vi_password"),
    (1, "kavar", "ka_password"),
    (2, "vaibhav", "va_password"),
    (3, "Nikunj", "ni_password"),
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter the username: ")
user_password = input("Enter the password: ")

_, username, password = username_mapping[username_input]

if(user_password == password):
    print("authorised user")
else:
    print("Incorrect details and user")