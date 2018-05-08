from django.contrib import admin
from django.urls import include, path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('', views.index, name="index"),
]
