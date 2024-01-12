# my_tennis_club.urls

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),  # Replace 'your_todo_app' with the actual app name
    # Add other app URLs as needed
]
