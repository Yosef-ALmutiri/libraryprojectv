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

    path('lab8/task1/', views.task1, name='task1'),
    path('lab8/task2/', views.task2, name='task2'),
    path('lab8/task3/', views.task3, name='task3'),
    path('lab8/task4/', views.task4, name='task4'),
    path('lab8/task5/', views.task5, name='task5'),
    path('lab8/task7/', views.task7, name='task7'),

    #lab9
    path('lab9/task1/', views.task1_lab9, name='lab9_task1'),
    path('lab9/task2/', views.task2_lab9, name='lab9_task2'),
    path('lab9/task3/', views.task3_lab9, name='lab9_task3'),
    path('lab9/task4/', views.task4_lab9, name='lab9_task4'),
    path('lab9/task5/', views.task5_lab9, name='lab9_task5'),
    path('lab9/task6/', views.task6_lab9, name='lab9_task6'),

    #Lab10
    path('lab9_part1/listbooks', views.listbooks, name='listbooks'),
    path('lab9_part1/addbook', views.addbook, name='addbook'),
    path('lab9_part1/editbook/<int:id>', views.editbook, name='editbook'),
    path('lab9_part1/deletebook/<int:id>', views.deletebook, name='deletebook'),

    # Lab10_Part2
    path('lab9_part2/listbooks', views.listbooks2, name='listbooks2'),
    path('lab9_part2/addbook', views.addbook2, name='addbook2'),
    path('lab9_part2/editbook/<int:id>', views.editbook2, name='editbook2'),
    path('lab9_part2/deletebook/<int:id>', views.deletebook2, name='deletebook2'),
]