from django.contrib import admin
from django.contrib.auth.models import Group
from . models import PropertyType ,Category ,Property, Images

admin.site.register(PropertyType)
admin.site.register(Category)
admin.site.register(Property)
admin.site.register(Images)


admin.site.unregister(Group)