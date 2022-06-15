from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import todoModel
from .serializers import todoSerializer

@api_view(['GET'])
def ShowAll(request):
    todos = todoModel.objects.all()
    serializer = todoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request, pk):
    todos = todoModel.objects.get(id=pk)
    serializer = todoSerializer(todos, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def ViewBool(request, pt):
    todos = todoModel.objects.filter(completed=pt)
    serializer = todoSerializer(todos, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def CreateProduct(request):
    serializer = todoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateProduct(request, pk):
    todos = todoModel.objects.get(id=pk)
    serializer = todoSerializer(instance=todos, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteProduct(request, pk):
    product = todoModel.objects.get(id=pk)
    product.delete()

    return Response('Items delete successfully!')
