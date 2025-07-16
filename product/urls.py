from django.urls import path

from .views import ProductCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('create/', ProductCreateAPIView.as_view())
]