from django.urls import path
from .views import rag_query

urlpatterns = [
    path('rag_query/', rag_query, name='rag_query'),
]
