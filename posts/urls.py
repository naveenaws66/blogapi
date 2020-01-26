from django.urls import path

from rest_framework.routers import SimpleRouter

#from .views import PostList, PostDetail, UserList, UserDetail

from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, base_name = 'users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls


# urlpatterns = [
#     path('', PostList.as_view(), name='home'),
#     path('<int:pk>/', PostDetail.as_view(), name='detail'),
#     path('user/', UserList.as_view(), name='userlist'),
#     path('user/<int:pk>/', UserDetail.as_view()),
# ]