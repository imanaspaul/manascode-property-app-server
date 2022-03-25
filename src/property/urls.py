from django.urls import path
from .views import CreatProperty, GetAllCategories, GetAllProperty, GetAllPropertyType


urlpatterns = [
    path('all-categories/', GetAllCategories.as_view(), name='get-all-categories'),
    path('all-types/', GetAllPropertyType.as_view(), name='get-all-property-types'),
    path('all-property/', GetAllProperty.as_view(), name='get-all-property'),
    path('create-property/', CreatProperty.as_view(), name='create-property'),
]