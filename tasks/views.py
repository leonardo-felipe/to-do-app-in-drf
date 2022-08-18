from rest_framework.views import APIView 
from rest_framework.response import Response
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskAPIView(APIView):
    
    def get(self, request):
        title = Task.objects.all()
        serializer = TaskSerializer(title, many=True)
        return Response(serializer.data)
