from django.urls import path
from api_solution1.views import EntityView

urlpatterns = [
    path('entities/', EntityView.as_view(), name="entities"),
]
