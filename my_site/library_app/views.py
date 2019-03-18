from django.shortcuts import render
from django.http import HttpResponse
from library_app.models import Customer,Book
from django.shortcuts import render
from django.views import generic
from .forms import BookForm


def login():
    pass


def logout():
    pass


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book
    template_name = 'library_app/book-detail.html'



class CustomerDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Customer
    template_name = 'library_app/customer-detail.html'


# Create your views here.
def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    dict={'num_visits': num_visits,}
    return render(request,'index.html',context=dict)

def modal(request):
    return render(request,'modal.html')

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def books(request):
    list_of_books = Book.objects.order_by("id")
    number_of_books = Book.objects.all().count()

    dict = {
        'list_of_books': list_of_books,
        'number_of_books': number_of_books,
     }
    return render(request,'books.html',context = dict)

def customer(request):
    list_of_customer = Customer.objects.order_by("id")
    number_of_customer = Customer.objects.all().count()

    dict = {
        'list_of_customer': list_of_customer,
        'number_of_customer': number_of_customer,
     }
    return render(request,'customer.html',context = dict)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['book_title']
            author = form.cleaned_data['book_author']
            isbn = form.cleaned_data['book_isbn_no']
            date = form.cleaned_data['book_pub_date']
            book = Book(book_title=title,book_author=author,book_isbn_no=isbn,book_pub_date=date)
            book.save()
            return HttpResponseRedirect('/')




    return render(request,'add_book.html',{'form': form})







# def books(request):
#     list_of_books = Book.objects.order_by("book_title")
#     dict2 = { 'book_dict': list_of_books }
#     return render(request,"index.html",context = dict2)
