#!/usr/bin/env python3
""""Define a class auth
"""


from flask import request
from typing import List, TypeVar


class Auth():
    """ defines authentication system
    """
    
    #def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        

    def authorization_header(self, request=None) -> str:
        """"Handles authentication request
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        return header if header else None
    
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Handles authentication users
        """
        if request is None:
            return None