from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, BookViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'posts', PostViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]