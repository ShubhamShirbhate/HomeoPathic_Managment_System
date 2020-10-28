from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('patinet_form/',views.patinet_form, name='patinet_form'),
    path('patient_view/',views.patient_view, name='patient_view'),
    path('search/',views.search,name='search'),
    path('create/',views.Create, name='Create'),
    path('history/',views.history, name='history')
]
