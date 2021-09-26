from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.loginview),
    path('signup/',views.signupview),
    path('loginsubmit/',views.loginsubmit),
    path('signsubmit/',views.signsubmit),
    path('logout/',views.logoutkr)
    
]
