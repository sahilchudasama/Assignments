from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
urlpatterns = [
    path('', views.index, name='index'),
    # Other paths if needed
]