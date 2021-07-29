from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)
router.register('polls', views.PollsViewSet)
router.register('answers',views.AnswerViewSet, basename='answer')
router.register('my-answers', views.MyAnswers,basename='my-answers')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
