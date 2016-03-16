from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from todo.views import TodoListCreateAPIView, TodoRetrieveUpdateDestroyAPIView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^api/todos/$', TodoListCreateAPIView.as_view()),
    url(r'^api/todos/(?P<pk>\d+)/$', TodoRetrieveUpdateDestroyAPIView.as_view())

]
