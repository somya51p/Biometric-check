from django.contrib import admin
from django.urls import path
from verify.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_home/', admin_home, name='admin_home'),
    path('', login_admin, name='login')

]