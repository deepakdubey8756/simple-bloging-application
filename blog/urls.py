from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('details/<slug:slug>', views.details, name="post_detail")
]
