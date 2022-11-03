from django.urls import include, path
from .views import CategoryViewSet, GenreViewSet, TitleViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("genres", GenreViewSet, basename="genres")
router.register("titles", TitleViewSet, basename="titles")


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(router.urls), name='api-root'),
]