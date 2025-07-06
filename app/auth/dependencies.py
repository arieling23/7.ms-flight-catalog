from fastapi import Request, HTTPException
from app.auth.jwt import verify_token
from jwt import PyJWTError
from app.logger import logger

def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        logger.warning("❌ Solicitud sin token JWT")
        raise HTTPException(status_code=403, detail="Token faltante")

    token = auth_header.split(" ")[1]
    try:
        payload = verify_token(token)
        logger.info(f"🔐 Usuario autenticado: {payload['email']} - Rol: {payload['role']}")
        return payload
    except PyJWTError:
        logger.error("❌ Token JWT inválido")
        raise HTTPException(status_code=403, detail="Token inválido")