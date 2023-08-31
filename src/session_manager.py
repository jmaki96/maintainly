"""There's probably a cleaner way to do this, but I want a single location that manages session state so we don't end up in a mess."""
from typing import Union

from flask import session

from src.models.user import User


class SessionManager:
    """A static class for managing flask session state."""

    @classmethod
    def log_in(cls, user: User):
        """Sets the session state as logged in for the specified user. If a user is already logged in, it will quietly log them out."""

        session['loggedin'] = True
        session['user_id'] = user.id
    
    @classmethod
    def log_out(cls):
        """Logs out current session if logged in. Does nothing otherwise."""
        
        session['loggedin'] = False
        session['user_id'] = None

    @classmethod
    def get_logged_in_user_id(cls) -> Union[int, None]:
        """ Gets logged in user if available. Returns None otherwise."""

        return session.get('user_id')

    @classmethod
    def is_logged_in(cls) -> bool:
        """Check if a user is logged in (any user)"""

        return session.get('loggedin', False)
