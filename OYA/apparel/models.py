from django.db import models
class PRODUCTS(models.Model):

     Prod_Descript=models.CharField(max_length=30)
     Price=models.FloatField()
     hlink= models.URLField(max_length=200)
     #hlink=models.CharField(max_length=30)

     def __str__(self):
         return self.Prod_Descript

class CUSTOMERS(models.Model):
     C_name=models.CharField(max_length=20)
     Ph_no=models.IntegerField()
     Address=models.CharField(max_length=30)
     email= models.EmailField(max_length=254)

     def __str__(self):
         return self.C_name

class ORDERS(models.Model):
    Ordered_by=models.CharField(max_length=20)
    Price=models.FloatField()
    Quantity=models.IntegerField()
    C_id=models.ForeignKey(CUSTOMERS, on_delete=models.CASCADE)
    P_id=models.ManyToManyField(PRODUCTS)
    def __str__(self):
        return self.Ordered_by
