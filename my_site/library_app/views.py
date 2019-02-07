from django.shortcuts import render
from django.http import HttpResponse
from library_app.models import Customer,Book
# Create your views here.
def index(request):

    list_of_customer = Customer.objects.order_by("customer_name_surname")
    list_of_books = Book.objects.order_by("book_title")
    dict = {
        'customers_dict': list_of_customer,
        'book_dict': list_of_books,
     }

    return render(request,'index.html',context = dict)

# def books(request):
#     list_of_books = Book.objects.order_by("book_title")
#     dict2 = { 'book_dict': list_of_books }
#     return render(request,"index.html",context = dict2)
