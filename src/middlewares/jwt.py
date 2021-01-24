import datetime

import jwt
from django.conf import settings
from rest_framework.response import Response


def generate_token(user):
    payload = {
        'id': str(user.id),
        'email': user.email,
        'name': user.name,
        'phone': user.phone,
        'is_superuser': user.is_superuser,
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }
    token = jwt.encode(payload, settings.SECRET_KEY)

    payloadRefreshToken = {
        'id': str(user.id),
        'email': user.email,
        'name': user.name,
        'phone': user.phone,
        'is_superuser': user.is_superuser,
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)
    }
    refreshToken = jwt.encode(payloadRefreshToken, settings.REFRESH_JWT_SECRET)
    user_data = {
        'id': user.id,
        'name': user.name,
        'phone': user.phone,
        'email': user.email,
        'is_superuser': user.is_superuser,
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)
    }
    return Response({
        'user': user_data,
        'token': token,
        'refreshToken': refreshToken
    })
