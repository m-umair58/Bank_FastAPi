from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

SECRET_KEY = "17b4ae5cbe59bf75d1a74dd7b5ec5d3f562606f492856b6eaf59e46916707765"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_TIME = 30

bearer_scheme = HTTPBearer()

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# The corrected function to decode the token and extract user info
async def get_user_info(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
    token = credentials.credentials  # Extract the token string
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        accid: str = payload.get("acc_id")
        userid: int = payload.get("user_id")
        
        if accid is None or userid is None:
            raise HTTPException(status_code=401, detail="Unauthorized User")
        
        return {"acc_id": accid, "id": userid}
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate user")
