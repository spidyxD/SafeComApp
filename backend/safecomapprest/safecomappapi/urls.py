from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.persons_all),
    # path('snippets/<int:pk>/', views.snippet_detail),
]