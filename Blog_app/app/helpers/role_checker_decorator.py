from functools import wraps
from flask_login import current_user
from flask import abort


def has_role(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.has_role(f"{role}"):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
