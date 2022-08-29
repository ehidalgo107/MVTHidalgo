from django.contrib import admin
from django.urls import path
from myapp.views import lista_familia
from . import views

urlpatterns = [
    path('lista_familia/', lista_familia),
    path('admin/', admin.site.urls),

]