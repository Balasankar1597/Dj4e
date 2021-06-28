from django.urls import path

from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.myview),
    #path('sess',views.sessfun),
    ]