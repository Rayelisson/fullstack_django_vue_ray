from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('account.urls')),
    path('api/posts/', include('post.urls')),
    path('api/search/', include('search.urls')),
    path('admin/', admin.site.urls),
]
