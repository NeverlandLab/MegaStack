from django.urls import path, include
from rest_framework import routers

from apps.sample import views
from apps.sample.views import SampleCeleryView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'snippet', views.SnippetViewSet)

urlpatterns = [
    path('simple_celery_action/', SampleCeleryView.as_view()),
    path('', include(router.urls)),
]
