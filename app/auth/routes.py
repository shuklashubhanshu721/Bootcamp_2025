from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from app.infrastructure.database.mongo_client import db
from app.auth.models import User
from datetime import datetime

router = APIRouter(tags=["Authentication"])

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/register")
async def register_user(payload: RegisterRequest):
    """Register a new user with hashed password"""
    try:
        if db:
            existing_user = db["users"].find_one({"email": payload.email})
            if existing_user:
                raise HTTPException(status_code=400, detail="User already exists")
            hashed_pw = pwd_context.hash(payload.password)
            new_user = User(
                email=payload.email,
                hashed_password=hashed_pw,
                role="agent",
                status="active",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            result = db["users"].insert_one(new_user.dict(by_alias=True))
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content={
                    "message": "User registered successfully (db)",
                    "user_id": str(result.inserted_id),
                    "email": payload.email,
                    "storage": "database"
                },
            )
        else:
            # Fallback mock registration when DB isn't available
            hashed_pw = pwd_context.hash(payload.password)
            mock_user = {
                "email": payload.email,
                "hashed_password": hashed_pw,
                "role": "agent",
                "status": "active",
                "created_at": str(datetime.utcnow()),
                "storage": "in-memory"
            }
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content={
                    "message": "User registered successfully (mock)",
                    "user": mock_user
                },
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --- Added JWT login and protected routes implementation ---

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from fastapi import Depends
from datetime import timedelta

SECRET_KEY = "supersecretjwtkey"  # TODO: move to env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
   """Generate a JWT access token"""
   to_encode = data.copy()
   expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
   to_encode.update({"exp": expire})
   encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
   return encoded_jwt


class TokenResponse(BaseModel):
   access_token: str
   token_type: str = "bearer"


class LoginRequest(BaseModel):
   email: EmailStr
   password: str


@router.post("/login", response_model=TokenResponse)
async def login_user(payload: LoginRequest):
   """Verify credentials and issue JWT token"""
   user = db["users"].find_one({"email": payload.email})
   if not user:
       raise HTTPException(status_code=401, detail="Invalid credentials")
   if not pwd_context.verify(payload.password, user["hashed_password"]):
       raise HTTPException(status_code=401, detail="Invalid credentials")

   # update last_login_at
   db["users"].update_one({"_id": user["_id"]}, {"$set": {"last_login_at": datetime.utcnow()}})
   token_data = {"sub": payload.email, "role": user.get("role", "agent")}
   access_token = create_access_token(data=token_data)
   return TokenResponse(access_token=access_token)


async def get_current_user(token: str = Depends(oauth2_scheme)):
   """Validate JWT and return current user"""
   credentials_exception = HTTPException(
       status_code=401,
       detail="Could not validate credentials",
       headers={"WWW-Authenticate": "Bearer"},
   )
   try:
       payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
       email: str = payload.get("sub")
       if email is None:
           raise credentials_exception
   except JWTError:
       raise credentials_exception

   user = db["users"].find_one({"email": email})
   if user is None:
       raise credentials_exception
   return User(**user)


@router.get("/users/me")
async def read_current_user(current_user: User = Depends(get_current_user)):
   """Protected route returning current user info"""
   return {"email": current_user.email, "role": current_user.role, "status": current_user.status}


@router.get("/status")
def auth_status():
   return {"module": "AuthModule", "status": "active", "jwt_enabled": True}