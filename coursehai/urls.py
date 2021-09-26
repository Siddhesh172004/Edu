from django.urls import path
from . import views


urlpatterns = [
    path('',views.Shop),
    path('detail/<int:id>',views.detail),
    path('cartpage/',views.Cartpage),
    path('contact/',views.Contactus),
    path('contactsubmit/',views.Contactsubmit),
    path('checkout/',views.checkout),
    path('submitcheckout/',views.submitcheckout),
    path('blogcreate/',views.blogcreate),
    path('display/',views.displayblog)
    
]
