from.import views
from django.urls import path

urlpatterns = [
    path('',views.static,name='static'),

]