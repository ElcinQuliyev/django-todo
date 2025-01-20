from django.urls import path
from .views import home_view, todo_list_view


urlpatterns = [
    path('home/', home_view, name='home'),
    path('todo_list/', todo_list_view, name='todo_list')
]