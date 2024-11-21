from django.urls import path

from perstagram.common import views

urlpatterns = (
    path('', views.home_page, name = 'home'),
)