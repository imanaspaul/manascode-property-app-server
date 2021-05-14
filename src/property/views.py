from property.utils import PaginationClass
from .serializers import CategorySerializer, CreatePropertySerializer, GetPropertySerializer, PropertyTypeSerializer
from . models import Category, Property, PropertyType
from rest_framework.generics import CreateAPIView, ListAPIView


# List all categories
class GetAllCategories(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# List all property type
class GetAllPropertyType(ListAPIView):

    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer



# List all property
class GetAllProperty(ListAPIView):

    queryset = Property.objects.all()
    serializer_class = GetPropertySerializer
    pagination_class = PaginationClass


class CreatProperty(CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = CreatePropertySerializer