from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path("list/", UserList.as_view(), name="user-list"),
    path("<int:pk>/", UserDetail.as_view(), name="user-detail"),
]
