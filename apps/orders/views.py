from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja_jwt.authentication import JWTAuth

from .models import Order, Category
from .serializers import OrderListSerializer, OrderDetailSerializer, OrderUpdateSerializer, CategoryListSlug

router = Router()


@router.get("/orders", response=list[OrderListSerializer], auth=JWTAuth())
def all_orders(request):
    orders = Order.objects.filter(user=request.user)
    orders = [
        {
            'id': order.id,
            'title': order.title,
            'description': order.description,
            'category': order.category.slug
        } for order in orders
    ]
    return orders



@router.get("/orders/{pk}", response=OrderDetailSerializer)
def get_order(request, pk: int):
    order = get_object_or_404(Order, pk=pk)
    order = {
        'title': order.title,
        'description': order.description,
        'category': order.category.id
    }
    return order



@router.patch("/orders/{pk}", response=OrderDetailSerializer, auth=JWTAuth())
def get_order(request, pk: int, order: OrderUpdateSerializer):
    my_order = get_object_or_404(Order, pk=pk, user=request.user)
    my_order.title = order.title or my_order.title
    my_order.description = order.description or my_order.description
    my_order.save()
    response = {
        "title": my_order.title,
        "description": my_order.description,
        "category": my_order.category.slug
    }
    return response



@router.post("/orders", response=OrderListSerializer, auth=JWTAuth())
def create_order(request, order: OrderDetailSerializer):
    user = request.user
    category = get_object_or_404(Category, slug=order.category)
    new_order = Order.objects.create(
        category=category,
        user=user,
        title=order.title,
        description=order.description
    )
    response = {
        'id': new_order.id,
        'title': new_order.title,
        'description': new_order.description,
        'category': new_order.category.slug
    }
    return response



@router.delete("/orders/{pk}", auth=JWTAuth())
def create_order(request, pk: int):
    new_order = Order.objects.filter(user=request.user)
    new_order = get_object_or_404(new_order, pk=pk, user=request.user)
    new_order.delete()
    return JsonResponse({"detail": "Order successfully deleted"})



@router.post("/category", response=list[OrderListSerializer])
def category_orders(request, category: CategoryListSlug):
    categories = [
        get_object_or_404(Category, slug=slug)
        for slug in category.slug
    ]
    category_filter = Q()
    for item in categories:
        category_filter |= Q(category=item)

    orders = Order.objects.filter(category_filter)
    response = [
        {
            'id': order.id,
            'title': order.title,
            'description': order.description,
            'category': order.category.slug
        } for order in orders
    ]
    return response
