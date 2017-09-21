from core.models import TipoDivisa
from .serializers import TipoDivisaSerializer
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TipoDivisa(viewsets.ModelViewSet):
    queryset = TipoDivisa.objects.all()
    serializer_class = TipoDivisaSerializer


class TipoDivisaList2(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        divisas = TipoDivisa.objects.all()
        serializer = TipoDivisaSerializer(divisas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TipoDivisaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DivisaViewSetDetail(APIView):
    """
    Retrieve, update or delete a Divisa instance.
    """
    def get_object(self, pk):
        try:
            return Divisa.objects.get(pk=pk)
        except Divisa.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        divisa = self.get_object(pk)
        serializer = DivisaSerializer(divisa)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        divisa = self.get_object(pk)
        serializer = DivisaSerializer(divisa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        divisa = self.get_object(pk)
        divisa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
