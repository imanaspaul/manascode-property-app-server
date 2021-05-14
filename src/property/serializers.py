from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from . models import Category, Images, Property, PropertyType

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class CreateCategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ["id"]


class PropertyTypeSerializer(ModelSerializer):

    class Meta:
        model = PropertyType
        fields = "__all__"


class CreatePropertyTypeSerializer(ModelSerializer):

    class Meta:
        model = PropertyType
        fields = ["id"]


class ImageSerializer(ModelSerializer):

    class Meta:
        model = Images
        fields = ["id", "url"]



class GetPropertySerializer(ModelSerializer):
    
    property_img = ImageSerializer(many=True)
    property_type = PropertyTypeSerializer()
    category = CategorySerializer()

    class Meta:
        model = Property
        fields = [
            "id", 
            "name",
            "rent_cost",
            "primary_cost",
            "bedrooms",
            "kitchen",
            "bathroom",
            "property_size",
            "furnished",
            "description",
            "localtion",
            "category", 
            "property_img",
            "landmark",
            "latitude",
            "longitude",
            "is_featured",
            "on_sale",
            "sold",
            "property_age",
            "property_type",
            "category",
            "created_at"
            ]


class CreatePropertySerializer(ModelSerializer):
    
    property_img = ImageSerializer(many=True)
    property_type = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=PropertyType.objects.all())
    category = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Category.objects.all())

    class Meta:
        model = Property
        fields = [
            "id", 
            "name",
            "rent_cost",
            "primary_cost",
            "bedrooms",
            "kitchen",
            "bathroom",
            "property_size",
            "property_img",
            "furnished",
            "description",
            "localtion",
            "category", 
            "landmark",
            "latitude",
            "longitude",
            "is_featured",
            "on_sale",
            "sold",
            "property_age",
            "property_type",
            "category",
            "created_at"
            ]
    
    def create(self, validated_data):
        images = validated_data.pop('property_img')

        property = Property.objects.create(**validated_data)
        # property.save()
        for img in images:
            Images.objects.create(**img, property=property)
        # question.tags.set(tags)
        return property