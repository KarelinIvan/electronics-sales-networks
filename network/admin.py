from django.contrib import admin

from network.models import NetworkElement, Product

# Register your models here.


@admin.register(NetworkElement)
class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier',
                    'debt_to_supplier', 'created_at')
    search_fields = ['name']
    list_filter = ['city']
    actions = ['clear_debts']

    def clear_debts(self, request, queryset):
        row_updated = queryset.update(debt_to_supplier=0)
        if row_updated == 1:
            message = '1 запись была обновлена'
        else:
            message = '%s записей были обновлены' % row_updated
        self.message_user(request, '%s записей были обновлены' % message)

    clear_debts.short_description = 'Очистить задолженности перед поставщиками'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('element', 'name', 'model', 'release_date')
    list_filter = ['element__country']
