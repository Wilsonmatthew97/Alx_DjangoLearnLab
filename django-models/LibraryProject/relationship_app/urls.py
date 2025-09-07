from django.urls import path
from . import views
from .views import (list_books, LibraryDetailView, register, CustomLoginView, CustomLogoutView)

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name = 'library_detail'),
    path('register/', register, template_name = 'register'),
    path('login/', CustomLoginView.as_view('login')),
    path('logout/', CustomLogoutView.as_view('logout'))
]
