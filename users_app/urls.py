
from django.urls import path
from django.contrib.auth.views import LoginView,logout_then_login



urlpatterns = [
    path('', LoginView.as_view(template_name='users_app/login.html'), name="login"),
    path('logout/', logout_then_login, name="logout_then_login")
    
]
