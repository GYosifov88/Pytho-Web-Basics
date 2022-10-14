from django.urls import path

from gamesplay_app.dashboard.views import show_dashboard, home_page

urlpatterns = (
    path('', home_page, name='home page'),
    path('dashboard/', show_dashboard, name='dashboard')
)