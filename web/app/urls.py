from django.urls import path

from .views import AdvertListView, AdvertDetailView

urlpatterns = [
    path('advert-list/', AdvertListView.as_view(), name='advert-list'),
    path('advert/<int:pk>/', AdvertDetailView.as_view(), name='advert-detail'),
]
