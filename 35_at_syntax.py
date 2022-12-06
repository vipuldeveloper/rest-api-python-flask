# Modify original function without modifying original one
import functools

user = {"user_name": "Vipul", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if(user['access_level'] == 'admin'):
            return func()
        else:
            return f"No admin permission for {user['user_name']}"

    return secure_function

@make_secure
def get_admin_password():
    return "1234"


#print(get_admin_password())
print(get_admin_password.__name__)