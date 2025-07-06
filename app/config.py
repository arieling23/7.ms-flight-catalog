import os
from dotenv import load_dotenv

load_dotenv()

def get_env_var(key: str, default=None, required=False):
    value = os.getenv(key, default)
    if required and value is None:
        raise ValueError(f"❌ Variable de entorno obligatoria no definida: {key}")
    return value

PORT = int(get_env_var("PORT", 8082))
DATABASE_URL = get_env_var("DATABASE_URL", required=True)
JWT_SECRET = get_env_var("JWT_SECRET", required=True)
JWT_ALGORITHM = get_env_var("JWT_ALGORITHM", "HS256")
