from django.urls import path

from almutariz.users import views as users_views

app_name = "users"

urlpatterns = [
    path(
        route='',
        view=users_views.IndexView.as_view(),
        name='index'
    ),
]
