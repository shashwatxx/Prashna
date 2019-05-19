from django.contrib import admin
from django.urls import path
from django.urls.conf import include, re_path
from django.conf.urls import url
from django.views.generic.base import RedirectView
from uttar import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter() 
router.register(r'topic', views.TopicViewSet)
router.register(r'like', views.LikeViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'answer', views.AnswerViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('question/', views.QuestionList.as_view()),  
    path('question/create/', views.QuestionCreate.as_view()),     
    path('answer/create/', views.AnswerCreate.as_view()),  
    path('like/create/', views.like),       
    url('question/(?P<pk>[0-9]+)/', views.QuestionDetails.as_view()), 
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),        
#     url('movie/edit/(?P<pk>[0-9]+)$', views.MovieUpdate.as_view()), 
#     url('movie/delete/(?P<pk>[0-9]+)$', views.MovieDelete.as_view()), 
    url('^$', RedirectView.as_view(url='home/'))
]
