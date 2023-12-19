from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.register.as_view(), name= 'register_page'),
    path('login/', views.login.as_view(), name= 'login_page'),
    path('logout/', LogoutView.as_view(), name= 'logout_page'),
    path('profile/', views.profile, name= 'profile_page'),
    path('edit_profile/<int:id>', views.edit_profile.as_view(), name= 'edit_profile_page'),
]
