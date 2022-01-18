from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('line_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'full_name', 'user', 'email',
                       'date', 'shipping_fee', 'order_total',
                       'total_cost')
    fieldsets = (
        ('Order info', {
            'fields': ('order_number', 'full_name', 'user', 'email',
                       'date', 'shipping_fee', 'order_total',
                       'total_cost')
        }),
        ('Shipping info', {
            'fields': ('shipping_street_name', 'shipping_street_number', 'shipping_town_or_city', 
                       'shipping_county', 'shipping_postcode', 'shipping_country')
        }),
        ('Billing info', {
            'fields': ('billing_street_name', 'billing_street_number', 'billing_town_or_city',
                    'billing_county', 'billing_postcode', 'billing_country')
        })
    )

    add_fieldsets = (
        ('Shipping info', {
            'fields': ('shipping_street_name', 'shipping_street_number', 'shipping_town_or_city', 
                       'shipping_county', 'shipping_postcode', 'shipping_country')
        }),
        ('Billing info', {
            'fields': ('billing_street_name', 'billing_street_number', 'billing_town_or_city',
                    'billing_county', 'billing_postcode', 'billing_country')
        })
    )

    list_display = ('order_number', 'date', 'user',
                    'order_total', 'shipping_fee',
                    'total_cost',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)