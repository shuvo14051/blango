from django.contrib import admin
from django.urls import path, include
from django.conf import settings

print(f"Time zone: {settings.TIME_ZONE}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
