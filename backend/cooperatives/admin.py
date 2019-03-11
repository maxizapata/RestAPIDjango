from django.contrib import admin
from cooperatives.models import Cooperative, Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')



@admin.register(Cooperative)
class CooperativeAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'short_description',
                    'logo',
                    'description',
                    'phone',
                    'facebook_profile',
                    'address',
                    'map_latitude',
                    'map_longitude',
                    'whatsapp',
                    )



