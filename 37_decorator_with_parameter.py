import functools

user = {"user_name": "Vipul", "access_level": "superadmin"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if(user['access_level'] == access_level):
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permission for {user['user_name']}"

        return secure_function
    return decorator
    
@make_secure('admin')
def get_admin_password():
    return "1234"

@make_secure('superadmin')
def get_superadmin_password():
    return "1234@332112"

#print(get_admin_password())
print(get_admin_password())
print(get_superadmin_password())