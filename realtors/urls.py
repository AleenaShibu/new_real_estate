
from django.urls import path
from .views import  AddPropertyView,DeletePropertyView,SearchPropertyView,PropertyListView,PropertyDetailView,EditPropertyView



urlpatterns = [
    path('',PropertyListView.as_view(),name = 'home'),
    path('detail/<int:pk>/',PropertyDetailView.as_view(),name = 'detail'),
    path('addproperty/',AddPropertyView.as_view(),name = 'addproperty'),
    path('delete/<int:pk>/',DeletePropertyView.as_view(),name ='delete'),
    path('edit/<int:pk>/',EditPropertyView.as_view(),name ='edit'),

    path('search/',SearchPropertyView.as_view(),name='search'),]
    

