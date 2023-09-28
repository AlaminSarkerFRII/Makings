from django.contrib import admin
from .models import Catagory,Item

# Register your models here.

#===================> CatagoryAdmin for Catagory Model ===================>

class CatagoryAdmin(admin.ModelAdmin):
    proxy = True



admin.site.register(Catagory,CatagoryAdmin)


#===================> ItemAdmin for Item Model ===================>


class ItemAdmin(admin.ModelAdmin):
    proxy = True


admin.site.register(Item,CatagoryAdmin)