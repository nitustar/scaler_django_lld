from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import UserSerializer, ShippingAddressSerializer, CreateShippingAddressSerializer
from .models import User, ShippingAddress


class UserListCreateAPIView(APIView):

    def get(self, request):
        users = User.objects.all().prefetch_related('shipping_address').select_related('default_shipping_address')
        return Response(UserSerializer(users, many=True).data)

    def post(self, request):
        serialized = UserSerializer(data=self.request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=400)
        serialized.save()
        return Response(serialized.data, status=201)


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShippingAddressListCreateAPIView(GenericAPIView):
    serializer_class = CreateShippingAddressSerializer

    def post(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        serialized = CreateShippingAddressSerializer(data=self.request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=400)
        shipping_address = ShippingAddress(
            city=serialized.validated_data['city'],
            street=serialized.validated_data['street'],
            state=serialized.validated_data['state'],
            zip_code=serialized.validated_data['zip_code'],
            country=serialized.validated_data['country'], user=user
        )
        shipping_address.save()
        return Response(ShippingAddressSerializer(shipping_address).data, status=201)


class SetDefaultShippingAddress(APIView):

    def patch(self, request, user_id, address_id):

        user = get_object_or_404(User, pk=user_id)
        address = get_object_or_404(ShippingAddress, user_id=user_id, pk=address_id)
        user.default_shipping_address = address
        user.save()
        return Response(
            UserSerializer(User), 200
        )

