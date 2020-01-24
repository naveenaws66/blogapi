from django.urls import path
from .view import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<int:pk>/', PostDetail.as_view(), name='detail'),
]