from ninja import Schema
from pydantic import EmailStr


class LoginSerializer(Schema):

    username: str
    password: str




class UserCreateSerializer(Schema):

    username: str
    email: EmailStr
    password: str
    category: list[str]



class UserDetailSerializer(Schema):

    username: str
    email: EmailStr
    category: list[str]


class TokenSerializer(Schema):
    
    type: str
    refresh: str
    access: str
