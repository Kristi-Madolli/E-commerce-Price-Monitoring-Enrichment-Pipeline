import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

def _write_env_key(key: str) -> None:
    # creates .env in project root if missing
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
