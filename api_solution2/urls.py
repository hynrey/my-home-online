from django.urls import path
from api_solution2.views import EntityView

urlpatterns = [
    path('entities/', EntityView.as_view(), name="entities"),
]
