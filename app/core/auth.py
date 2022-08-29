from core.config import settings
from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from models.user import User
from starlette.status import HTTP_403_FORBIDDEN

access_token_header = APIKeyHeader(name="access_token", auto_error=False)

async def get_current_user(access_token: str = Security(access_token_header)):
    if access_token == settings.API_KEY:
        return User(
            id = 1,
            username = "Regular user",
            email = "user@mail.com",
            is_active = True,
            is_admin = False
        )
    elif access_token == settings.API_KEY_ADMIN:
        return User(
            id = 2,
            username = "Admin user",
            email = "admin@mail.com",
            is_active = True,
            is_admin = True
        )
    else:
        raise HTTPException(
            status_code = HTTP_403_FORBIDDEN,
            detail = "Invalid API KEY"
        )
