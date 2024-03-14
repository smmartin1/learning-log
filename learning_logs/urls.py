'''Defines URL patterns for learning_logs'''
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name = 'index'),                                      #Home page
    path('topics/', views.topics, name = 'topics'),                             #Topics page
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),                #Single topic page
    path('new_topic/', views.new_topic, name = 'new_topic'),                    #New Topic page
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),     #New Entry page
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),  #Edit Entry page
]