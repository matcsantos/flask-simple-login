
import string
import database
from hashlib import sha256
from sqlite3 import Row, IntegrityError
from classes.errors import ValidationError

CHARACTERS = string.ascii_letters + string.digits
USERNAME_MIN_LEN = 4
PASSWORD_MIN_LEN = 8

class User:
    
    def __init__(self, username:str, password:str):
        
        self.username = username
        self.password = password

        self.validate_username()
        self.validate_password()


    def validate_username(self):
        
        if not len(self.username) >= USERNAME_MIN_LEN:
            raise ValidationError(f'Usename must have at least {USERNAME_MIN_LEN} characters.')

        for char in self.username:
            if not char in CHARACTERS:
                raise ValidationError(f'Username cant contain special characters.')
    

    def validate_password(self):
        
        if not len(self.password) >= PASSWORD_MIN_LEN:
            raise ValidationError(f'Password must have at least {PASSWORD_MIN_LEN} characters.')
        
        for char in self.password:
            if not char in string.printable:
                raise ValidationError(f'Invalid character {char} in password.')


    def register(self):
        
        try:
            
            cursor = database.connect().execute(
                '''
                INSERT INTO users(username, password)
                VALUES (?, ?)
                ''',
                (self.username, User.encrypt_password(self.password))
            )
            
            cursor.connection.commit()
            cursor.close()
            return True
        
        except IntegrityError:
            return False


    def encrypt_password(password:str):
        return sha256(password.encode('UTF-8')).hexdigest()


    def serialize(row:Row):
        return User(
            username=row['username'],
            password=row['password']
        )


    def get_user(username:str):
        
        cursor = database.connect(factory=Row).execute(
            '''
            SELECT * FROM users WHERE username = ?
            ''',
            (username,)
        )
        
        user = cursor.fetchone()
        cursor.close()
        
        return User.serialize(user) if user else None


    def validate_login(username:str, password:str):
        
        if not len(username) or not len(password):
            return False

        user = User.get_user(username)

        if user and user.password == User.encrypt_password(password):
            return True
        
        else: return False
