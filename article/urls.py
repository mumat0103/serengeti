import imp
from django.urls import path
from .views import delete, new, show, edit, delete

app_name = 'article'

urlpatterns = [
    path('new', new, name='new'),
    path('<int:id>', show, name='show'),
    path('<int:id>/edit', edit, name='edit'),
    path('<int:id>/delete', delete, name='delete'),

]
