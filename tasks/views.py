from rest_framework.generics import ListCreateAPIView
from tasks.models import Task
from tasks.serializers import TaskSerializer

class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
