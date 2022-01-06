from django.urls import path

from book import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:rubric_id>/', views.by_rubric_view, name='by_rubric'),
    path('add/', views.PostCreateView.as_view(), name='create'),
    path('test/', views.TestView.as_view(), name='test'),
]
