import os
from cryptography.fernet import Fernet, InvalidToken
from dotenv import load_dotenv

load_dotenv()


def generate_key() -> str:
    return Fernet.generate_key().decode("utf-8")


def _get_fernet() -> Fernet:
    key = os.getenv("FERNET_KEY")
    if not key:
        raise RuntimeError("FERNET_KEY is missing. Create a .env file with FERNET_KEY=...")
    return Fernet(key.encode("utf-8"))


def encrypt_text(plain: str) -> str:
    f = _get_fernet()
    return f.encrypt(plain.encode("utf-8")).decode("utf-8")


def decrypt_text(token: str) -> str:
    f = _get_fernet()
    try:
        return f.decrypt(token.encode("utf-8")).decode("utf-8")
    except InvalidToken:
        raise ValueError("Invalid encryption token")
