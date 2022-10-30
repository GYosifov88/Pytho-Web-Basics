from django.urls import path, include

from car_collection_app.car_collection_web.views import home_page, catalogue_page, car_create, car_edit, car_delete,\
    car_details, profile_edit, profile_create, profile_delete, profile_details

urlpatterns = (
    path('', home_page, name='home page'),
    path('catalogue/', catalogue_page, name='catalogue page'),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
    path('car/', include([
        path('create/', car_create, name='car create'),
        path('<int:pk>/details/', car_details, name='car details'),
        path('<int:pk>/edit/', car_edit, name='car edit'),
        path('<int:pk>/delete/', car_delete, name='car delete'),
    ])),
)




