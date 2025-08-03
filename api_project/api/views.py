from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# ListAPIView (optional, if still needed)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ✅ This is the required BookViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
