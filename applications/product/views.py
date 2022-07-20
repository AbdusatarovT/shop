from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from applications.product.models import Category, Product
from applications.product.permissions import CustomIsAdmin
from applications.product.serializers import CategorySerializer, ProductSerializer


# class CategoryView(ViewSet):
#     def list(self, request):
#         queryset = Category.objects.all()
#         serializer = CategorySerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.seve()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


class LargeResultSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'parm_size'
    max_page_size = 10000




class CategoryView(ModelViewSet): # Весь CRUD
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LargeResultSetPagination
    permission_classes = [CustomIsAdmin]

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]# для фльтрации по категориям
    filterset_fields = ['category', 'owner'] #  фильтрация по полям
    ordering_fields = ['name', 'id'] # Сортировка
    search_fields = ['name', 'descriptions'] # для поиска по имени




    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_queryset(self): # отвечает за отображение информации
    #     queryset = super().get_queryset()
    #     filter_category = self.request.query_params.get('category')
    #     if filter_category:
    #         queryset = queryset.filter(category=filter_category)
    #     return queryset
