from functools import wraps
from flask import abort
from flask_login import current_user, login_required

def role_required(*roles):
    allowed_roles = [role.lower() for role in roles]

    def decorator(function):
        @wraps(function)
        @login_required
        def wrapper(*args, **kwargs):
            user_role = str(current_user.role).lower()

            if user_role not in allowed_roles:
                abort(403)

            return function(*args, **kwargs)

        return wrapper

    return decorator