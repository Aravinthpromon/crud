from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),      # URL for the admin panel
    path('api/', include('tasks.urls')),  # Include the URLs from the 'tasks' app
]
