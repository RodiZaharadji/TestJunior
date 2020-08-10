from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.serializers import RegisterSerializer
from drf_util.decorators import serialize_decorator


class RegisterUserView(GenericAPIView):
    serializer_class = RegisterSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(RegisterSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return Response(RegisterSerializer(user).data)
