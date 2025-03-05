from django.contrib import admin
from lfs_order_numbers.models import OrderNumberGenerator


class OrderNumberGeneratorAdmin(admin.ModelAdmin):
    list_display = ["last", "format"]


admin.site.register(OrderNumberGenerator, OrderNumberGeneratorAdmin)
