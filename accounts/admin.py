from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserAccount


class UserAccountsAdmin(UserAdmin):
    list_display = (
        'last_name', 'first_name', 'username', 'email',
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Shipping info', {
            'fields': ('shipping_street_name', 'shipping_street_number',
                       'shipping_town_or_city', 'shipping_county',
                       'shipping_postcode', 'shipping_country')
        }),
        ('Billing info', {
            'fields': ('billing_street_name', 'billing_street_number',
                       'billing_town_or_city', 'billing_county',
                       'billing_postcode', 'billing_country')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Shipping info', {
            'fields': ('shipping_street_name', 'shipping_street_number',
                       'shipping_town_or_city', 'shipping_county',
                       'shipping_postcode', 'shipping_country')
        }),
        ('Billing info', {
            'fields': ('billing_street_name', 'billing_street_number',
                       'billing_town_or_city', 'billing_county',
                       'billing_postcode', 'billing_country')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )


admin.site.register(UserAccount, UserAccountsAdmin)
