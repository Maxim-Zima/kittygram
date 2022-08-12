from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Cat
from .serializers import CatSerializer


@api_view(['GET', 'POST'])
def cat_list(request):
    if request.method == 'POST':
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)


class MyAPIView(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatList(ListCreateAPIView):
    '''возвращает всю коллекцию котиков или создает новую запись в БД'''
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(RetrieveUpdateDestroyAPIView):
    '''возвращает, обновляет или удаляет объекты модели по одном '''
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatViewSet(ModelViewSet):
    '''вьюсет реализует все 6 операций CRUD для модели Cat'''
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
