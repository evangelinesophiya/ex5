from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.rectangle_area, name='areaofrectangle'),
    path('areaofrectangle/', views.rectangle_area, name='areaofrectangle'),
]