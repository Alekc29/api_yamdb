from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                     ReviewViewSet, TitleViewSet, UserViewSet)
import api.v1.auth.urls

app_name = 'api.v1'

router = DefaultRouter()
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')
router.register("categories", CategoryViewSet, basename="categories")
router.register("genres", GenreViewSet, basename="genres")
router.register("titles", TitleViewSet, basename="titles")
router.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls), name='api-root'),
    path('auth/', include(api.v1.auth.urls)),
]
