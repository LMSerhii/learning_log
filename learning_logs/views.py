from django.shortcuts import render
from .models import Topic


def index(request):
    """ main page """
    title = 'Learning_log'
    content = {'title': title}
    return render(request, 'learning_logs/index.html', content)


def topics(request):
    """ page show all topics """
    title = 'Topics'
    topics = Topic.objects.order_by('date_added')

    content = {'title': title, 'topics': topics}
    return render(request, 'learning_logs/topics.html', content)


def topic(request, topic_id):
    """ this page show topic page"""
    title = 'Topic'
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    content = {'title': title, 'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', content)