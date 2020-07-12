from django.urls import path
from .import views
from django.urls import path, include
urlpatterns = [
    path('register/', views.newregister, name='newregister'),
    path('', include('myapi.urls')),
    path('welcome.html',views.welcome,name='welcome'),
    path('login/',views.newlogin,name='newlogin'),
    path('login/update/<id>', views.update, name='update'),
    path('addapp/', views.newaddapp, name='newaddapp'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
]
