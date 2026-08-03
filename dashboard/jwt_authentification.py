from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .models import AnonymousAccount


class AnonymousAccountJWTAuthentication(JWTAuthentication):

    def get_user(self, validated_token):
        username = validated_token.get("username")

        if not username:
            raise AuthenticationFailed(
                "Token does not contain an anonymous username."
            )

        try:
            account = AnonymousAccount.objects.get(
                username=username
            )
        except AnonymousAccount.DoesNotExist:
            raise AuthenticationFailed(
                "Anonymous account no longer exists."
            )

        return account