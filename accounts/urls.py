from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signupview, name='signup'),  # Add a name to the path
]