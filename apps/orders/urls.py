from django.urls import path, include
from apps.orders.views import router


urlpatterns = [    
    path('', router.urls)
]

