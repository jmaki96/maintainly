from sqlalchemy.ext.hybrid import hybrid_property

from src.extensions.database import db
from src.extensions.bcrypt import bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(320))
    _password = db.Column(db.String(128))

    @hybrid_property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def _set_password(self, plaintext: str):
        self._password = bcrypt.generate_password_hash(plaintext)

    def authenticate(self, plaintext_password: str) -> bool:
        """Authenticates user supplied password.

        Args:
            plaintext_password (str): Plaintext password provided by the user. Never print or store this.

        Returns:
            bool: True if the password is correct for this user.
        """

        return bcrypt.check_password_hash(self.password, plaintext_password)