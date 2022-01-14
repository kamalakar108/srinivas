#POPULATE DATA IN DATA BASE
'''import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','data_base.settings')
import django
django.setup()
from Deposit.models import Customer'''


import random

def phonenumbergen():
  d1=random.randint(6,9)
  num=''+str(d1)
  for i in range(9):
     num=num+str(random.randint(0,9))
  return int(num)
def populate(n):
  for i in range(n):
       order_no=random.randint(1,99999)
       ordered_by=random.choice(["A","B","C","D"])  + str(random.randint(1,99999))
       price=random.randint(1000,9999)
       addr=random.choice(["A","B","C","D"])     + str(random.randint(1,99999))
       phone_no=phonenumbergen()

       print(order_no,ordered_by,price,addr,phone_no)
      # Customer_record=Customer.objects.get_or_create(acc_no=accno,acc_name=accname,acc_balance=accbalance,acc_adhar=accadhar,acc_address=accaddress)
populate(100)
