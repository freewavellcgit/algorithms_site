from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:algorithm_id>/', views.detail, name='detail'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')
]
