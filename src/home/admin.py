from django.contrib import admin
from .models import Product,Member

# Register your models here
class ProductAdmin(admin.ModelAdmin):
    list_display =('name','price','_description','image','stock')
    list_editable = ('price','stock',)
    search_fields = ('name',)

    def _description(self, obj):
        return f"{obj.description[:30]} ..."

    # def _image(self, obj):
    #     return f"<img height='200' width='200' src='{obj.image.url}'/>"

admin.site.register(Product,ProductAdmin)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number','email')
    list_editable =('phone_number',)
    search_fields =('phone_number',)
admin.site.register(Member, MemberAdmin)
