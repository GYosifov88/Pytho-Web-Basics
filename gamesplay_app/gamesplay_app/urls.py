from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/', include('gamesplay_app.game.urls')),
    path('profile/', include('gamesplay_app.profiles.urls')),
    path('', include('gamesplay_app.dashboard.urls')),

]
