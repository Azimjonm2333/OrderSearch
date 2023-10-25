from django.urls import path, include
from apps.accounts.views import router
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )




urlpatterns = [
    path('', router.urls),
    # # token
    # path('token/refresh/', TokenRefreshView.as_view()),
]
