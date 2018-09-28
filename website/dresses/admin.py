
from django.contrib import admin
from .models import Lehengas,weddingLehenga
# Register your models here.


class LehengasModalAdmin(admin.ModelAdmin):
    list_display = ['lehenga_desc','lehenga_size', 'lehenga_price', 'available', 'stock']
    search_fields = ['lehenga_desc','lehenga_size']
    class Meta:
        model = Lehengas

admin.site.register(Lehengas,LehengasModalAdmin)
admin.site.register(weddingLehenga)
