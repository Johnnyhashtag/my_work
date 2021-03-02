""" Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),

    # Page that shows all topics
    path('topics/', views.topics, name = 'topics'),

    # Details for a single page.
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),

]