from celery.result import AsyncResult
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import serializers, viewsets, permissions
from rest_framework.views import APIView

from apps.sample import tasks
from apps.sample.models import Snippet
from apps.sample.serializers import UserSerializer, GroupSerializer, SnippetSerializer


class SampleCeleryView(APIView):

    def get(self, request):
        res = tasks.sample_celery_action.delay()
        result = AsyncResult(res.task_id)
        return JsonResponse({'status': result.status, 'task_id': result.task_id})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]
