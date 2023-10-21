
from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('likespage/', views.likespage, name='likespage'),    
    path('createjob/', views.Createjob.as_view(), name='createjob'),
    path('detail/<int:id>/', views.detail, name='detail'),
    
]
