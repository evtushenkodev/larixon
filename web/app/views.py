from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from .models import Advert
from .serializers import AdvertSerializer


class AdvertListView(ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


class AdvertDetailView(RetrieveAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

    def retrieve(self, request, *args, **kwargs):
        advert = self.get_object()
        advert.views += 1  # Увеличиваем счетчик просмотров
        advert.save()
        serializer = self.get_serializer(advert)
        return Response(serializer.data)
