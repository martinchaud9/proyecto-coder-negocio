from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('pages/', PostList.as_view(), name="post_list"),
    path('pages/<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('pages/crear/', PostCreate.as_view(), name="post_create"),
    path('pages/<int:pk>/editar/', PostUpdate.as_view(), name="post_update"),
    path('pages/<int:pk>/borrar/', PostDelete.as_view(), name="post_delete"),
]