from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path(
        "register/",
        views.register,
        name="register",
    ),

    # Role-based views
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),

    # Permission-based book views (CHECKER REQUIRED PATHS)
    path('add_book/', add_book, name='add_book'),
    path('edit_book/', edit_book, name='edit_book'),
    path('delete_book/', delete_book, name='delete_book'),
]
