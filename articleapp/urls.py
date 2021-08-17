

from articleapp.views import ArticleCreateView, ArticleDeleteView, ArticleDetatilView, ArticleListView, ArticleUpdateView
from django.urls.conf import path
from django.views.generic import TemplateView

app_name = 'articleapp'
urlpatterns = [
    path('list/', ArticleListView.as_view(template_name='articleapp/list.html'), name='list'),

    path('create/', ArticleCreateView.as_view(template_name='articleapp/create.html'), name='create'),
    path('detail/<int:pk>', ArticleDetatilView.as_view(
        template_name='articleapp/detail.html'), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(
        template_name='articleapp/update.html'), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(
        template_name='articleapp/delete.html'), name='delete'),



]
