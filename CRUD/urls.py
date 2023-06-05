from django.contrib import admin
from django.urls import path, include
from CRUD.views import PessoaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pessoas', PessoaViewSet, basename='Pessoas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
]