from django.urls import path

from users.views import RegisterAPIView, BlacklistTokenUpdateView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('logout/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
]
