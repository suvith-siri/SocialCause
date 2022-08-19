from django.urls import path 
 
from . import views 

urlpatterns = [
    path('', views.home,name="home"),
    path('ShareInfo',views.ShareInfo,name="ShareInfo"),
    path('login',views.login,name="login"),
    path('verify',views.verify, name='verify'), 
    path('tfs',views.tfs,name='tfs'),
]