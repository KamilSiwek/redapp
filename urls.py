from django.contrib import admin
from django.urls import path
import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', users.views.signup, name='signup'),
]
