from django.urls import path, include
from todoApp import views
from rest_framework.routers import DefaultRouter

# Create default router object and register the viewsets with it
router = DefaultRouter(trailing_slash=False)
router.register('todos', views.TodoItemViewSet)
urlpatterns = [
    path('', include(router.urls)),
]