from django.contrib import admin

from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_filter = ['customer__username', 'category']
    search_fields = ['title']
    exclude = ['image']
    ordering = ['price']

    # def has_delete_permission(self, request, obj=...):
        

    # def has_add_permission(self, request):
    #     return super().has_add_permission(request)
    
    # def has_change_permission(self, request, obj = ...):
    #     return request.user == obj.customer

admin.site.register(Category)