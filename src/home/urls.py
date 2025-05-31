
from django.urls import path
from .views import home,products,contacts,about


urlpatterns = [
    
    path('', home, name='home'),
    path('products/',products, name='products'),
    path('contacts/',contacts,name='contacts'),
    path('about/',about,name='about'),
]