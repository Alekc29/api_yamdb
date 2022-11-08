from django.urls import path

from .views import post_get_token, post_signup

app_name = 'api.v1.auth'

urlpatterns = [
    path('signup/', post_signup),
    path('token/', post_get_token)
]
