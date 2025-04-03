from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/<int:user_profile_id>/', views.profile, name='profile'),
    path('multiplication_table/', views.multiplication_table, name='multiplication_table'),
]
