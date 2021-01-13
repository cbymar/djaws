

from django.conf.urls import url
from . import views
app_name = 'polls'

urlpatterns = [
path(r'^$', views.IndexView.as_view(), name='index' ), 
path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
path(r'^(?P<pk>[0-9]+)/results$', views.ResultsView.as_view(), name='results'),
path(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote'),
]
