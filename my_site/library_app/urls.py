from django.conf.urls import url
from library_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^books/$', views.books, name='books'),
    url(r'^customer/$', views.customer, name='customer'),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.CustomerDetailView.as_view(), name='customer-detail'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^add_book/', views.add_book, name='add_book'),



]
