from django.contrib import admin

from main_board.models import MarketIndex, ValueUpdate


class MarketIndexAdmin(admin.ModelAdmin):
    fields = ['ticker', 'name']


admin.site.register(MarketIndex, MarketIndexAdmin)
admin.site.register(ValueUpdate)
