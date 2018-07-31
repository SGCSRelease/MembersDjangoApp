from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:member_id>', views.profile, name='profile'),
    path('<int:member_id>/penalty', views.penalty, name='penalty')
]
