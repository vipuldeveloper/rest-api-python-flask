import functools

user = {"user_name": "Vipul", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if(user['access_level'] == 'admin'):
            return func(*args, **kwargs)
        else:
            return f"No admin permission for {user['user_name']}"

    return secure_function

@make_secure
def get_password(panel):
    if panel == 'admin':
        return "1234"
    elif panel == 'super_admin':
        return "q2123121231@sAS"

#print(get_admin_password())
print(get_password("super_admin"))