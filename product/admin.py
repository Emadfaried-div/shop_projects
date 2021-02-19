from django.contrib import admin
from .models import Product,ProductImage,Category,Product_Alternatives,Product_Accessories


# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Product_Alternatives)
admin.site.register(Product_Accessories)