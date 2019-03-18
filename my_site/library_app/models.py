from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    customer_id=models.CharField(max_length=255)
    customer_name_surname=models.CharField(max_length=255)
    customer_mail=models.EmailField()
    customer_adress=models.CharField(max_length=255)


    def __str__(self):
        return self.customer_name_surname

    class Meta:
        ordering = ['customer_id']

class Book(models.Model):
    user_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, related_name='customer_book')
    book_title=models.CharField(max_length=255)
    book_author=models.CharField(max_length=255,default="", editable=False)
    book_isbn_no=models.CharField(max_length=255,default='SOME STRING')
    book_pub_date=models.DateField()

    def __str__(self):
        return self.book_title
