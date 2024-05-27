from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ecomProject.models import Product, DairyProduct
from ecomProject.serializers import ProductSerializer, DairyProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateProductAPIView(APIView):
    def get(self, request):
        # products = Product.objects.all().filter(price__range=(60.00, 100.00))
        products = Product.objects.all()
        # products = Product.objects.raw('SELECT * FROM ecomProject_product WHERE price BETWEEN 60.00 AND 100.00')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DairyListCreateAPIView(ListCreateAPIView):
    queryset = DairyProduct.objects.all()
    serializer_class = DairyProductSerializer


class DairyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DairyProduct.objects.all()
    serializer_class = DairyProductSerializer
