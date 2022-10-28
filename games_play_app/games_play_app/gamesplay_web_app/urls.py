from django.urls import path, include

from games_play_app.gamesplay_web_app.views import home_page, dashboard_page, \
        profile_create, profile_details, profile_edit, profile_delete, \
        game_create, game_edit, game_details, game_delete


urlpatterns = (
    path('', home_page, name='home page'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('game/', include([
        path('create/', game_create, name='game create'),
        path('details/<int:pk>/', game_details, name='game details'),
        path('edit/<int:pk>/', game_edit, name='game edit'),
        path('delete/<int:pk>/', game_delete, name='game delete'),
    ])),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
)

