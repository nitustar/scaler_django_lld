from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response


class UserListCreateView(APIView):

    def get(self, request):
        user = User.objects.all()
        serialized_user = UserSerializer(user, many=True)
        return Response(serialized_user.data)

    def post(self, request):
        user = User.objects.all()
        serialised_user = UserSerializer(data=request.data)
        if serialised_user.is_valid():
            serialised_user.save()
            return Response(serialised_user.data)
        return Response(serialised_user.errors)
