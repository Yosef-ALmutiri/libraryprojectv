from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    
    path('html5/links/', views.links_page, name='books.links_page'),
    path('html5/text/formatting/', views.formatting_page, name='books.formatting_page'),
    path('html5/listing/', views.listing_page, name='books.listing_page'),
    path('html5/tables/', views.tables_page, name='books.tables_page'),

    path('search/', views.search_books, name='books.search'),
    
    path('simple/', views.search_books, name='books.search'),

    path('simple/query/', views.simple_query, name='books.simple_query'),
    path('complex/query/', views.complex_query, name='books.complex_query'),
]