

from subscribeapp.views import SubscriptionListView, SubscriptionView
from django.urls.conf import path

app_name = 'subscribeapp'


urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),


]
