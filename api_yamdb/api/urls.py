from django.urls import include, path
import api.v1.urls

app_name = 'api'


urlpatterns = [
    path('v1/', include(api.v1.urls)),
]
