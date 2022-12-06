# Modify original function without modifying original one

user = {"user_name": "Vipul", "access_level": "admin"}

def make_secure(func):
    def secure_function():
        if(user['access_level'] == 'admin'):
            return func()
        else:
            return f"No admin permission for {user['user_name']}"

    return secure_function


def get_admin_password():
    return "1234"


get_admin_password = make_secure(get_admin_password)
print(get_admin_password())