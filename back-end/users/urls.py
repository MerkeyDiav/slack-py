from django.urls import path, include
from .views import UserList, UserDetail

urlpatterns = [
    path("list/", UserList.as_view(), name="user-list"),
    path("int:pk>/", UserDetail.as_view(), name="user-detail"),
    path("api-auth/", include("rest_framework.urls")),
    path("dj-rest/auth/", include("dj_rest_auth.urls")),
    path("dj-rest/registration/", include("dj_rest_auth.registration.urls")),
]
