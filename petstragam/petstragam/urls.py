from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('accounts/', include('petstragam.accounts.urls')),
    path('pets/', include('petstragam.pets.urls')),
    path('', include('petstragam.common.urls')),
    path('photos/', include('petstragam.photos.urls')),

)
