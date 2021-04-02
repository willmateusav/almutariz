from django.urls import path

from almutariz.users import views as users_views

app_name = "users"

urlpatterns = [
    path(
        route='',
        view=users_views.IndexView,
        name='index'
    ), path(
        route='images/',
        view=users_views.ImagesView,
        name='blog-grid'
    ),
]
