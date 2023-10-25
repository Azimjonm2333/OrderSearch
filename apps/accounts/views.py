from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja_jwt.tokens import RefreshToken
from .models import User
from apps.orders.models import Category
from .serializers import UserCreateSerializer, TokenSerializer
from utils.base.serializer import Error

from ninja.router import Router

from ninja_jwt.schema_control import SchemaControl
from ninja_jwt.settings import api_settings

schema = SchemaControl(api_settings)

router = Router()


@router.post("/register", response={200: TokenSerializer, 403: Error})
def register(request, user: UserCreateSerializer):
    try:
        User.objects.get(email=user.email)
        return 403, {"detail": "Email already in use"}
    except User.DoesNotExist:
        pass
    try:
        User.objects.get(username=user.username)
        return 403, {"detail": "Username already in use"}
    except User.DoesNotExist:
        pass
    new_user = User(username=user.username, email=user.email)
    categories = [
        get_object_or_404(Category, slug=x)
        for x in user.category
    ]
    new_user.set_password(user.password)
    new_user.save()
    new_user.category.set(categories)
    refresh = RefreshToken.for_user(new_user)
    
    response = {
        "type": "Bearer",
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return response


@router.post(
    "/login",
    response=schema.obtain_pair_schema.get_response_schema(),
    url_name="login",
    auth=None,
)
def obtain_token(request, user_token: schema.obtain_pair_schema):
    user_token.check_user_authentication_rule()
    return user_token.output_schema()


@router.post(
    "/refresh",
    response=schema.obtain_pair_refresh_schema.get_response_schema(),
    url_name="token_refresh",
    auth=None,
)
def refresh_token(request, refresh_token: schema.obtain_pair_refresh_schema):
    return refresh_token.to_response_schema()
