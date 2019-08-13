from django.shortcuts import render
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework import (
    status,
    viewsets,
)
from rest_framework.reverse import reverse
#from rest_framework.decorators import list_route
from rest_framework.response import Response

# Create your views here.
class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def perform_create(self, serializer):
        # save instance to get the primary key and then update the URL
        # save the instance
        instance = serializer.save()
        # generate url
        instance.url = reverse('todoitem-detail', args=[instance.pk], request=self.request)
        # persist the instance
        instance.save()
    
    def delete(self, request):
        # delete all todo items
        TodoItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
