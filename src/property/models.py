import uuid
from django.db import models

class PropertyType(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Property Type', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Category(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Property Category', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Categories'


class Property(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Property Name', max_length=100)

    # characteristics
    rent_cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Property rent price", blank=True)
    primary_cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Property price")
    bedrooms = models.IntegerField()
    kitchen = models.IntegerField()
    bathroom = models.IntegerField()
    property_size = models.CharField(max_length=50)
    furnished = models.BooleanField(default=True)
    description = models.TextField()
    localtion = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    is_featured = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    property_age = models.IntegerField()


    # foreignkey fields
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, verbose_name="Property Type")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Property Category")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def property_img(self):
        return self.images_set.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Properties'


class Images(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()

    # foreign key relationship
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = 'Images'