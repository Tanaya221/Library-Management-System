from django.urls import path

from . import views


urlpatterns = [
    path('signup/',views.admin_signup,name='signup'),
    path('login/',views.admin_login,name='login'),
    path('books/create/',views.create_book,name="create_book"),
    path('books/<int:book_id>/',views.list_books,name="list_books"),
    path('books/update/<int:book_id>/',views.update_book,name="update_book"),
    path('books/delete/<int:book_id>/',views.delete_book,name="delete_book")
]





