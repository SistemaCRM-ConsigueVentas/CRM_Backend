from django.contrib import admin
from api.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
#admin.site.register(Employees)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Promotion)
admin.site.register(Service)
admin.site.register(SaleDetailsService)
admin.site.register(SaleDetailsProduct)
admin.site.register(Provider)
admin.site.register(Payment)
admin.site.register(Purchase)