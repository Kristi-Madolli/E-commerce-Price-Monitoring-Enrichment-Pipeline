import os
from cryptography.fernet import Fernet, InvalidToken
from dotenv import load_dotenv

load_dotenv()


def generate_key() -> str:
    """Generate a new Fernet key."""
    return Fernet.generate_key().decode("utf-8")


def _write_env_key(key: str) -> None:
    if not os.path.exists(".env"):
        with open(".env", "w", encoding="utf-8") as f:
            f.write(f"FERNET_KEY={key}\n")


def _get_fernet() -> Fernet:
    key = os.getenv("FERNET_KEY")
    if not key:
        key = Fernet.generate_key().decode("utf-8")
        _write_env_key(key)
        os.environ["FERNET_KEY"] = key
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
