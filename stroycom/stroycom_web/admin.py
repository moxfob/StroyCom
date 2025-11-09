from django.contrib import admin
from .models import Services

@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_with_unit', 'is_aviable']
    list_filter = ['category', 'is_aviable']
    search_fields = ['name', 'description']
    list_editable = ['is_aviable']
    ordering = ['category', 'name']
    
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'description')
        }),
        ('Цена и сроки', {
            'fields': ('price', 'unit', 'duration')
        }),
        ('Статус', {
            'fields': ('is_aviable',)
        }),
    )

    def price_with_unit(self, obj):
        return f"{obj.price} ₽/{obj.unit}"
    price_with_unit.short_description = 'Стоимость'
    price_with_unit.admin_order_field = 'price'