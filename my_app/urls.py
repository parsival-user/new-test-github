
from django.urls import path
from my_app.views import hole_product, completed_product, waiting_product

urlpatterns = [
    path('completed_product/',completed_product),
    path('waiting_product/',waiting_product),
    path('hole_product/',hole_product),
]
