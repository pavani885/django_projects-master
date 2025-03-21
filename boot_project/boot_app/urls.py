from django.urls import path 
from .views import login_view,show1 
urlpatterns = [ 
    path('', login_view , name='login'), 
]