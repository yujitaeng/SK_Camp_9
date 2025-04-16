from django.urls import path, include
from rest_framework.routers import DefaultRouter
from qna.views import QuestionViewSet, AnswerViewSet
from rest_framework_nested.routers import NestedSimpleRouter

# /api로 시작하는 기본 url 설정
router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)

questions_router = \
    NestedSimpleRouter(router, r'questions', lookup='question')
questions_router.register\
    (r'answers', AnswerViewSet, basename='question-answers')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(questions_router.urls)),
]

"""
생성된 url 패턴

api/ ^questions/$ [name='question-list']
api/ ^questions\.(?P<format>[a-z0-9]+)/?$ [name='question-list']
api/ ^questions/(?P<pk>[^/.]+)/$ [name='question-detail']
api/ ^questions/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='question-detail']
api/ ^answers/$ [name='answer-list']
api/ ^answers\.(?P<format>[a-z0-9]+)/?$ [name='answer-list']
api/ ^answers/(?P<pk>[^/.]+)/$ [name='answer-detail']
api/ ^answers/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='answer-detail']
api/ [name='api-root']
api/ <drf_format_suffix:format> [name='api-root']
"""
