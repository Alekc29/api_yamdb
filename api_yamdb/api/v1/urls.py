from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ..views import (CategoryViewSet, CommentViewSet, GenreViewSet, GetTokenAPI,
                    ReviewViewSet, SignupAPI, TitleViewSet, UserViewSet)

app_name = 'v1'

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
    path('/', include(router.urls)),
    path('/', include(router.urls), name='api-root'),
    path('/auth/signup/', SignupAPI.as_view(), name='signup'),
    path('/auth/token/', GetTokenAPI.as_view(), name='token')
]