from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/', views.JGdatesAPIView.as_view())
]
