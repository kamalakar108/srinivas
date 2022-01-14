from django.contrib import admin
from apparel.models import PRODUCTS,CUSTOMERS,ORDERS

 # Register your models here.

class PRODUCTSAdmin(admin.ModelAdmin):
    list_display=['id','Prod_Descript','Price','hlink']

admin.site.register(PRODUCTS,PRODUCTSAdmin)

# Register your models here.
class CUSTOMERSAdmin(admin.ModelAdmin):
    list_display=['C_name','Ph_no','Address','email']

admin.site.register(CUSTOMERS,CUSTOMERSAdmin)

class ORDERSAdmin(admin.ModelAdmin):
    list_display=['Ordered_by','Price','Quantity','C_id']

admin.site.register(ORDERS,ORDERSAdmin)
