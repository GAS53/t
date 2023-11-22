from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend

from mainapp.models import Task
from mainapp.serializers import TaskSerializer
from mainapp.paginate import TaskPagination


class TasksApiView(APIView):
    pagination_class = TaskPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.query_params.get('status')
        print(status)
        if status is not None:
            queryset = queryset.filter(task__status=status)
        return queryset

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PkTasksApiView(APIView):
    pagination_class = TaskPagination

    def get_object(self, task_id):
        try:
            return Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            raise Http404

    def put(self, request, task_id, format=None):
        tasks = self.get_object(task_id)
        serializer = TaskSerializer(tasks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id, format=None):
        tasks = self.get_object(task_id)
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)