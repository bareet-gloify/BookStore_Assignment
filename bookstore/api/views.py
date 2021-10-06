from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . serializer import *
from .models import *
# Create your views here.


class UserLoginView(APIView):
    def post(self, request):
        data = request.data
        name = data.get('name')
        password = data.get('password')
        try:
            user = User.objects.get(name=name)
        except:
            return Response("Wrong Credentials")

        if(getattr(user, 'password') == password):
            return Response("Logged In Successfully")
        else:
            return Response("Wrong Credentials")

# ---------------------------------------------------------------------------


class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response("Deleted Successfully.......")


class UserDetailAPIView(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

# ----------------------------------------------------------------------------------------------------


class BookStoreAPIView(APIView):
    def get(self, request):
        bookStores = BookStore.objects.all()
        serializer = BookStoreSerializer(bookStores, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = BookStoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        bookStore = BookStore.objects.get(id=pk)
        serializer = BookStoreSerializer(instance=bookStore, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        bookStore = BookStore.objects.get(id=pk)
        bookStore.delete()
        return Response("Deleted Successfully.......")


class BookStoreDetailAPIView(APIView):
    def get(self, request, pk):
        bookStore = BookStore.objects.get(id=pk)
        serializer = BookStoreSerializer(bookStore, many=False)
        return Response(serializer.data)

# ---------------------------------------------------------------------------


class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response("Deleted Successfully.......")


class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)
