from ninja import Schema


class CategoryListSerializer(Schema):

    id: int
    name: str
    slug: str


class CategoryDetailSerializer(Schema):

    id: int
    name: str
    slug: str
    parent: int
    created_at: str
    updated_at: str


class CategoryCreateSerializer(Schema):

    name: str
    parent: int
