from django.urls import path
from .views import *
app_name='accapp'

urlpatterns = [
    path('',home,name='homeurl'),
    path('login/',mylogin,name='myloginurl'),
    path('register/',createuser,name='registerurl'),
    path('catalog/',addproduct,name='catalogaddurl'),
    path('cataloglist',listproduct,name='cataloglisturl'),
    path('logout/',mylogout,name='mylogouturl'),
    path('hfgg/',contact,name='reachurl'),
]
