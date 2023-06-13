from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
    path('list/', views.List.as_view(), name='list'),
    path('edit/<int:pk>/', views.Update.as_view(), name='edit'),
    path('deletev/<int:pk>/', views.Delete.as_view(), name='deletev'),
]
