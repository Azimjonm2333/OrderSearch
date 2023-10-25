from ninja import Schema
from typing import Optional




class OrderListSerializer(Schema):

    id: int
    title: str
    description: str
    category: str


class OrderDetailSerializer(Schema):

    title: str
    description: str
    category: str


class OrderUpdateSerializer(Schema):

    title: Optional[str]
    description: Optional[str]


class CategoryListSlug(Schema):
    
    slug: list[str]