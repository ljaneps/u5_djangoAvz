from django.urls import path
from .views import *

urlpatterns = [
    path('roles/',RolListCreateView.as_view(),name='Rol-list'),
    path('roles/<int:id>',RolDetailCreateView.as_view(),name='Rol-detail'),
    path('profiles/',ProfileListCreateView.as_view(),name='Profile-list'),
    path('profiles/<int:id>',ProfileDetailView.as_view(),name='Profile-detail')
]