from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializer import BookSerializer
from .models import Book
# Create your views here.


@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getBook(request, pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(books, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addBook(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteBook(request, pk):
    product = Book.objects.get(id=pk)
    product.delete()

    return Response("Deleted Successfully.......")
