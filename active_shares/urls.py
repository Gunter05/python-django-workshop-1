from django.urls import path
from . import views

app_name = 'active_shares'

urlpatterns = [
    path('', views.share_list_view, name='share_list')
]