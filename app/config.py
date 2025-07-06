import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", 8082))
DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
