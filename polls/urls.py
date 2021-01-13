
from django.urls import path, include
from django.conf.urls import url
from . import views
app_name = 'polls'

urlpatterns = [
path('', views.IndexView.as_view(), name='index' ), 
path('/', views.DetailView.as_view(), name='detail'),
path('/results', views.ResultsView.as_view(), name='results'),
path('/vote', views.vote, name='vote'),
]
