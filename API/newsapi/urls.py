from django.urls import path
from . views import newsAPIView

urlpatterns = [
     path('newsapi/', newsAPIView.as_view())
]