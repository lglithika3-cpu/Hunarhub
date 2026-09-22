from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError

password_hasher = PasswordHasher()

def hash_password(password):
    return password_hasher.hash(password)

def verify_password(password, password_hash):
    try:
        password_hasher.verify(password_hash, password)
        return True
    except (VerifyMismatchError, VerificationError):
        return False