from django.urls import path
from .views import CooperativeApiView


urlpatterns = [
    path('cooperatives/', CooperativeApiView.as_view(),
         name="cooperatives-all")
]
