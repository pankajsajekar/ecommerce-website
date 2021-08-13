from django.contrib import admin
from app.models import Contact, Products, ProductImage, OrderProductInfo, CustomePaymentMethod, Orders, CartProductInfo, \
    Cart ,CourierDetail

# Register your models here.

admin.site.register(Contact)
admin.site.register(OrderProductInfo)
admin.site.register(CustomePaymentMethod)
admin.site.register(Orders)
admin.site.register(CartProductInfo)
admin.site.register(Cart)
admin.site.register(CourierDetail)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):


    inlines = [ProductImageAdmin]
    list_per_page = 10
    ordering = ['id']

    list_display = ('product_title',)

    class Meta:
        model = Products