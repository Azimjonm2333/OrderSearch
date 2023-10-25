from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from apps.orders.views import router as orders_router
from apps.accounts.views import router as users_router


api = NinjaAPI()
api.add_router("users", tags=['Auth'], router=users_router)
api.add_router("orders", tags=['Orders'], router=orders_router)


urlpatterns = [
    path("api/", api.urls),
    path("admin/", admin.site.urls),
]
