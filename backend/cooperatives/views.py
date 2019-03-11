from rest_framework import generics
from .models import Cooperative
from .serializer import CooperativeSerializer


class CooperativeApiView(generics.ListAPIView):
    queryset = Cooperative.objects.all()
    serializer_class = CooperativeSerializer
