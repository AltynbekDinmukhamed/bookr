from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book_search/', views.book_search, name='book_search'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/<int:book_id>/edit/', views.book_update, name='book_update'),
    path('book/<int:book_id>/delete/', views.book_delete, name='book_delete'),
]

