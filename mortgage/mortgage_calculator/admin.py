from django.contrib import admin

from .models import MortgageOffers


class MOAdmin(admin.ModelAdmin):
    """implements the display of the table MortgageOffers in the admin panel"""
    list_display = ('id', 'bank_name', 'term_min', 'term_max', 'rate_min', 'rate_max', 'payment_min', 'payment_max')
    list_display_links = ('id', 'bank_name')
    search_fields = ('id', 'bank_name', 'term_min', 'term_max', 'rate_min', 'rate_max', 'payment_min', 'payment_max')


admin.site.register(MortgageOffers, MOAdmin)
