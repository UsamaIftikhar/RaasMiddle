from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('welcome.html',views.welcome,name='welcome'),
    path('login/',views.login,name='login'),
    path('login/update/<id>', views.update, name='update'),
    path('addapp/', views.addapp, name='addapp'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
]
