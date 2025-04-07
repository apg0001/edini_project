from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# 간단한 토큰 인증 예제 (실제 구현 시 DB 연동 필요)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/admin/login")

FAKE_ADMIN_TOKEN = "admin-secret-token"

def get_current_admin(token: str = Depends(oauth2_scheme)):
    if token != FAKE_ADMIN_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid admin token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"role": "admin"}