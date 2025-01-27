from django.urls import path
from .views import (
    CartInfoCreateView,
    CartInfoView,
    ItemCreateView,
    ItemView,
    ItemDeleteView,
)

urlpatterns = [
    path("api/new/", CartInfoCreateView.as_view(), name="cart-create"),
    path("api/<uuid:id>/", CartInfoView.as_view(), name="cart"),
    path("api/item/new/", ItemCreateView.as_view(), name="item-create"),
    path("api/item/<uuid:id>/", ItemView.as_view(), name="item"),
    path("api/item/dev_null/<uuid:id>/", ItemDeleteView.as_view(), name="item"),
]
