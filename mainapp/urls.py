from django.urls import path

from mainapp.views import TasksApiView, PkTasksApiView

app_name = 'mainapp'

urlpatterns = [
    path("tasks/<int:task_id>/", PkTasksApiView.as_view()),
    path("tasks/", TasksApiView.as_view()),
]