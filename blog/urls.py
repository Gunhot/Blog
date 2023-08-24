from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router	= DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'blog', BlogViewSet)

urlpatterns	= [
    path('', include(router.urls)), 
]
# urlpatterns = [


    # #	user	urls
    # path('user/', UserViewSet.as_view({'get':'list', 'post':'create'})),
    # path('user/<int:pk>/', UserViewSet.as_view({'get':'retrieve', 'put':'update','patch':'partial_update','delete':'destroy'})),
    # #	blog	urls
    # path('blog/', BlogViewSet.as_view({'get':'list', 'post':'create'})),
    # path('blog/<int:pk>/', BlogViewSet.as_view({'get':'retrieve', 'put':'update','patch':'partial_update','delete':'destroy'})),
# ]


# urlpatterns = [
    # # user urls
    # # as_view : view처럼 쓸 수 있음
    # path('create-user/', UserCreateAPIView.as_view()),
    # path('list-user/', UserListAPIView.as_view()),
    # path('retrieve-user/<int:pk>/', UserRetrieveAPIView.as_view()),
    # path('update-user/<int:pk>/', UserUpdateAPIView.as_view()),
    # path('destroy-user/<int:pk>/', UserDestroyAPIView.as_view()),

    # path('create-blog/', BlogCreateAPIView.as_view()),
    # path('list-blog/', BlogListAPIView.as_view()),
    # path('retrieve-blog/<int:pk>/', BlogRetrieveAPIView.as_view()),
    # path('update-blog/<int:pk>/', BlogUpdateAPIView.as_view()),
    # path('destroy-blog/<int:pk>/', BlogDestroyAPIView.as_view()),
# ]