from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from useraccount.models import Users
from useraccount.api.user.serializers import (
                                UserSerializer,
                                RegisterUserSerializer,

                        )


@api_view(['GET'])
def get_all_user(request):
    try:
        user = Users.objects.all()
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register_user(request):
    serializer = RegisterUserSerializer(data=request.data)

    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'Successfully User Created!!'
        data['name'] = user.name
        data['username'] = user.username
        data['email'] = user.email
        token = Token.objects.get(user=user).key
        data['token'] = token
    else:
        data = serializer.errors

    return Response(data)

