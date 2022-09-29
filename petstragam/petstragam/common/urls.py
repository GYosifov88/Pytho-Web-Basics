from django.urls import path

from petstragam.common.views import index

urlpatterns = (
    path('', index, name='index'),
)