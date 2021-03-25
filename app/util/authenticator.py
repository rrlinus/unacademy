from flask import request, session
from functools import wraps
from flask_restx import abort

from ..models.user import User


class Authenticator:
    @staticmethod
    def authenticate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            headers = request.headers
            # Temporarily disabled token validation.
            if not headers.get('X-Api-Key') or not Authenticator.__verify_token(headers['X-Api-Key']):
                abort(401)
            return func(*args, **kwargs)

        return wrapper

    @staticmethod
    def __verify_token(token: str):
        '''
            This method will take a token and verify whether it is authenticated or not
        '''
        res = User.query.filter_by(token=token, active=True).first()
        if not res:
            return False
        session['root_uid'] = res.root_uid
        session['logged_in'] = True
        return True
