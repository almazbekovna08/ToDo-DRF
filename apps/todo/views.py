# Create your views here.
from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import User, Todo
from .serializer import UserSerializer, TodoSerializer
from rest_framework.permissions import IsAuthenticated



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_completed']
    search_fields = ['title', 'description']
    ordering = ['-created_at'] 

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Todo.objects.filter(user=self.request.user)
        return Todo.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, pk=None):
        try:
            todo = Todo.objects.get(id=pk, user=request.user)
            todo.delete()
            return Response({"message": "Задача удалена"})
        except Todo.DoesNotExist:
            return Response({"error": "Задача не найдена"})
        
    def update(self, request, pk=None):
        try:
            todo = Todo.objects.get(id=pk, user=request.user)
            serializer = self.get_serializer(todo, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Задача обновлена", "todo": serializer.data})
        except Todo.DoesNotExist:
            return Response({"error": "Задача не найдена"})


class DeleteAllTasksViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request):
        Todo.objects.filter(user=request.user).delete()
        return Response({"message": "Все задачи удалены"})
