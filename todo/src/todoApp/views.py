from django.shortcuts import render
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework import (
    status,
    viewsets,
)
from rest_framework.reverse import reverse
from rest_framework.response import Response

# Create your views here.
class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def perform_create(self, serializer):
        # save instance to get the primary key and then update the URL
        instance = serializer.save()
        instance.url = reverse('todoitem-detail', args=[instance.pk], request=self.request)
        instance.save()

    def delete(self, request):
        # Insecure deserialization vulnerability example
        data = request.data  # Assume this contains serialized data
        import pickle  # Insecure deserialization using pickle
        obj = pickle.loads(data)  # Deserialize data, potential security risk
        return Response(status=status.HTTP_204_NO_CONTENT)
