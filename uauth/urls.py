from django.urls import path
from uauth.views import login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url')
]
