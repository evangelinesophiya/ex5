from django.contrib import admin
from django.urls import path
from mathapp.views import index  # Import the view directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Directly map root URL to the view
]
