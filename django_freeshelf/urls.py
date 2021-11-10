
#### Resource for customizing registration:
## https://pythonprogramming.net/user-registration-django-tutorial/

from django.contrib import admin
from django.urls import path, include
from books import views as books_views

urlpatterns = [
    path("", books_views.list_books, name="list_books"),
    path("admin/", admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('books/add_book/', books_views.add_book, name='add_book'),
    path('books/favorites/', books_views.favorite_books, name='favorite_books'),
    path('books/favorites/remove/<int:book_id>', books_views.remove_favorite, name='remove_favorite'),
    path('books/favorites/add/<int:book_id>', books_views.add_favorite, name='add_favorite'),

    path("login/", books_views.login_custom),
    path("logout/", books_views.logout_custom),
    path("register/", books_views.register),

]

