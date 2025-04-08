from django.urls import path
from .views import (
    GuestListView,
    GuestCreateView,
    GuestUpdateView,
    GuestDeleteView
)

app_name = 'guestbook'  # ini penting buat {% url 'guestbook:list' %} di template

urlpatterns = [
    path('', GuestListView.as_view(), name='list'),
    path('create/', GuestCreateView.as_view(), name='create'),
    path('update/<str:id>/', GuestUpdateView.as_view(), name='update'),
    path('delete/<str:id>/', GuestDeleteView.as_view(), name='delete'),
]
