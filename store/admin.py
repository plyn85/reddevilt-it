from django.contrib import admin
from .models import Product, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = (

        'name',
        'description',
        'price',
        'image',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('transaction_id', 'date_ordered')

    fields = ("profile", 'transaction_id', 'date_ordered', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',
              )

    list_display = ('transaction_id', 'date_ordered', 'full_name',
                    )

    ordering = ('-date_ordered',)


admin.site.register(Order, OrderAdmin)
